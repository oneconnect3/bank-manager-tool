#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 16 13:53:10 2020

@author: Tianyu
"""
import pandas as pd
from fbprophet import Prophet

'''
根据所设置时长进行时间序列预测
输入：时序数据集、所需预测时长
输出：预测时间列、预测值列、置信上限、置信下限
'''

def ts_prediction(fb_train, pred_dura):
    
    m = Prophet(daily_seasonality=True)
    m.fit(fb_train)

    future = m.make_future_dataframe(periods=pred_dura)
    forecast = m.predict(future)
    pred_rs = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(pred_dura)
    pred_rs['ds'] = pred_rs['ds'].astype(str)
    pred_rs.columns=['时间', '预测值', '置信下限', '置信上限']

    yhat = forecast['yhat']
    yhat = list(yhat)
    growth_rate = round(((yhat[-1] - yhat[-pred_dura]) / yhat[-pred_dura]), 4)

    ds = forecast['ds']
    yhat = forecast['yhat']
    yhat_upper = forecast['yhat_upper']
    yhat_lower = forecast['yhat_lower']

    return pred_rs.to_dict(orient='records')


# # 时序预测NLG
# def forecast_nlg(fb_train, pred_dura):
#     summary_df = pd.DataFrame(index=['NLG描述'], columns=['外层描述', '内层描述', '算法描述'])
#     growth_rate, pred_rs = ts_prediction(fb_train, pred_dura)

#     if (growth_rate < 0):
#         in_summary = '总体呈现下降趋势'

#     elif (growth_rate == 0):
#         in_summary = '总体趋于平稳'

#     elif (growth_rate > 0):
#         in_summary = '总体呈现上升趋势'

#     outer_summary = '未来' + str(pred_dura) + '天' + in_summary + '。'
#     inner_summary = '基于历史数据进行预测，未来' + str(pred_dura) + '天' + in_summary + '将环比增长' + str(growth_rate * 100) + '%。'
#     algo_summary = 'fbprophet 预测算法。'

#     summary_df['外层描述'] = outer_summary
#     summary_df['内层描述'] = inner_summary
#     summary_df['算法描述'] = algo_summary

#     return summary_df, pred_rs
