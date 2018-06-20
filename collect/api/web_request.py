from urllib.request import  Request,urlopen
from datetime import *
import json
import sys

def json_request(url='',
    encoding = 'utf-8',
    success = None,
    error = lambda e:print('%s %s' % (e,datetime.now()),file = sys.stderr)):

    try:
        # request객체 생성
        request = Request(url)
        resp = urlopen(request)


    # 응답내용을 다 읽는다.
        html = resp.read().decode(encoding)
        json_result = json.loads(html) # 읽어온 데이터형식이 dict으므로 자동으로 json_result는 dict으로 저장

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            # success = None이 여서 html이 return됨 , 함수인지 아닌지를 판별
            return json_result
            # return값을 주는 의미는 바깥에서 처리해라 뜻


          #else

        success(json_result)

    except Exception as e:
         if callable(error) is True:
             error(e)


def html_request(
        url=' ',
        encoding = 'utf-8',
        success = None,
        error = lambda e:print('%s %s' % (e,datetime.now()),file = sys.stderr) #standard err
        ):# lambda : 함수 한줄로 만들기 이름이 없는 함수 -- (익명함수: 한번만 호출할 때)
# success = function(함수명)
    try:
         # request객체 생성
        request = Request(url)
        resp = urlopen(request)

    # 응답내용을 다 읽는다.
        html = resp.read().decode(encoding)

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False: # 함수인지 아닌지를 판별

            return html # return값을 주는 의미는 바깥에서 처리해라 뜻


    except Exception as e:
         if callable(error) is True:
             error(e)
