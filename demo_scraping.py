from pandas.io.data import DataReader
from datetime import datetime

goog = DataReader("GOOG",  "yahoo", "IBM", "MSFT" datetime(2000,1,1), datetime(2015,1,1))
print goog["Adj Close"]
