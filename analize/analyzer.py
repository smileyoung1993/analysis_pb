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

    return r
#    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())

def analysis_correlation_by_tourspot(resultfiles):
    results = []
    r_list = []
    r_dict={}
    a=0
    tour_spot_dict = dict()
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    # print(tourspotvisitor_table)
    tourist_spot_list = tourspotvisitor_table['tourist_spot'].unique() # unique()는 한요소를 가져오면서 리스트를 만들어준다.

    # for a in tourist_spot_list:


    # tour_spot_dict = {'tourist_spot': str(temp_table['tourist_spot'].unique())}
    for temp_tourist in tourist_spot_list:
        tour_spot_dict.update({'tourspot': temp_tourist})
        temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == temp_tourist]
        temp_table = temp_table.set_index('date')
        # print(temp_table)

        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')
            # print(foreignvisitor_table)
            foreignvisitor_list = foreignvisitor_table['country_name'].unique()
            merge_table = pd.merge(temp_table, foreignvisitor_table,left_index=True,right_index=True)
            # print(merge_table)

            x = list(merge_table['visit_count'])
            # print('x: ',x)
            y = list(merge_table['count_foreigner'])
            # print('y : ', y)

            r = correlation_coefficient(x,y)
            # print('r : ',r)
            r_list.append(r)
            r_dict.update({'r_{}'.format(foreignvisitor_list[0]):r})
        
        tour_spot_dict.update(r_dict) # 완성된 하나의 관광명소 상관계수 딕셔너리
        results.append(tour_spot_dict.copy()) # 완성된 하나의 관광명소 딕셔너리를 카피해서 리스트에 추가
        # results.append(tour_spot_dict)
        print(results)
    return results

            # if foreignvisitor_list[0] == '미국':
            #     results.append(r_dict)
            # tour_spot_dict.update(r_dict)
        # print(tour_spot_dict)
        # results.append(tour_spot_dict)
    # print(results)    # print(tour_spot_dict)

    # #         #if len(r_list) == 3:
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






















