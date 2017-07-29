import numpy as np
import Markowitz_Frontier as mf
import cvxopt as opt
from cvxopt import blas, solvers
import operator

solvers.options['show_progress'] = False

def bl_expect_return(market_cap,returns,rf,fq_adj):
    bench_weight = np.matrix(market_cap)/sum(market_cap)

    returns = returns.T
    mean_return = np.matrix(np.mean(returns,axis = 1)) #here we get a row vector
    bench_return = float(bench_weight * mean_return.T)

    n_asset = len(mean_return.T)
    I = np.matrix(np.ones(n_asset))

    covariance = np.matrix(np.cov(returns))

    bl_expect_return = covariance * bench_weight.T * (bench_return - rf/fq_adj)/float(bench_weight*covariance*bench_weight.T) + rf/fq_adj*I.T
#    bl_expect_return = bl_expect_return.T

    return bl_expect_return

def bl_possible_portfolios(bl_expect_return,returns,n_port,fq_adj):
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
	expect_return = bl_expect_return #here we get a row vector
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

def	bl_efficient_frontier(bl_expect_return,returns,tolerance,fq_adj):
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
	expect_return = opt.matrix(bl_expect_return)

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

def sharpe_ratio(bl_expect_return,returns,rf,fq_adj):
	#Assume:
	#returns: n_observs * n_asset

	n_asset = len(returns.T)
	returns = np.asmatrix(returns.T)

	N = 100
	tolerance = [10**(5 * t/N - 1.0) for t in range(N)]

	covariance = opt.matrix(np.cov(returns))
	expect_return = opt.matrix(bl_expect_return)

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
