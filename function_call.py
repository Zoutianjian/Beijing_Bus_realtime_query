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
    Bus_url_str = Bus_Str1 + Bus_ID_Str + Bus_Str2
    try:
        response2 = req.get(Bus_url_str)
        Bus_List = get_Bus_List(response2.content.decode('utf-8')) # 注意 Bus_List 的索引需要加双引号！
    except:
        Bus_List = '查询错误 或 网络连接错误，请检查后重试！'
    
    return Bus_List