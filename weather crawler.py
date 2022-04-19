from requests import *
from json import *
a=input('请输入城市：')
url='https://www.tianqiapi.com/api/?version=v6&appid=74169348&appsecret=ti3VzXtb&city=%s'%a
b=loads(get(url).text)
print('当前城市：'+b['city'])
print('更新时间：'+b['update_time'])
print('建议：'+b['air_tips'])
print('温度：'+b['tem']+'℃')
print('风速：'+b['win_speed'])
print('风力：'+b['win_meter'])
print('风向：'+b['win'])
print('天气：'+b['wea'])