#Python

import pandas as pd
import numpy as np
from fbprophet import Prophet
import csv
import time
#import matplotlib.pyplot as plt


df = pd.read_csv('HuntingtonSouth.csv')
m = Prophet(changepoint_prior_scale=0.01).fit(df)
future = m.make_future_dataframe(periods=8000, freq='H')
forecast = m.predict(future)
timestamp = forecast[['ds']].tail(n=720)
tempFuture = forecast[['yhat']].tail(n=720)
	

forecast.to_csv('PredictOutput.csv')


#m.plot(forecast);
#plt.show()


