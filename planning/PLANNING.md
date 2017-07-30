# Planning & Requirements Gathering
---

## System Objectives

RoboVest (RV) is an intelligent digital investment management platform that provides autonomous & customizable market-driven portfolios based on the risk profile and twitter sentiment of the investor.  RV's intelligent approach assesses the investor's capacity and willingness to take risk through a quick questionnaire and automated Twitter sentiment analysis. RV recommends a unique market driven portfolio consisting of cost-effective ETFs that diversify exposure to multiple asset classes across the world.

Many investors don't retain traditional wealth managers because of high account minimums and management fees. Most investors do not take a DIY approach to investing because of time constraints and investment illiteracy. RV provides a low cost solution with very low account minimums accessible to investors of all income and net worth levels by applying computing power to portfolio management and leveraging financial technology. The platform guides every investor through every step of the investment process in a simplified and streamlined approach. We enable any investor to access markets with any investment amount in one simple way.

## Information Inputs

RV imports historical (up to 15 years) weekly closing and dividend adjusted prices of our ETF investment universe that is databased on a remote server. The prices are then analyzed in a risk/return as inputs into the portfolio recommendation process. The platform also collects answers to our investment questionnaire which in turn become inputs into the portfolio management recommendation process. Lastly, RV collects Twitter feeds of the investor in order to conduct sentiment analysis which becomes an input into the risk tolerance assessment.

## Information Outputs

RV will output a percentage which is a weight of each individual ETF in the customized portfolio that sums to 100%.  We will also output multiple expected risk/return metrics in addition to visual depictions of the weights and performance metrics, ideally on a web-based application.

# Research
---

## Web Services and/or APIs:
* We would require a Twitter REST API https://dev.twitter.com/rest/public
* We would require a Bloomberg Developer API  https://www.bloomberg.com/professional/support/api-library/ or if that becomes difficult we will use Google Finance API (much more limited)

## Third Party Packages

* psycpg2 https://pypi.python.org/pypi/psycopg2
* django  https://djangopackages.org/
* Tweepy  http://www.tweepy.org/
* pandas  http://pandas.pydata.org/
* cvxopt http://cvxopt.org/applications/index.html
* numpy http://www.numpy.org/
* operator
* matplotlib https://pypi.python.org/pypi/matplotlib
* nltk http://www.nltk.org/book/
* tkinter https://docs.python.org/3/library/tkinter.html#module-tkinter
* beautifulsoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Hardware

RV will be a web based application staged on a heroku server.  The database will also be hosted there.
