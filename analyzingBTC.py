import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as npf
import yfinance as yf

#price for 2018-2021
#bitcoin = [3869.47, 7188.46, 22203.31, 29391.78]

BTC = yf.Ticker('BTC-USD')
x = BTC.history('1y')['Close']
cost = x[0]
NumBitcoin = x/cost
investment = 1000
ret = np.multiply(NumBitcoin, investment)

#year = list(range(2018, 2022))
#irrlist = [i*10 for i in bitcoin]
#irrlist.insert(0,-500000)

annual_std = np.std(ret) * np.sqrt(252)
sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)
print('Risk: ' + str(annual_std))
print('Sharpe: ' + str(sharpe))

#print(npf.irr(irrlist))

NumBitcoin.plot()

#plt.xticks(ticks = year)

plt.savefig('Investment.png')
