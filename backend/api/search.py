import pandas as pd 
from flask_cors import CORS
from flask import Flask, jsonify, request, send_from_directory, render_template
import json

app = Flask(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})   # 允许所有域名跨域

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getProd', methods=['GET', 'POST'])
def home():
    with open('../data/hx_dep_prd.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    
    df = pd.DataFrame(data)

    response_object = {}
    if request.method == 'POST':
        keyword = request.get_json()
        print(keyword)

        bank_name = keyword['bank_name']
        prod_type = keyword['prod_type']
        prod_return = keyword['prod_return']
        duration = keyword['duration']
        prod_name = keyword['prod_name']

        if bank_name == '不限':
            bank_name = ''

        if prod_type == '不限':
            prod_type = ''

        if prod_return == '不限':
            prod_return = ''

        if duration == '不限':
            duration = ''

        prod_rs = df[['产品名称', '发行银行', '投资类型', '委托币种起始金额', '预期收益率(%)','委托管理期(月)', '委托币种']]
        prod_rs['预期收益率(%)'] = prod_rs['预期收益率(%)'].astype(float)
        prod_rs['委托管理期(月)'] = prod_rs['委托管理期(月)'].astype(float)
        prod_rs['委托币种起始金额'] = prod_rs['委托币种起始金额'].astype(float)

        if bank_name != '':
            prod_rs = prod_rs[prod_rs['发行银行'] == bank_name]

        if prod_type != '':
            prod_rs = prod_rs[prod_rs['投资类型'] == prod_type]

        if prod_return != '':
            if prod_return == '1.5%以下':
                prod_rs = prod_rs[prod_rs['预期收益率(%)'] < 1.5]
            elif prod_return == '1.5%~2%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 1.5) & (prod_rs['预期收益率(%)'] < 2)]
            elif prod_return == '2%~2.5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 2) & (prod_rs['预期收益率(%)'] < 2.5)]
            elif prod_return == '2.5%~3%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 2.5) & (prod_rs['预期收益率(%)'] < 3)]
            elif prod_return == '3%~3.5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 3) & (prod_rs['预期收益率(%)'] < 3.5)]
            elif prod_return == '3.5%~4%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 3.5) & (prod_rs['预期收益率(%)'] < 4)]
            elif prod_return == '4%~4.5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 4) & (prod_rs['预期收益率(%)'] < 4.5)]
            elif prod_return == '4.5%~5%':
                prod_rs = prod_rs[(prod_rs['预期收益率(%)'] >= 4.5) & (prod_rs['预期收益率(%)'] < 5)]
            elif prod_return == '5%以上':
                prod_rs = prod_rs[prod_rs['预期收益率(%)'] >= 5]

        if duration != '':
            if duration == '3个月以下':
                prod_rs = prod_rs[prod_rs['委托管理期(月)'] < 3]
            elif duration == '3~6个月':
                prod_rs = prod_rs[(prod_rs['委托管理期(月)'] >= 3) & (prod_rs['委托管理期(月)'] < 6)]
            elif duration == '6~12个月':
                prod_rs = prod_rs[(prod_rs['委托管理期(月)'] >= 6) & (prod_rs['委托管理期(月)'] < 12)]
            elif duration == '12个月以上':
                prod_rs = prod_rs[prod_rs['委托管理期(月)'] >= 12]

        if prod_name != '':
            prod_rs = prod_rs[prod_rs['产品名称'].str.contains(prod_name)]

        prod_rs.columns = ['name', 'bank', 'type', 'amount', 'profit', 'duration', 'currency']

        prod_rs['amount'] = prod_rs['amount'].apply(lambda x: round(x/10000, 2))

        # # 单个产品的详情
        # prod_rs['all_info'] = prod_rs['name'].apply(lambda x: str(df[df['产品名称']==x][['name', 'bank', 'type']].to_dict(orient='records')))
        prod_rs['all_info'] = prod_rs['name'].apply(lambda x: prod_rs[prod_rs['name']==x][['name', 'bank', 'type']].to_dict(orient='records'))
        print(prod_rs['all_info'])
        prod_json = prod_rs.to_dict(orient='records')

        print(prod_json)

        prod_cnt = prod_rs.shape[0]
       
        response_object = {
            'prod_data': prod_json,
            'prod_cnt': prod_cnt
        }

    else:
        response_object = "出错啦"
        
    return jsonify(response_object)

# @app.route('/getProd', methods=['GET', 'POST'])
# def home():
#     response_object = {}
#     if request.method == 'POST':
#         keyword = request.get_json()['prod_name']
#         print(keyword)
#         df = pd.read_csv('../data/animal-crossing-fish-info.csv')
#         df['price'] = df['price'].astype(str)
#         price = df[df['name'] == keyword]['price'].iloc[0]
#         image = df[df['name'] == keyword]['image'].iloc[0].split('\t')[0] + '>'
#         fish_info = {'price': str(price), 'image': image}
#         response_object = {
#             'msg': fish_info
#         }
#     else:
#         response_object = "出错啦"
        
#     return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True) 