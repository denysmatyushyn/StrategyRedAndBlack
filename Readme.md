**The strategy Red and Black.**

A simple algorithmic strategy has been written in Python to show the dependency between a psychological aspect of a trader and discipline.

The strategy is named Red and Black like a casino. Timeframes are 1-minute candlesticks. 1440 deals per day.

Rules:
It does buy BTCUSDT by market price if the previous close price of a candlestick is less than the current close price of a candlestick and sells if the conditions are reversed.

Result: 
During the two-week non-stop trading profit was about ZERO. (Commission not included)
It shows that even for a beginner trader using simple and high-level rules (who are not deep in trading) it is hard to pour off a deposit. But when a trader starts to use fundamentals, Elliott waves, technical, COT (Commitments of Traders), stock market correlation and etc. analysis, that is to be possible.)))

I have to admit, that is really weird.

To run this:
- `pip3 install -r requirements.txt`

To use it:  
- Example of running `python StrategyRedAndBlack.py`
