from collect.api.web_request import json_request as wr

# test for web_request

url ='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'


'''dwqdwq
deqd
feqdw
efqw
'''


def success_fetch_user_list(response):
    print(response)


def error_fetch_user_list(e):
    print(e)

wr.json_request(url=url, success = success_fetch_user_list, error = error_fetch_user_list)

'''
json_result = wr.json_request(url)
print(json_result)
'''

# https://graph.facebook.com/v3.0/jtbcnews/posts/?access_token=(토큰을 넣어라 가로도 지우고)&since=20170101&untill=20171231&limit=50