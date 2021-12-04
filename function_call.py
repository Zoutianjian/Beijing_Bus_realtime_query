import numpy as np
from urllib import request
import requests as req
from project_function import *

def consult_Bus_Line(Line_name):

    Line_url_str = 'http://www.bjbus.com/api/api_etaline_list.php?hidden_MapTool=busex2.BusInfo&city=%25u5317%25u4EAC&pageindex=1&pagesize=30&fromuser=bjbus&datasource=bjbus&clientid=9db0f8fcb62eb46c&webapp=mobilewebapp&what='
    Line_name = Line_name.encode('utf-8')
    Line_name = str(Line_name)
    Line_name = Line_name[2:-1].replace('\\x','%')
    Line_name = Line_name.upper()
    Line_url_str = Line_url_str + Line_name

    try:
        response = req.get(Line_url_str)
        Line_List = get_Line_List(response.content.decode('utf-8'))
    except:
        Line_List = '网络连接错误，无正常返回结果，请检查网络之后重试！'
    
    return Line_List

def consult_Line_Station(Line_ID_Str):
    Station_Str1 = 'http://www.bjbus.com/api/api_etastation.php?lineId='
    
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTEyODgwMDB9.BJqtzMSedNqs3d12hWLHFC-PeWk_dToFGZ25Kumc4RM'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTM5NDQ4MDB9.dIwtbSPc52TzsQ68DafuImR2_NZcJ08sQZjfXWoSJS0'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTY1MzY4MDF9.BalA1LZoStafkHzomepuv51bUDdiQY8Q6JiB_l8vIW8'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTkxMjg4MDF9.BikJy-wEpHr0Ao6kKGD4CPCYeP7l3fZORYz0f-A0Bog'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MjE3MjA4MDF9.fiP0eWDkEb8jZ4V9JIpwkt9vIJuhFsD7DuBaR8S1ers'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MjQ1MDMxMDB9.l1a915d9OleMq_6YUjch004V0ZGNsXlqa6iGMB_m0i8'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MjcwOTkyMDB9.OQYkF6rC9jfgxoC5nXDjjv1nqDIv3KfXqol0ATdts9g'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MzAxMjA3MDJ9.RIWvu5qeD2iziXk3kOEYJeeRge8hH1OuwDwhGxjew7w'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MzI3MTUyMDB9.KAznHQ57w7lAhMapHhCtkTnEYm2nMu4PZ02_qriDF44'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2Mzg0MTc2MDB9.rKPp15ziIsnlmu3h3zI8lZMSi4tSw0ADU4Gxfm01Ngs'
    Station_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2NDEwNzQ0MDJ9.4zXkjluUtdcbW8r81N6PxFsRBTldqmT1YB8nzGVp-yc'
    Station_url_str = Station_Str1 + Line_ID_Str + Station_Str2

    try:
        response1 = req.get(Station_url_str)
        Station_List = get_Station_List(response1.content.decode('utf-8'))        
    except:
        Station_List = '线路选择错误 或 网络连接错误，请检查后重试！'

    return Station_List

def consult_Bus(Line_ID_Str,Station_Str):
    Bus_Str1 = 'http://www.bjbus.com/api/api_etartime.php?conditionstr='
    Bus_ID_Str = Line_ID_Str + '-' + Station_Str
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTEyODgwMDB9.BJqtzMSedNqs3d12hWLHFC-PeWk_dToFGZ25Kumc4RM'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTM5NDQ4MDB9.dIwtbSPc52TzsQ68DafuImR2_NZcJ08sQZjfXWoSJS0'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTY1MzY4MDF9.BalA1LZoStafkHzomepuv51bUDdiQY8Q6JiB_l8vIW8'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MTkxMjg4MDF9.BikJy-wEpHr0Ao6kKGD4CPCYeP7l3fZORYz0f-A0Bog'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MjE3MjA4MDF9.fiP0eWDkEb8jZ4V9JIpwkt9vIJuhFsD7DuBaR8S1ers'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MjQ1MDMxMDB9.l1a915d9OleMq_6YUjch004V0ZGNsXlqa6iGMB_m0i8'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MjcwOTkyMDB9.OQYkF6rC9jfgxoC5nXDjjv1nqDIv3KfXqol0ATdts9g'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MzAxMjA3MDJ9.RIWvu5qeD2iziXk3kOEYJeeRge8hH1OuwDwhGxjew7w'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2MzI3MTUyMDB9.KAznHQ57w7lAhMapHhCtkTnEYm2nMu4PZ02_qriDF44' 
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2Mzg0MTc2MDB9.rKPp15ziIsnlmu3h3zI8lZMSi4tSw0ADU4Gxfm01Ngs'
    Bus_Str2 = '&token=eyJhbGciOiJIUzI1NiIsIlR5cGUiOiJKd3QiLCJ0eXAiOiJKV1QifQ.eyJwYXNzd29yZCI6IjY0ODU5MTQzNSIsInVzZXJOYW1lIjoiYmpidXMiLCJleHAiOjE2NDEwNzQ0MDJ9.4zXkjluUtdcbW8r81N6PxFsRBTldqmT1YB8nzGVp-yc'
    Bus_url_str = Bus_Str1 + Bus_ID_Str + Bus_Str2
    try:
        response2 = req.get(Bus_url_str)
        Bus_List = get_Bus_List(response2.content.decode('utf-8')) # 注意 Bus_List 的索引需要加双引号！
    except:
        Bus_List = '查询错误 或 网络连接错误，请检查后重试！'
    
    return Bus_List