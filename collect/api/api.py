
# FB API WRAPPER FUNCTIONS
from urllib.parse import urlencode
from collect.api.web_request import json_request # 현디렉토리 .  /  상위 디렉토리 ..
from datetime import  *
import math
import sys

END_POINT ='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
SERVICE_KEY='YHMyEqaNs%2Bb8wx%2FroF7AkdmXlA1NofEJPOK5B3BI9tbwbMTfcxiZhQ2Kr0WO6icXc4SmOmSzpi0NvViyF2TFiA%3D%3D'


def pb_gen_url(endpoint = END_POINT, service_key = SERVICE_KEY, **params):

    url = '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params)) # urlencode땜에 service key를 params로 하면 안됨
    # 서비스키는 encoding이 된상태라서 하면 안된당!
    return url

def pb_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0,
        service_key=''):

    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    pageno = 1
    hasnext = True

    while hasnext:
        url = pb_gen_url(
            endpoint,
            service_key,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            numOfRows=100,
            _type='json',
            pageNo=pageno)
        json_result = json_request(url=url)
        if json_result is None:
            break

        json_response = json_result.get('response')
        json_header = json_response.get('header')
        result_message = json_header.get('resultMsg')

        if 'OK' != result_message:
            print('%s : Error[%s] for Request(%s)' % (datetime.now(), result_message, url), file=sys.stderr)
            break

        json_body = json_response.get('body')

        numofrows = json_body.get('numOfRows')
        totalcount = json_body.get('totalCount')

        if totalcount == 0:
            break

        last_pageno = math.ceil(totalcount/numofrows)
        if pageno == last_pageno:
            hasnext = False
        else:
            pageno += 1

        json_items = json_body.get('items')
        yield json_items.get('item') if isinstance(json_items, dict) else None

# def pb_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0,pageNo= 1,service_key= ''):
#
#     isnext = True
#     results = []
#
#     while isnext:
#
#         url = pb_gen_url(endpoint=END_POINT,
#                          serviceKey=SERVICE_KEY,
#                          SIDO=district1,
#                          GUNGU=district2,
#                          RES_NM=tourspot,
#                          YM='{0:04d}{1:02d}'.format(year, month),
#                          _type='json',
#                          numOfRows=10,
#                          pageNo=pageNo)
#
#         json_result = json_request(url=url)
#         json_response = json_result.get('response')
#         json_header = json_response.get('header')
#         result_message = json_header.get('resultMsg')
#         # print("result_message" + ":" + result_message)
#
#         if 'OK' != result_message:
#             print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
#             return None
#
#         json_body = json_response.get('body')
#         json_items = json_body.get('items')  # 함수내에서 변수선언은 한번 쓰고 없어지므로 의미있게 쓰자
#
#         numOfRows = json_body.get('numOfRows')
#         totalCount = json_body.get('totalCount')
#
#         if totalCount == 0:
#             break
#
#         last_page = math.ceil(totalCount/numOfRows)
#
#         if pageNo == last_page:
#             isnext = False
#         else:
#             pageNo += 1
#         for item in json_items.get('item'): # 리스트에 있는 딕션을 리스트에 다시 담는다.
#             results.append(item)
#
#     return results
#


def pb_fetch_foreign_visitor(country_code = '',year = 0,month = 0,service_key = ''):

   endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

   url = pb_gen_url(endpoint,
                    service_key,
                    YM='{0:04d}{1:02d}'.format(year, month),
                    NAT_CD = country_code,
                    ED_CD = 'E',
                    _type='json',
                    )

   # header는 통신의 성공유무 , body는 내용
   json_result = json_request(url = url)
   json_response = json_result.get('response')
   json_header = json_response.get('header')
   result_message = json_header.get('resultMsg')

   if 'OK' != result_message:
       print('%s Error[%s] for request %s' % (datetime.now(),result_message,url))
       return None

   json_body = json_response.get('body')
   json_items = json_body.get('items') # 함수내에서 변수선언은 한번 쓰고 없어지므로 의미있게 쓰자
   return json_items.get('item') if isinstance(json_items, dict) else None



