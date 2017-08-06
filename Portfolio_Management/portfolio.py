import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from IPython import embed
import psycopg2
import pandas
from pandas_datareader import data
from datetime import date, timedelta
from numpy.linalg import inv

def portfolio():
    #This is for server DATABASE
    Server_DB_Username = 'vnqyscaajfifeg'
    Server_DB_Host = "ec2-54-163-254-143.compute-1.amazonaws.com"
    Server_DB_Password = "6ee97dda964f794ee664a52ab7cd6ed367d8480ba496ebcc0647b3226c16a370"
    Server_Port = "5432"
    Server_DB_Name = "d7t1alfnvnuu63"

    # OPEN DATABASE CONNECTION
    conn = psycopg2.connect(
        dbname=Server_DB_Name,
        user=Server_DB_Username,
        password=Server_DB_Password,
        host=Server_DB_Host,
        port=Server_Port
        )

    years = 15
    week = 52
    Horizon =years*week

    # PERFORM A DATABASE OPERATION
    ETF_Tickers=[]
    ETF_MktCap=[]
    ETF = []
    #ETFs=["id","Date","MINT","EMB","IAU","VCIT","MUB","SCHA","VEA","VYM","SCHH","SCHM","SCHX","VWO","VWO","FENY","VNQI","VTIP","VGLT","ITE"]
    with conn:
        with conn.cursor() as cursor:
            sql_query ="SELECT * From etf;"
            cursor.execute(sql_query)


            for row in cursor.fetchall():
                ETF_Tickers.append(row[0])
                ETF_MktCap.append(row[8])

    for id, txt in enumerate(ETF_Tickers):
        ETF.append({"name": txt, "mkt_cap":ETF_MktCap[id]})

    # # CLOSE DATABASE CONNECTION
    # #conn.close()
    #
    ##Import Prices
    symbols=ETF_Tickers
    data_source = 'google'
    start = str(date.today() - timedelta(days=Horizon)) #> '2017-07-09'
    end = str(date.today())
    response = data.DataReader(symbols, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    #daily_closing_prices = daily_closing_prices[list(daily_closing_prices.columns[:8])]
    tickers = ["MINT","EMB","IAU","VCIT","MUB","SCHA","VEA","VYM","SCHH","VWO","FENY","VTIP","VGLT","ITE"]
    daily_closing_prices = daily_closing_prices[tickers]
    daily_closing_prices.to_csv("portfolio.csv", sep=',')


    # Mean_Variance Theory

    def bl_expect_return(market_cap,returns,rf,fq_adj):
        bench_weight = np.matrix(market_cap)/sum(market_cap)

        returns = returns.T
        mean_return = np.matrix(np.mean(returns,axis = 1)) #here we get a row vector
        mean_return = mean_return.T
        bench_return = float(bench_weight * mean_return.T)

        n_asset = len(mean_return.T)
        I = np.matrix(np.ones(n_asset))

        covariance = np.matrix(np.cov(returns))

        bl_expect_return = covariance * bench_weight.T * (bench_return - rf/fq_adj)/float(bench_weight*covariance*bench_weight.T) + rf/fq_adj*I.T

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
        expect_return = bl_expect_return.T #here we get a column vector
        covariance = np.cov(returns)
        port_returns = []
        port_risks = []
        for row in weights:
            returns = float(row * expect_return.T)
            risks = float(np.sqrt(row * covariance * row.T))
            while(risks > 0.01):
                w = np.random.randn(n_asset)
                w = np.asmatrix(w/sum(w))
                returns = float(w * expect_return.T)
                risks = float(np.sqrt(w * covariance * w.T))
            port_returns.append(np.array(returns*fq_adj))
            port_risks.append(np.array(risks*np.sqrt(fq_adj)))
        return port_risks, port_returns

    def	bl_efficient_frontier(bl_expect_return,returns,fq_adj):
        n_asset = len(returns.T)
        returns = np.asmatrix(returns.T)
        #Assume
        #returns of each asset is a column vector
        #rq_returns only contains the smallest and biggest ones

        #this parameter should be adjusted according to characteristics of different database
        #parameter = 1.8
        #N = 100
        #tolerance = [10**(5 * t/N - 1.0) for t in range(N)]

        covariance = np.matrix(np.cov(returns))
        expect_return = np.matrix(bl_expect_return)

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

    #Here assume using simplest return
    def mf_get_return(prices,return_type):
        prices = np.array(prices)
        if return_type == "log": stock_return = np.log(prices[1:]/prices[:-1])
        else: stock_return = prices[1:]/prices[:-1]-1
        return stock_return


    def find_mkt(etf_nm,ETF):
        for etf in ETF:
            if etf["name"] == etf_nm: mkt = etf["mkt_cap"]
        return mkt

    def del_nan(port_price):
        port_price = np.asarray(port_price.T)
        for row in port_price:
            for id, value in enumerate(row):
                if np.isnan(value)==True: row[id] = (row[id-1]+row[id+1])/2
        return np.asmatrix(port_price).T

    def filter_ef(ef_risks,ef_returns,ef_weights):
        r = []
        s = []
        w = []
        for id,value in enumerate(ef_returns):
            if value > 0:
                r.append(ef_returns[id])
                s.append(ef_risks[id])
                if len(ef_weights) > 0: w.append(ef_weights[id])

        ef_risks = s
        ef_returns = r
        ef_weights = w

        return ef_risks, ef_returns, ef_weights

    rf = 0.02 #annualized risk-free rate
    fq_adj = 252 #weekly data. for daily data, set fq_adj = 252.

    score = 7
    #score = risk_tolerance(age_adj, income_adj, invest_adj, q1, q2, q3)

    market_cap = []
    for i in tickers: market_cap.append(find_mkt(i,ETF))

    port_price = daily_closing_prices
    #port_price = mf_read_prices("portfolio.csv")
    port_price = del_nan(port_price)

    returns = mf_get_return(port_price,return_type = "percentage") #or choose "log" as return_type
    returns = np.asmatrix(returns)

    bl_expect_return = bl_expect_return(market_cap,returns,rf,fq_adj)
    bl_port_risks, bl_port_returns = bl_possible_portfolios(bl_expect_return,returns,1000,fq_adj)
    bl_ef_risks, bl_ef_returns, bl_ef_weights = bl_efficient_frontier(bl_expect_return,returns,fq_adj)

    bl_ef_risks, bl_ef_returns, bl_ef_weights = filter_ef(bl_ef_risks,bl_ef_returns,bl_ef_weights)
    bl_port_risks, bl_port_returns, []= filter_ef(bl_port_risks, bl_port_returns, [])


    # Outputs

    position1 = int((score-2.5)/(11-2.5)*len(bl_ef_weights))

    weights_bl = round(bl_ef_weights[position1]*100,1)
    return_bl =round(bl_ef_returns[position1]*100,2)
    risk_bl = round(bl_ef_risks[position1],2)

    plt.plot(bl_port_risks,bl_port_returns, 'ro')
    line1, = plt.plot(bl_ef_risks,bl_ef_returns,'b-',label='Market Implied Assumption')
    plt.plot(bl_ef_risks[position1],bl_ef_returns[position1],'bo')
    first_legend = plt.legend(handles=[line1], loc=1)
    ax = plt.gca().add_artist(first_legend)
    plt.title('Efficient Frontier')
    plt.ylabel('Annualized Expected Return')
    plt.xlabel('Standard Deviation as Risk')
    pylab.savefig('/Users/cynthia/Desktop/efficient_frontier.png')
    plt.close()


    y_pos = np.arange(len(tickers))
    plt.bar(y_pos, weights_bl, align='center', alpha=0.5)
    plt.xticks(y_pos, tickers, fontsize = 5)
    plt.ylabel('Percentage')
    plt.title('Portfolio Weights')
    pylab.savefig('/Users/cynthia/Desktop/weights.png')
    plt.close()
    
    return weights_bl, return_bl, risk_bl

if __name__ == "__main__":
    portfolio()
