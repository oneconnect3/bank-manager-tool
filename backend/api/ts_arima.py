#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16 15:38:14 2020

@author: Tianyu
"""

import pandas as pd
import numpy as np
import math
import sklearn
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

def predict(coef, history):
	yhat = 0.0
	for i in range(1, len(coef)+1):
		yhat += coef[i-1] * history[-i]
	return yhat

def difference(dataset):
	diff = list()
	for i in range(1, len(dataset)):
		value = dataset[i] - dataset[i - 1]
		diff.append(value)
	return np.array(diff)

def arima_pred():
    X = series.values
    size = len(X) - 7
    train, test = X[0:size], X[size:]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(5,1,1))
        model_fit = model.fit(trend='nc', disp=False)
        ar_coef, ma_coef = model_fit.arparams, model_fit.maparams
        resid = model_fit.resid
        diff = difference(history)
        yhat = history[-1] + predict(ar_coef, diff) + predict(ma_coef, resid)
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('>predicted=%.3f, expected=%.3f' % (yhat, obs))
    # rmse = math.sqrt(sklearn.metrics.mean_squared_error(test, predictions))
    # print('Test RMSE: %.3f' % rmse)