import Markowitz_Frontier as mf
import csv
import numpy as np
import matplotlib.pyplot as plt
import Black_Litterman as bl

# Mean_Variance Theory
## Initialize some parameters
rf = 0.02 #annualized risk-free rate
fq_adj = 52 #weekly data. for daily data, set fq_adj = 252.
risk_aversion = 10
market_cap = [40,66,25,79,0.04,79]

port_price = mf.read_prices("ASSET1.csv")
returns = mf.get_return(port_price,return_type = "percentage") #or choose "log" as return_type

port_risks, port_returns = mf.possible_portfolios(returns,1000,fq_adj)
ef_risks, ef_returns, ef_weights = mf.efficient_frontier(returns,risk_aversion,fq_adj)
max_sp, tangency_weight = mf.sharpe_ratio(returns,rf,fq_adj)

bl_expect_return = bl.bl_expect_return(market_cap,returns,rf,fq_adj)
print(bl_expect_return)
bl_ef_risks, bl_ef_returns, bl_ef_weights = bl.bl_efficient_frontier(bl_expect_return,returns,risk_aversion,fq_adj)
bl_max_sp, bl_tangency_weight = bl.sharpe_ratio(bl_expect_return,returns,rf,fq_adj)

# Outputs

print("Recommendations\n----------------------------------\nBlack-Litterman Adjusted Portfolio (Expect from Market)\n")
print("Weights: ")
bl_ef_weights = bl_ef_weights.tolist()[0]
for i in range(len(bl_ef_weights)):
    print("  +  Asset",i+1,": {}%".format(round(bl_ef_weights[i]*100,2)))
print("Expected Return: {}%".format(round(bl_ef_returns[0]*100,2)))
print("Expected Risk: ",round(bl_ef_risks[0],2))
## Tangency Portfolio Sharpe Ratio
print("Expected Sharpe Ratio: ",round(bl_max_sp,4))

print("\n----------------------------------\nMean-Variance Portfolio (Expect from History)\n")
## Tangency Portfolio Weights
print("Weights: ")
ef_weights = ef_weights.tolist()[0]
for i in range(len(ef_weights)):
    print("  +  Asset",i+1,": {}%".format(round(ef_weights[i]*100,2)))
#print(ef_weights)
print("Expected Return: {}%".format(round(ef_returns[0]*100,2)))
print("Expected Risk: ",round(ef_risks[0],2))
## Tangency Portfolio Sharpe Ratio
print("Mean-Variance Portfolio Expected Sharpe Ratio: ",round(max_sp,4))
## possible portfolios: risks and returns
plt.plot(port_risks, port_returns, 'ro')
## efficient frontier: risks and returns
plt.plot(ef_risks,ef_returns,'b-o')
#plt.plot([0,ef_risks[tangency_index]],[rf,ef_returns[tangency_index]],'y--o')
plt.title('Mean-Variance Portfolio')
plt.ylabel('Annualized Expected Return')
plt.xlabel('Standard Deviation as Risk')
plt.show()
plt.close()
