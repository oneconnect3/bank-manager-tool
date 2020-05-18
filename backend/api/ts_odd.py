#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 14 18:45:15 2020

@author: Tianyu
"""

import pandas as pd
import numpy as np
from fbprophet import Prophet

# 备用异常检测方案

def ts_prediction(df, pred_dura):
    
    df.columns = ['ds', 'y']
    
    m = Prophet()
    m.fit(df)

    future = m.make_future_dataframe(periods=pred_dura)
    forecast = m.predict(future)

    fb_x = forecast['ds']
    fb_y = forecast['yhat']
    
    pred_rs = pd.DataFrame()
    pred_rs['date'] = fb_x
    pred_rs['value'] = fb_y

    return pred_rs


def generate_expanding_mad_envelope(df, z, value_col):
    
    mad = lambda x: np.median(np.fabs(x - np.median(x))) #计算绝对中位差(MAD)
    df = df.copy()
    exp = df[value_col].expanding()
    mu = exp.median()
    sigma = exp.apply(mad, raw=False)
    
    df['median'] = mu
    df['hi'] = mu + z * sigma
    df['low'] = mu - z * sigma
    
    return df


def func(hi, low, value): 
    
    if (low <= value <= hi): 
        return 'False'
    
    else: 
        return 'True' 


def detect_anomaly(df):
    
    df_exp_mad = generate_expanding_mad_envelope(df, 3, 'value')
    df_exp_mad['outlier'] = df_exp_mad.apply(lambda x: func(x.hi, x.low, x.value), axis=1)
    
    return df_exp_mad



if __name__ == "__main__":
    
    try:
        
        pred_time = 7
        
        df = pd.read_csv("/Users/Cyan/Documents/OneConnect/ts_test_data.csv")
        pred_rs = ts_prediction(df, pred_time)
        
        detect_rs = detect_anomaly(pred_rs).tail(pred_time)
        detect_rs = detect_rs[['date', 'value', 'outlier']]
        
        detect_rs.to_csv('./result.csv', index=False)


    except Exception as e:
        
        print('检测异常')
        print(e)

