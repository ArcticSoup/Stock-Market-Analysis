import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as data
import pandas as pd
from iexfinance.stocks import get_historical_data
from datetime import datetime
'''def getdata():
    start_date='2014-01-01'
    end_date='2018-01-01'
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = ['TSLA','AAPL','AAL']
    data = get_historical_data(df, start=start_date, end=end_date, output_format='pandas')
    # Drop date variable
    data = data.drop(['date'], 1)
    return data
print(getdata())  '''
start_date='2014-01-01'
end_date='2018-01-01'
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

df = ['TSLA','AAPL','AAL']

data = get_historical_data(df, start=start_date, end=end_date, output_format='pandas')
print(data.head())
print(data.shape)
print(data.columns)
#data.plot()
#plt.show()
'''#Tckers
tickers = ['AAPL', 'MSFT', '^GSPC']

#Dates
start = '2010-01-01'
end = '2011-01-01'

#Load data
panel_data = data.DataReader('INPX', 'morningstar', start, end)

print(panel_data.to_frame().head(9))'''