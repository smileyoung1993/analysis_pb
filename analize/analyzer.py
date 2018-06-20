import json
import pandas as pd
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
import math

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())
    results = []
    #
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')
        merge_table = pd.merge(temp_tourspotvisitor_table,foreignvisitor_table,left_index = True, right_index = True)

        print(merge_table)
        # merge
        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        r = ss.pearsonr(x,y)[0]
         #r = np.corrcoef(x,y)[0]
        data = {'x':x, 'y':y, 'country_name':country_name, 'r': r}
        results.append(data)

    return results

def correlation_coefficient(x, y):

    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except:
        r = 0.0
        print(r)

    return r
#    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())

def analysis_correlation_by_tourspot(resultfiles):
    results = []
    r_list = []
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    tourist_spot_list = tourspotvisitor_table['tourist_spot'].unique()
    for temp_tourist in tourist_spot_list:
        temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == temp_tourist]
        temp_table = temp_table.set_index('date')

    #########foreign_visitor##########

        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())

            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')
            merge_table = pd.merge(temp_table, foreignvisitor_table,left_index=True,right_index=True)
            print(merge_table)
            x = list(merge_table['visit_count'])
            y = list(merge_table['count_foreigner'])
            r_list.append(correlation_coefficient(x,y))
        print(r_list)
            #if len(r_list) == 3:
            # country_name = foreignvisitor_table['country_name'].unique().item(0)
             #r = ss.pearsonr(x, y)[0] # 방문 빈도 계수 구하기
             #r = np.corrcoef(x, y)[0]
            #results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})

            #merge_table['visit_count'].plot(kind='bar')
            #plt.show()
        #return results







''' # 1. analysis and visualize
       result_analyze = analyze.analysis_correlation(resultfiles)
       #visialize.graph_scatter(result_analysis)
       #print(result_anlaysis)


       # 2. analysis and visualize
       # result_analysis = analyze.analysis_correlation_by_tourspot() # 각 관광명소와 각 나라 관광객들의 상관계수 ex)창덕궁 방문자 수(count_foreigner)와 일본 관광객(visit_count)의 상관계수
       # graph_table = pd.DataFrame(result_analysis, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
       # graph_table = graph_table.set_index('tourspot')
       #
       # graph_table.plot(kind='bar')
       # plt.show()
   '''






















