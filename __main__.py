import sys
from collect import crawler as collection
from config import CONFIG
import visualize
import analize
import collect

#
# sys.path.append('/pychamProjects/python-modules')
# ## analysus_fb를 실행시켜줌
# from analysis_fb.collect import  crawler as cw
#collect


if __name__ == '__main__':

    #collection

    resultfiles = dict()

    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    #analysis
    #result_analysis = analize.analysis_correlation(resultfiles)
    result_analysis = analize.analysis_correlation_by_tourspot(resultfiles)
    #print(result_analysis)

    #visualize
    # 01월 01~ 12월 31

    # 데이터 분석(analyze)

    # 데이터 시각화(visualize)
    #visualize.graph_scatter(result_analysis)

