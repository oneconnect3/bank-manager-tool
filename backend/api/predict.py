# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:40:17 2020

@author: annie
"""
import numpy as np
import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

# bank = '中国银行'
# rate = 5.5
# start_amount = 1000
# term = 2


def gen_sample(bank,rate,start_amount,term,bank_info):
    if rate-0.5>0:
        rates = np.arange(rate-0.5,rate+0.6,0.1)
    else:
        rates = np.arange(0,1.1,0.1)
    if start_amount-5000>0:
        amounts = np.arange(start_amount-5000,start_amount+6000,1000)
    else:
        amounts = np.arange(0,11000,1000)
    if term-5>0:
        terms = np.arange(term-5,term+6,1)
    else:
        terms = np.arange(0,11,1)
    print('rates',rates)
    print('amounts',amounts)
    print('terms',terms)
    
    result = pd.DataFrame({'rate':[rate]*11,'start_amount':[start_amount]*11,'term':[term]*11})
    result['bank'] = bank
    result = pd.merge(result,bank_info,on='bank')
    result['bank']=result['bank_enc']
    result.drop(["bank_enc"],axis=1,inplace=True)
    
    order = ['bank', 'rate', 'start_amount', 'term', 'bank_money','bank_start_year']
    result = result[order]
    
    rate_data = result.copy()
    rate_data['rate'] = rates


    amount_data = result.copy()
    amount_data['start_amount'] = amounts
    
    term_data = result.copy()
    term_data['term'] = terms
    
    return rate_data,amount_data,term_data

def get_series(bank, rate, start_amount, term,bank_info):
    #loading model
    pickle_in = open('../model/linearregression.pickle','rb')
    clf = pickle.load(pickle_in)

    Xs = gen_sample(bank,rate,start_amount,term,bank_info)
    ys = [clf.predict(X) for X in Xs]

    df1 = pd.concat([round(Xs[0]['rate'],2), pd.Series(ys[0])], axis=1)
    df1.columns = ['预计收益率（%）', '售罄时长（月）']
    df1['预计收益率（%）'] = df1['预计收益率（%）'].astype(str)
    df2 = pd.concat([Xs[1]['start_amount'], pd.Series(ys[1])], axis=1)
    df2.columns = ['起投金额（RMB）', '售罄时长（月）']
    df2['起投金额（RMB）'] = df2['起投金额（RMB）'].astype(str)
    df3 = pd.concat([Xs[2]['term'], pd.Series(ys[2])], axis=1)
    df3.columns = ['产品期限（月）', '售罄时长（月）']
    df3['产品期限（月）'] = df3['产品期限（月）'].astype(str)

    origin_x = pd.DataFrame({
            'bank':Xs[0]['bank'][0],
            'rate':[rate],
            'start_amount':[start_amount],
            'term':[term],
            'bank_money':Xs[0]['bank_money'][0],
                  'bank_start_year':Xs[0]['bank_start_year'][0]})
    origin_y = clf.predict(origin_x)

    response = {
    'origin_y': round(origin_y[0], 2),
    'rate_series' : df1.to_dict(orient='records'),
    'start_amount_series' : df2.to_dict(orient='records'),
    'term_series': df3.to_dict(orient='records'),
    'origin_pt': {'rate':rate,'start_amount':start_amount,'term':term}
    }

    return response
    









