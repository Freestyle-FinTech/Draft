import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import csv
import operator

solvers.options['show_progress'] = False

#Read prices
def read_prices(file_path):
	port_price = list(csv.reader(open(file_path)))
	port_price = np.delete(np.asmatrix(port_price),(0),axis=1)
	port_price = np.delete(np.asmatrix(port_price),(0),axis=0)
	port_price = port_price.astype(np.float)
	return port_price

#Here assume using simplest return
def get_return(prices,return_type):
	prices = np.array(prices)
	if return_type == "log": stock_return = np.log(prices[1:]/prices[:-1])
	else: stock_return = prices[1:]/prices[:-1]-1
	return stock_return

def possible_portfolios(returns,n_port,fq_adj):
	#randomly generate n weights
	n_asset = len(returns.T)
	weights = []
	np.random.seed(123)
	for i in range(n_port):
		w = np.random.randn(n_asset)
		weights.append(w/sum(w))
	weights = np.matrix(weights)

	#calculate the random returns and risks
	#assume: returns for each asset is a column vector
	returns = returns.T
	expect_return = np.matrix(np.mean(returns,axis = 1)) #here we get a row vector
	covariance = np.cov(returns)
	port_returns = []
	port_risks = []
	for row in weights:
		returns = float(row * expect_return.T)
		risks = float(np.sqrt(row * covariance * row.T))
		while(risks > 0.03):
			w = np.random.randn(n_asset)
			w = np.asmatrix(w/sum(w))
			returns = float(w * expect_return.T)
			risks = float(np.sqrt(w * covariance * w.T))
		port_returns.append(np.array(returns*fq_adj))
		port_risks.append(np.array(risks*np.sqrt(fq_adj)))
	return port_risks, port_returns

def	efficient_frontier(returns,tolerance,fq_adj):
	if type(tolerance) in [int,float]: tolerance = [tolerance]
	n_asset = len(returns.T)
	returns = np.asmatrix(returns.T)
	#Assume
	#returns of each asset is a column vector
	#rq_returns only contains the smallest and biggest ones

	#this parameter should be adjusted according to characteristics of different database
	#parameter = 1.8
	#N = 100
	#tolerance = [10**(5 * t/N - 1.0) for t in range(N)]

	covariance = opt.matrix(np.cov(returns))
	expect_return = opt.matrix(np.mean(returns,axis = 1))

	#Constraint Matrices
	G = -opt.matrix(np.eye(n_asset))
	h = opt.matrix(0.0,(n_asset,1))
	A = opt.matrix(1.0,(1,n_asset))
	b = opt.matrix(1.0)

	#Optimization
	ef_frontier = [solvers.qp(to*covariance, -expect_return, G, h, A, b)['x'] for to in tolerance]
	ef_returns = [blas.dot(expect_return,x)*fq_adj for x in ef_frontier]
	ef_risks = [np.sqrt(blas.dot(x,covariance*x)*fq_adj) for x in ef_frontier]
	m1 = np.polyfit(ef_returns, ef_risks, 2)
	x1 = np.sqrt(m1[2] / m1[0])
	ef_weights = []
	for x in ef_frontier: ef_weights.append(list(x))

	return ef_risks, ef_returns, np.asarray(ef_weights)

def sharpe_ratio(returns,rf,fq_adj):
	#Assume:
	#returns: n_observs * n_asset

	n_asset = len(returns.T)
	returns = np.asmatrix(returns.T)

	N = 100
	tolerance = [10**(5 * t/N - 1.0) for t in range(N)]

	covariance = opt.matrix(np.cov(returns))
	expect_return = opt.matrix(np.mean(returns,axis = 1))

	#Constraint Matrices
	G = -opt.matrix(np.eye(n_asset))
	h = opt.matrix(0.0,(n_asset,1))
	A = opt.matrix(1.0,(1,n_asset))
	b = opt.matrix(1.0)

	#Optimization
	ef_frontier = [solvers.qp(to*covariance, -expect_return, G, h, A, b)['x'] for to in tolerance]
	ef_weights = []
	for x in ef_frontier: ef_weights.append(list(x))

	expect_return = np.asmatrix(expect_return).T
	covariance = np.asmatrix(covariance)
	ef_weights = np.asmatrix(ef_weights)
	ratios = []
	for weight in ef_weights:
		sp = (weight*expect_return.T-rf/fq_adj)/np.sqrt(weight*covariance*weight.T)
		ratios.append(float(sp))
	tangency_index, max_sp = max(enumerate(ratios),key = operator.itemgetter(1))
	max_sp = np.sqrt(fq_adj)*max_sp

	return max_sp, ef_weights[tangency_index]
