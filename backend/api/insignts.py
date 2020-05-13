def gene_insights(df, bank1, bank2):
    bank1_dep = df[df['银行'] == bank1]['存款类产品']iloc[0]
    bank2_dep = df[df['银行'] == bank2]['存款类产品']iloc[0]
    ratio = 1-bank1_dep

    if bank1_dep > bank2_dep:
        insight1 = '与{bank2}相比，{bank1}零售金融产品集中于零售存款，理财产品仅占{ratio}，渗透率低，产品供给无法满足财富客户多元产品需求，但是'.format(
            bank1=bank1, bank2=bank2, ratio=ratio)
