#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 4 10:11:43 2020

@author: Tianyu
"""

import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify, request, send_from_directory, render_template
import json
import pickle
from insights import gene_insights
from predict import get_series
from ts_fbprophet import ts_prediction

app = Flask(__name__)

# 允许跨域
CORS(app, resources={r"/*": {"origins": "*"}})   


@app.route('/')
def hello_world():
    return 'Hello World!'

# 查一查接口
@app.route('/getProd', methods=['GET', 'POST'])
def search():
    with open('../data/hx_dep_prd3.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    df = pd.DataFrame(data)

    response_object = {}
    if request.method == 'POST':
        keyword = request.get_json()
        # print(keyword)

        bank_name = keyword['bank_name']
        prod_type = keyword['prod_type']
        prod_return = keyword['prod_return']
        duration = keyword['duration']
        prod_name = keyword['prod_name']

        if ((bank_name == '') & (prod_type == '') & (prod_return == '') & (duration == '') & (prod_name == '')):
            df = df.sample(20)

        if bank_name == '不限':
            bank_name = ''

        if prod_type == '不限':
            prod_type = ''

        if prod_return == '不限':
            prod_return = ''

        if duration == '不限':
            duration = ''

        # prod_rs = df[['产品名称', '发行银行', '投资类型',
        #               '委托币种起始金额', '预期收益率(%)', '委托管理期(月)', '委托币种', '是否保本',
        #               '发行起始日期', '发行终止日期', '可否质押', '图片地址', '客户是否有权提前赎回',
        #               '银行是否有权提前终止', '适用地区', '产品管理费', '付息周期(月)', '申购赎回规定',
        #               '投资对象', '投资风险说明']]
        prod_rs = df[['产品名称', '发行银行', '投资类型',
                      '委托币种起始金额', '预期收益率(%)', '委托管理期(月)', '委托币种', '是否保本',
                      '发行起始日期', '发行终止日期', '可否质押', '图片地址', '客户是否有权提前赎回',
                      '银行是否有权提前终止', '适用地区', '产品管理费', '付息周期(月)']]
        prod_rs['预期收益率(%)'] = prod_rs['预期收益率(%)'].astype(float)
        prod_rs['委托管理期(月)'] = prod_rs['委托管理期(月)'].astype(float)
        prod_rs['委托币种起始金额'] = prod_rs['委托币种起始金额'].astype(float)

        if bank_name != '':
            prod_rs = prod_rs[prod_rs['发行银行'] == bank_name]

        if prod_type != '':
            prod_rs = prod_rs[prod_rs['投资类型'] == prod_type]

        if prod_return != '':
            if prod_return == '1.5%以下':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] < 1.5)
                                  & (prod_rs['预期收益率(%)'] != 0)]
            elif prod_return == '1.5%~2%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 1.5)
                                  & (prod_rs['预期收益率(%)'] < 2)]
            elif prod_return == '2%~2.5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 2)
                                  & (prod_rs['预期收益率(%)'] < 2.5)]
            elif prod_return == '2.5%~3%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 2.5)
                                  & (prod_rs['预期收益率(%)'] < 3)]
            elif prod_return == '3%~3.5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 3)
                                  & (prod_rs['预期收益率(%)'] < 3.5)]
            elif prod_return == '3.5%~4%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 3.5)
                                  & (prod_rs['预期收益率(%)'] < 4)]
            elif prod_return == '4%~4.5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 4)
                                  & (prod_rs['预期收益率(%)'] < 4.5)]
            elif prod_return == '4.5%~5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 4.5)
                                  & (prod_rs['预期收益率(%)'] < 5)]
            elif prod_return == '5%以上':
                prod_rs = prod_rs[prod_rs['预期收益率(%)'] >= 5]

        if duration != '':
            if duration == '3个月以下':
                prod_rs = prod_rs[(prod_rs['委托管理期(月)'] < 3)
                                  & (prod_rs['委托管理期(月)'] != 0)]
            elif duration == '3~6个月':
                prod_rs = prod_rs[(prod_rs['委托管理期(月)'] >= 3)
                                  & (prod_rs['委托管理期(月)'] < 6)]
            elif duration == '6~12个月':
                prod_rs = prod_rs[(prod_rs['委托管理期(月)'] >= 6)
                                  & (prod_rs['委托管理期(月)'] < 12)]
            elif duration == '12个月以上':
                prod_rs = prod_rs[prod_rs['委托管理期(月)'] >= 12]

        if prod_name != '':
            prod_rs = prod_rs[prod_rs['产品名称'].str.contains(prod_name)]

        # prod_rs.columns = ['name', 'bank', 'type',
        #                    'amount', 'profit', 'duration', 'currency', 'if_safe',
        #                    'start_date', 'end_date', 'if_impawn', 'img_url',
        #                    'if_redeem', 'if_end', 'area', 'fee', 'cycle', 're_rule',
        #                    'target', 'risk']

        prod_rs.columns = ['name', 'bank', 'type',
                           'amount', 'profit', 'duration', 'currency', 'if_safe',
                           'start_date', 'end_date', 'if_impawn', 'img_url',
                           'if_redeem', 'if_end', 'area', 'fee', 'cycle']

        prod_rs['amount'] = prod_rs['amount'].apply(
            lambda x: round(x/10000, 2))

        prod_rs = prod_rs.replace(to_replace=0, value="未知")
        prod_rs = prod_rs.replace(to_replace="0", value="未知")

        # 若字段内容过长，则只保留前100个字
        # prod_rs['re_rule'] = prod_rs['re_rule'].astype(str).str[100]

        # 单个产品的详情
        # prod_rs['all_info'] = prod_rs['name'].apply(lambda x: prod_rs[prod_rs['name'] == x][[
        #                                             'name', 'bank', 'type', 'currency', 'if_safe',
        #                                             'start_date', 'end_date', 'if_impawn', 'img_url',
        #                                             'if_redeem', 'if_end', 'area', 'fee', 'cycle',
        #                                             're_rule', 'target', 'risk']].to_dict(orient='records'))

        prod_rs['all_info'] = prod_rs['name'].apply(lambda x: prod_rs[prod_rs['name'] == x][[
                                                    'name', 'bank', 'type', 'currency', 'if_safe',
                                                    'start_date', 'end_date', 'if_impawn', 'img_url',
                                                    'if_redeem', 'if_end', 'area', 'fee', 'cycle']].to_dict(orient='records'))

        prod_json = prod_rs.to_dict(orient='records')

        prod_cnt = prod_rs.shape[0]

        response_object = {
            'prod_data': prod_json,
            'prod_cnt': prod_cnt
        }

    else:
        response_object = "出错啦"

    return jsonify(response_object)

# 比一比接口
@app.route('/getCmp', methods=['GET', 'POST'])
def comparison():
    prod_struct_data = pd.read_csv(
        '../data/prod_struct_data.csv', encoding='gbk')
    interest_rate_data = pd.read_csv(
        '../data/interest_rate_data.csv', encoding='gbk')
    prod_contract_data = pd.read_csv(
        '../data/prod_contract_data.csv', encoding='gbk')

    bank_list = ['招商银行', '光大银行', '兴业银行', '平安银行', '浙商银行',
                 '民生银行', '浦发银行', '中信银行', '广发银行', '华夏银行']

    prod_list = ['结构性存款', '大额存单', '定期存款', '外币理财', '活期理财', '贵金属理财', '权益类理财']

    for bank in bank_list:
        interest_rate_data[bank] = interest_rate_data[bank].apply(
            lambda x: x*100)
        prod_contract_data[bank] = prod_contract_data[bank].apply(
            lambda x: x*100)

    for col in prod_list:
        prod_struct_data[col] = prod_struct_data[col].apply(lambda x: x*100)

    response_object = {}
    if request.method == 'POST':
        bank_names = request.get_json()

        bank1 = bank_names['bank1']
        bank2 = bank_names['bank2']

        if bank1 == '':
            bank1 = '平安银行'

        if bank2 == '':
            bank2 = '招商银行'

        bank_names = [bank1, bank2]

        # 产品类别分析
        bank_struct_dim = '类别'
        bank_struct_columns = ['类别', '结构性存款', '大额存单',
                               '定期存款', '外币理财', '活期理财', '贵金属理财', '权益类理财']

        bank_data1 = prod_struct_data[prod_struct_data['类别'] == bank1]
        bank_data2 = prod_struct_data[prod_struct_data['类别'] == bank2]
        bank_data12 = pd.concat([bank_data1, bank_data2], axis=0)
        bank_struct_data = bank_data12.to_dict(orient='records')

        # 产品利率分析
        interest_rate_dim = '类别'
        interest_rate_columns = [interest_rate_dim, bank1, bank2]

        bank_interest_data = interest_rate_data[interest_rate_columns]
        bank_interest_data = bank_interest_data.to_dict(orient='records')

        # 产品期限分析
        prod_contract_dim = '类别'
        prod_contract_columns = [prod_contract_dim, bank1, bank2]

        bank_contract_data = prod_contract_data[prod_contract_columns]
        bank_contract_data = bank_contract_data.to_dict(orient='records')

        stack_dict = {'类别': prod_list}

        # 生成insights
        insights = gene_insights(bank1, bank2)
        print(insights)

        response_object = {
            'bank_names': bank_names,
            'struct_dim': bank_struct_dim,
            'struct_columns': bank_struct_columns,
            'struct_data': bank_struct_data,
            'interest_columns': interest_rate_columns,
            'interest_data': bank_interest_data,
            'contract_columns': prod_contract_columns,
            'contract_data': bank_contract_data,
            'stack_dict': stack_dict,
            'insights': insights
        }

        # print(response_object['stack_dict'])
        # print(response_object['struct_columns'])
        # print(response_object['struct_data'])

    else:
        response_object = '出错啦'

    return jsonify(response_object)

# 销量预测接口
@app.route('/getTS', methods=['GET', 'POST'])
def ts_predict():

    response_object = {}
    if request.method == 'POST':
        args = request.get_json()
        print(args)

        arg1 = args['pred_prod']
        arg2 = args['pred_days']

        if arg1 == '':
            arg1 = '产品1'

        series = pd.read_csv('../data/sales_data.csv', encoding='gbk')
        fb_train = series[['ds', arg1]]
        fb_train.columns = ['ds', 'y']

        pred_rs = ts_prediction(fb_train, arg2)

        # print(origin_ts)
        # print("============")
        # print(pred_rs)

        response_object = {
            "result": pred_rs
        }

    else:
        response_object = '出错啦'

    # print(response_object)

    return jsonify(response_object)

# 销售时长预测接口
@app.route('/getPred', methods=['GET', 'POST'])
def prod_predict():

    bank_info = pd.read_csv('../data/bank_info.csv')

    response_object = {}
    if request.method == 'POST':
        args = request.get_json()

        arg1 = args['arg1']
        arg2 = int(args['arg2'])
        arg3 = int(args['arg3'])
        arg4 = int(args['arg4'])

        if arg1 == '':
            arg1 = '平安银行'

        result = get_series(arg1, arg2, arg3, arg4, bank_info)
        print(result)

        response_object = {
            "result": result
        }

        print(response_object)

    else:
        response_object = '出错啦'

    # print(response_object)

    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)
