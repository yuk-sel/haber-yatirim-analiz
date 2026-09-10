import yfinance as yf
import datetime as dt

bugun= dt.datetime.now().strftime("%Y-%m-%d")

print(yf.download("XU100.IS", end=bugun))
