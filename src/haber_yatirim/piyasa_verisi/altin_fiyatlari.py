import yfinance as yf
import datetime as dt
print(yf.download("GC=F", end=dt.datetime.now().strftime("%Y-%m-%d")))