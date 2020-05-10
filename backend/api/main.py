import pandas as pd 
from flask_cors import CORS
from flask import Flask, jsonify, request, send_from_directory, render_template

app = Flask(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})   # 允许所有域名跨域

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getProd', methods=['GET', 'POST'])
def home():
    response_object = {}
    if request.method == 'POST':
        keyword = request.get_json()['key']
        print(keyword)
        df = pd.read_csv('../data/animal-crossing-fish-info.csv')
        df['price'] = df['price'].astype(str)
        price = df[df['name'] == keyword]['price'].iloc[0]
        image = df[df['name'] == keyword]['image'].iloc[0].split('\t')[0] + '>'
        fish_info = {'price': str(price), 'image': image}
        response_object = {
            'msg': fish_info
        }
    else:
        response_object = "出错啦"
        
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True) 