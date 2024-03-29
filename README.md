## 快速开始
``` bash
# 克隆项目
git clone https://github.com/cyansoul/bank-manager-tool.git

# 进入项目目录
cd bank-manager-tool

# 启动Flask服务
python backend/api/main.py

# 安装依赖
npm install

# 启动Vue服务
npm run dev
```

浏览器访问：http://localhost:9527

## 产品架构
![产品架构](/src/assets/images/structure.png)

# 功能

## 1、看一看（首页）

``` bash
基于每天的最新数据，进行多维度产品信息可视化。
```

![看一看](/screenshots/dashboard.png)

## 2、查一查

``` bash
提供发行银行、产品类型、预计收益率、产品期限三个维度的筛选框，结合产品名称关键字进行全库搜索，系统会返回全部符合筛选条件的产品列表，点击「查看」按钮可以获取产品更多维度的信息。

若用户未搜索到本行的产品，可以通过「补充产品信息」入口进行产品数据上传，丰富我们的产品数据库。
```

![查一查](/screenshots/search.png)


## 3、比一比

``` bash
提供「本行」和「对标行」两个下拉框进行对比主体的选择，通过「一键对比」获取两个目标行所发售的产品情况对比，包括产品结构、产品利率、产品期限三个维度。并对应不同维度的对比图，自动生成具有业务指导意义的智能洞察结果。

通过「下载报告」按钮，可将当前页面的对比结果下载并存为PDF文件。
```

![比一比](/screenshots/comparison.png)

## 4、测一测
### 1）产品销量预测
``` bash
使用Prophet算法，结合时间序列分解和机器学习，用各产品的历史销量数据作为训练集，给出未来的销量趋势预测曲线，并提供置信上限和置信下限作为参考。
```

![比一比](/screenshots/ts_pred.png)
### 2）产品售罄时长预测
``` bash
用户可自定义银行、产品发售总量、预计收益率、起售金额、产品期限五个参数，一键获取预测结果。

并基于用户所填写的参数，对收益率、起售金额、产品期限三个字段进行左右区间的拓展，给出对应的预测值曲线，增强参数的可解释性。
```

![比一比](/screenshots/struct_pred.png)


## 数据结构

``` bash
1）产品详情数据
2）各银行产品结构数据
3）产品销量数据
```

## 爬虫方案
![scraper1](/screenshots/scraper1.png)
![scraper2](/screenshots/scraper2.png)
![scraper3](/screenshots/scraper3.png)
