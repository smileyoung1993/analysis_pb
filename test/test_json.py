# test json


# browser 만들기

# html 받기
from urllib.request import  Request,urlopen
from datetime import *
import sys
import json



try:
    url='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'

    Request(url)  # request객체 생성

    request = Request(url)
    resp = urlopen(request)

    # 응답내용을 다 읽는다.
    resp_body = resp.read().decode("utf-8")
    json_result = json.loads(resp_body) # str타입을 dict형태로 바꿔준다.

    # json을 하는 이유는 파이썬에서 데이터를 다루기 싶게 하기위해 객체형태인 dict를 사용
    print(type(resp_body), ":" ,resp_body)
    print(type(json_result) , ":" , json_result) # json은 dict형태이다.

    data = json_result['data']
    print(type(data), ":" , data)

except Exception as e:
    print('%s %s' % (e,datetime.now()),file = sys.stderr) #standard err

