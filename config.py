import os

# configuration
SERVICE_KEY='YHMyEqaNs%2Bb8wx%2FroF7AkdmXlA1NofEJPOK5B3BI9tbwbMTfcxiZhQ2Kr0WO6icXc4SmOmSzpi0NvViyF2TFiA%3D%3D'
result_directory = '__result__/crawling'
# configuration

CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'start_year': 2017,
        'end_year': 2017,
        'fetch': False, # 키를 많이 못쓰게 하려고 FALSE로 설정함
        'result_directory': '__results__/crawling',
        'service_key': SERVICE_KEY
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])