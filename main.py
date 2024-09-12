### INF601 - Advanced Programming in Python
### Cooper Weinhold
### Miniproject 1
import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
from matplotlib import pyplot as plt
import copy


#Get todays time
today = datetime.now()

#Calculates 10 days ago
ten_days_ago = today - timedelta(days=15)

myticker = ["MSFT", "AAPL", "NVDA", "GME", "LMT"]

mydata = {}

myticker.sort()
for ticker in myticker:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        maxlist = copy.copy(last10days)
        maxlist.sort()
        max_price = maxlist[-1]+10
        min_price = maxlist[-1]-10
        myarray = np.array(last10days)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f'{ticker} Last 10 Closing Prices')
        plt.show()
        #plt.savefig(f'charts/{ticker}.png')

else:
    print(f'Do not have ')


#aapl = yf.Ticker("AAPL")

# get all stock info
#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="1mo")

#pprint.pprint(hist)