from collect.api import api as pbapi
#
# url = pbapi.pb_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
#     YM='{0:04d}{1:02d}'.format(2017, 1),
#     SIDO='서울특별시',
#     GUNGU='',
#     RES_NM='',
#     numOfRows=10,
#     _type='json',
#     pageNo=1)
# print(url)
#
#
for items in pbapi.pb_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
    print(items)

# for items = pbapi.pd_fetch_foreign_visitor(112, 2012, 7):
#     print(items)
'''
item = pbapi.pb_fetch_foreign_visitor(112,2011,7)
print(item)
'''
'''
url = api.fb_gen_url(node='jtbcnews', a=10, b=20, s='kickscar')
print(url)
'''
'''
id = api.fb_name_to_id("jtbcnews")
print(id)
'''
'''
for posts in api.fb_fetch_posts('jtbcnews','2017-01-01','2017-12-31'):
    print(posts)
'''