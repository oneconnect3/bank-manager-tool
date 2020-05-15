import pandas as pd

def stand_pct(num):
    stand_num = num*100
    stand_rs = str(round(stand_num, 2)) + '%'

    return stand_rs

def gene_insights(bank1, bank2):

    # 生成insights
    prod_struct_data = pd.read_excel('../data/prod_struct_data_2.xlsx')
    interest_rate_data = pd.read_excel('../data/interest_rate_data_2.xlsx')
    prod_contract_data = pd.read_excel('../data/prod_contract_data_2.xlsx')

    # 筛选两个目标行对应的数据
    bank1_struct = prod_struct_data[prod_struct_data['类别'] == bank1]
    bank2_struct = prod_struct_data[prod_struct_data['类别'] == bank2]

    # 提取所需指标
    A_A1 = bank1_struct['A1'].iloc[0]
    B_A1 = bank2_struct['A1'].iloc[0]
    A_A11 = bank1_struct['A11'].iloc[0]
    A_A2 = bank1_struct['A2'].iloc[0]
    A_A22 = bank1_struct['A22'].iloc[0]

    # 存款产品渗透率
    if A_A1 > B_A1:
        insight1_1_title = '存款产品渗透率高'
        if A_A2 > 0:
            insight1_1 = '与{bank2}相比，{bank1}零售金融产品集中于零售存款，理财产品仅占{A_A11}，渗透率低，产品供给无法满足参财富客户多元化的投资需求，而且{bank1}的存款产品占比远超市场平均水平的{A_A2}；'.format(
                bank1=bank1, bank2=bank2, A_A11=stand_pct(A_A11), A_A2=stand_pct(A_A2))
        else:
            insight1_1 = '与{bank2}相比，{bank1}零售金融产品集中于零售存款，理财产品仅占{A_A11}，渗透率低，产品供给无法满足参财富客户多元化的投资需求，不足市场平均水平的{A_A2}；'.format(
                bank1=bank1, bank2=bank2, A_A11=stand_pct(A_A11), A_A2=stand_pct(A_A2))

    if A_A1 <= B_A1:
        insight1_1_title = '理财产品渗透率高'
        if A_A22 > 0:
            insight1_1 = '与{bank2}相比，{bank1}的零售金融产品集中于理财类产品，产品供给满足参财富客户多元化的投资需求，而且{bank1}的理财产品占比远超市场平均水平的{A_A22}；'.format(
                bank1=bank1, bank2=bank2, A_A22=stand_pct(A_A22))
        else:
            insight1_1 = '与{bank2}相比，{bank1}的零售金融产品集中于理财类产品，产品供给满足参财富客户多元化的投资需求，不足市场平均水平的{A_A22}；'.format(
                bank1=bank1, bank2=bank2, A_A22=stand_pct(A_A22))

    # 提取所需指标
    A_A3 = bank1_struct['A3'].iloc[0]
    B_A3 = bank2_struct['A3'].iloc[0]
    A_A4 = bank1_struct['A4'].iloc[0]
    B_A4 = bank2_struct['A4'].iloc[0]
    B_A5 = bank2_struct['A5'].iloc[0]

    # 特色产品
    if A_A3 <= B_A3:
        insight1_2_title = '特色产品市场竞争力不足'
        insight1_2 = '与{bank2}相比，其现有产品{B_A4}市场占有率高达{B_A5}，同类产品{bank1}竞争优势明显不足，而{bank1}自身的特色产品{A_A4}，没有起到产品承接互补的作用，非常缺乏针对高价值客户的钩子产品和特色财富产品；'.format(
            bank1=bank1, bank2=bank2, B_A4=(B_A4), B_A5=stand_pct(B_A5), A_A4=(A_A4))

    if A_A3 > B_A3:
        insight1_2_title = '特色产品优势明显'
        if A_A22 > 0:
            insight1_2 = '与{bank2}相比，{bank1}的零售金融产品集中于理财类产品，产品供给满足参财富客户多元化的投资需求，而且{bank1}的理财产品占比远超市场平均水平的{A_A22}；'.format(
                bank1=bank1, bank2=bank2, A_A22=stand_pct(A_A22))
        else:
            insight1_2 = '与{bank2}相比，{bank1}的零售金融产品集中于理财类产品，产品供给满足参财富客户多元化的投资需求，而且{bank1}的理财产品不足市场平均水平的{A_A22}；'.format(
                bank1=bank1, bank2=bank2, A_A22=stand_pct(A_A22))

    # 提取关键指标
    A_A7 = bank1_struct['A7'].iloc[0]
    A_A6 = bank1_struct['A6'].iloc[0]

    # 弱势产品
    insight1_3_title = '产品{A_A7}占有严重不足'.format(A_A7=A_A7)
    insight1_3 = '与{bank2}相比，{bank1}的产品{A_A7}占比仅有{A_A6}，{bank1}缺失此类产品的市场份额，无法吸引该产品的目标客群，其较高的产品利率优势还未充分发挥。'.format(
        bank1=bank1, bank2=bank2, A_A7=(A_A7), A_A6=stand_pct(A_A6))

    # 产品期限分布
    A_A1 = prod_contract_data[prod_contract_data['类别']=='A1'][bank1].iloc[0]
    B_A1 = prod_contract_data[prod_contract_data['类别']=='A1'][bank2].iloc[0]
    A_A2 = prod_contract_data[prod_contract_data['类别']=='A2'][bank1].iloc[0]
    B_A2 = prod_contract_data[prod_contract_data['类别']=='A2'][bank2].iloc[0]

    if A_A1 > B_A1:
        insight2_1_title = '短期产品占比较高'
        insight2_1 = '与{bank2}相比，{bank1}的周期产品（3月期以内）占总量的{A_A1}，远高于{bank2}的{B_A1}，应持续增加短期爆款产品发行规模和频率，提高募集资金留存频率，并且通过产品期限调配和类活期产品的衔接，帮客户主动管理产品到期持币等待期间资金；'.format(
            bank1=bank1, bank2=bank2, A_A1=stand_pct(A_A1), B_A1=stand_pct(B_A1))

    if A_A1 <= B_A1:
        insight2_1_title = '短期产品占比较低'
        insight2_1 = '与{bank2}相比，{bank1}的周期产品（3月期以内）占总量的{A_A1}，远低于{bank2}的{B_A1}，应持续增加短期爆款产品发行规模和频率，提高募集资金留存频率，并且通过产品期限调配和类活期产品的衔接，帮客户主动管理产品到期持币等待期间资金；'.format(
            bank1=bank1, bank2=bank2, A_A1=stand_pct(A_A1), B_A1=stand_pct(B_A1))

    B_A2 = bank2_struct['A2'].iloc[0]

    if A_A2 > B_A2:
        insight2_2_title = '长期产品占比较高'
        insight2_2 = '与{bank2}相比，{bank1}的长周期产品（3年以上）占总量的{A_A2},远高于{bank2}的{B_A2},应持续增加长期产品发行规模和频率，提高客户粘性和在我行的资金留存率，并且配合短期产品，增加募集期资金和产品到期赎回资金有针对性地留存。'.format(
            bank1=bank1, bank2=bank2, A_A2=stand_pct(A_A2), B_A2=stand_pct(B_A2))

    if A_A2 <= B_A2:
        insight2_2_title = '长期产品占比较低'
        insight2_2 = '与{bank2}相比，{bank1}的长周期产品（3年以上）占总量的{A_A2},远低于{bank2}的{B_A2}，应持续增加长期产品发行规模和频率，提高客户粘性和在我行的资金留存率，并且配合短期产品，增加募集期资金和产品到期赎回资金有针对性地留存。'.format(
            bank1=bank1, bank2=bank2, A_A2=stand_pct(A_A2), B_A2=stand_pct(B_A2))

    # 产品利率分布
    A_A1 = interest_rate_data[interest_rate_data['类别'] == 'A1'][bank1].iloc[0]
    B_A1 = interest_rate_data[interest_rate_data['类别'] == 'A1'][bank2].iloc[0]
    A_A2 = interest_rate_data[interest_rate_data['类别'] == 'A2'][bank1].iloc[0]
    B_A2 = interest_rate_data[interest_rate_data['类别'] == 'A2'][bank2].iloc[0]

    if A_A1 > B_A1:
        insight3_1_title = '低成本产品占比偏高'
        insight3_1 = '与{bank2}相比，{bank1}的低成本产品（2%以内）占总量的{A_A1}，远高于{bank2}的{B_A1}，在关注高收益的爆款产品的同时，应持续增加低成本财富产品，配合周期性较灵活的产品设计，满足客户对流动性和便捷度的要求，同时提高此类型产品的收益率；'.format(
            bank1=bank1, bank2=bank2, A_A1=stand_pct(A_A1), B_A1=stand_pct(B_A1))

    if A_A1 <= B_A1:
        insight3_1_title = '低成本产品占比偏低'
        insight3_1 = '与{bank2}相比，{bank1}的低成本产品（2%以内）占总量的{A_A1}，远低于{bank2}的{B_A1}，财富类产品中高息存款占比相对，势必会使得存款成本率攀升，在关注高收益的爆款产品的同时，应持续增加低成本财富产品，配合周期性较灵活的产品设计，满足客户对流动性和便捷度的要求，同时提高此类型产品的收益率；'.format(
            bank1=bank1, bank2=bank2, A_A1=stand_pct(A_A1), B_A1=stand_pct(B_A1))

    if A_A2 > B_A2:
        insight3_2_title = '高收益爆款占比高'
        insight3_2 = '与{bank2}相比，{bank1}的高收益产品（4.5%以上）占总量的{A_A2}，远高于{bank2}的{B_A2}，应由高收益爆款产品做好客户预热，适当延长高竞争力产品的募集周期。'.format(
            bank1=bank1, bank2=bank2, A_A2=stand_pct(A_A2), B_A2=stand_pct(B_A2))

    if A_A2 <= B_A2:
        insight3_2_title = '高收益爆款占比低'
        insight3_2 = '与{bank2}相比，{bank1}的高收益产品（4.5%以上）占总量的{A_A2}，远低于{bank2}的{B_A2}，标准定价的活定存缺乏对客吸引力，普通定期存款缺乏有力抓手。'.format(
            bank1=bank1, bank2=bank2, A_A2=stand_pct(A_A2), B_A2=stand_pct(B_A2))

    insights = {
        'insight1_1_title': insight1_1_title,
        'insight1_1': insight1_1,
        'insight1_2_title': insight1_2_title,        
        'insight1_2': insight1_2,
        'insight1_3_title': insight1_3_title,
        'insight1_3': insight1_3,
        'insight2_1_title': insight2_1_title,
        'insight2_1': insight2_1,
        'insight2_2_title': insight2_2_title,
        'insight2_2': insight2_2,
        'insight3_1_title': insight3_1_title,
        'insight3_1': insight3_1,
        'insight3_2_title': insight3_2_title,
        'insight3_2': insight3_2
    }

    print(insights)

    return insights
