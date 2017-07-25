#Prototype
This is a very basic prototype that does what a robo advisor essentially does. It can be summarized in 4 high level steps:

1. Risk Tolerance - assess a user's risk tolerance by eliciting repsones from a few qualitative and quantitative questions.

2. Security Selection - define a subset of the investable universe that you want to include in the recommended portfolios.  It is very exhaustive to choose every security possible and that is why you need to curate them and create your own investment galaxy (i.e. subset of universe).  For the purposes of the prototype, I have chosen 17 ETFs that encompass the majority of the investable universe in general, hence the power of ETFs.

2. Database - import daily, weekly, and monthly closing (and adjusted for dividends) prices for
every ETF or security selected going back at least 15 years if possible. Transform the daily prices to continously compouned returns, the weekly and monthly to periodic returns.

3. Analysis - analyze the risk and return characteristics of each security and devise a covariance or correlation matrix.

4. Portfolio Optimization - the risk return characteristics of each selected security become inputs into an optimization process.  In the prototype one can easily use Excel "Solver" to conduct a simple and single period mean variance optimization. Python and R have much more powerful tools.  The optimization process also incorporates the users Risk Tolerance in the ETF selection process and in the cash allocatoin of the portfolio. 

5.  Recommendations - recommend a customized portoflio for each user based on his risk tolerance with some cool visuals.

# Future improvements/Ideas -
Is there a way to incorporate twitter feeds into the risk tolerance section? If a user's twitter feed indicates favorability of a company or sector maybe the security selection part chooses ETFs that are aligned with the user's interests or twitter feed.

Advanced statistical models for risk and return analysis (i.e. forecasting returns, GARCH, DCC, probability scenario optimization, etc. )

Enhance gamification of the user (i.e. make the risk tolerance part more exciting)
