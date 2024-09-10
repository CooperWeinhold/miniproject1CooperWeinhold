### INF601 - Advanced Programming in Python
### Cooper Weinhold
### Miniproject 1
import pprint
import yfinance as yf
myticker = ["MSFT", "AAPL", "NVDA", "GME", "LMT"]

mydata = {}

myticker.sort()
for ticker in myticker:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dayHigh': result.info['dayHigh']}

pprint.pprint(mydata)

#aapl = yf.Ticker("AAPL")

# get all stock info
#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="1mo")

#pprint.pprint(hist)