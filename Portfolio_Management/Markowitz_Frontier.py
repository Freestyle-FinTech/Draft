import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import csv
import operator
import pandas as pd
from numpy.linalg import inv

solvers.options['show_progress'] = False

#Read prices
def read_prices(file_path):
	port_price = pd.read_csv(file_path)
	del port_price["Date"]
#	port_price = list(csv.reader(open(file_path)))
#	port_price = np.delete(np.asmatrix(port_price),(0),axis=1)
#	port_price = np.delete(np.asmatrix(port_price),(0),axis=0)
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
		w = np.random.randn(n_asset)*2
		weights.append(w/sum(w))
	weights = np.matrix(weights)

	#calculate the random returns and risks
	#assume: returns for each asset is a column vector
	returns = returns.T
	expect_return = np.matrix(np.mean(returns,axis = 1)) #here we get a row vector
	expect_return = expect_return.T
	covariance = np.cov(returns)
	port_returns = []
	port_risks = []
	for row in weights:
		returns = float(row * expect_return.T)
		risks = float(np.sqrt(row * covariance * row.T))
		while(risks > 0.003):
			w = np.random.randn(n_asset)
			w = np.asmatrix(w/sum(w))
			returns = float(w * expect_return.T)
			risks = float(np.sqrt(w * covariance * w.T))
		port_returns.append(np.array(returns*fq_adj))
		port_risks.append(np.array(risks*np.sqrt(fq_adj)))
	return port_risks, port_returns

def	efficient_frontier(returns,fq_adj):
	n_asset = len(returns.T)
	returns = np.asmatrix(returns.T)
	#Assume
	#returns of each asset is a column vector
	#rq_returns only contains the smallest and biggest ones

	covariance = np.matrix(np.cov(returns))
	expect_return = np.matrix(np.mean(returns,axis = 1))
	I = np.ones((n_asset,1))

	A = float(I.T * inv(covariance) * I)
	B = float(expect_return.T * inv(covariance) * I)
	C = float(expect_return.T * inv(covariance) * expect_return)
	D = A*C - B**2

	a = float(min(expect_return))
	b = float(max(expect_return))
	ef_returns = []
	for t in range(100): ef_returns.append(a+(b-a)*t/100)
	ef_weights = []
	ef_risks = []
	for id, r in enumerate(ef_returns):
		w = (C-B*r)/D*inv(covariance)*I + (A*r-B)/D*inv(covariance)*expect_return
		ef_weights.append((w.T).tolist()[0])
		sigma = (A*r**2 - 2*B*r + C)/D*fq_adj
		ef_risks.append(np.sqrt(sigma))
		ef_returns[id] = r*fq_adj

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
	#G = -opt.matrix(np.eye(n_asset))
	#h = opt.matrix(0.0,(n_asset,1))
	G = opt.matrix(np.eye(n_asset))
	h = opt.matrix(1.0,(n_asset,1))
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
