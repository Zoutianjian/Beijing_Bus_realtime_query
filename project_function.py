import numpy as np
from urllib import request
import requests as req

def transfer(str1):
    str1 =str1.encode('ascii').decode('unicode_escape') #'utf-8'换成 ascii 或者不写都可以
    return str1

def get_Line_List(txt1):
    txt1 = str(txt1)
    txt1 = txt1[txt1.find('[')+1:txt1.find(']')]
    txt1 = txt1 + ',' #其实可以不用加，但为了使整个过程更加清楚，还是加上去
    Line_List = txt1.split('{')
    Line_List.pop(0)
    Line_List = list(map(lambda x: x[0:-2], Line_List))
    # Line_List = list(map(lambda x: list(map(lambda y: list(map(lambda z: z[1:-1],y.split(':'))),x.split(','))),Line_List))
    Line_List = list(map(lambda x: list(map(lambda y: y.split('"'),x.split(','))),Line_List))
    Line_List = list(map(lambda x: dict(map(lambda y: [y[1],y[3]],x)),Line_List))
    Line_List = list(map(lambda x: get_Chinese(x),Line_List))
    return Line_List

def get_Chinese(Line_Dic):
    Line_Dic['lineName'] = transfer(Line_Dic['lineName'])
    Line_Dic['firstStationName'] = transfer(Line_Dic['firstStationName'])
    Line_Dic['lastStationName'] = transfer(Line_Dic['lastStationName'])
    Line_Dic['subcategorytxt'] = transfer(Line_Dic['subcategorytxt'])
    Line_Dic['caption'] = transfer(Line_Dic['caption'])
    return Line_Dic

def get_Station_List(txt1):
    txt1 = str(txt1)
    if txt1[-6:-1] == '10002':
        Station_List = '请求格式异常，请确认输入正确信息'
    elif txt1[-6:-1] == '10001':
        Station_List = '查无此线路，请检查后输入'
    else:
        txt1 = txt1[txt1.find('[')+1:txt1.find(']')]
        txt1 = txt1 + ',' #其实可以不用加，但为了使整个过程更加清楚，还是加上去
        Station_List = txt1.split('{')
        Station_List.pop(0)
        Station_List = list(map(lambda x: x[0:-2], Station_List))
        Station_List = list(map(lambda x: list(map(lambda y: y.split(':'),x.split(','))),Station_List))
        Station_List = list(map(lambda x: dict(map(lambda y: list(map(lambda z: z[1:-1],y)),x)),Station_List)) 
        # 其实上一句可以塞在上上一句里面，不过为了调试，先不这样做
    return Station_List
    
def get_Bus_List(txt1):
    txt1 = str(txt1)
    txt1 = txt1[txt1.find('[')+1:txt1.find(']')]
    if txt1.find('[') == -1:
        Bus_List = '当前线路在查询站之前尚无车辆接近 查询结果为空'
    else:
        txt1 = txt1[txt1.find('[')+1:]
        txt1 = txt1 + ',' #其实可以不用加，但为了使整个过程更加清楚，还是加上去
        Bus_List = txt1.split('{')
        Bus_List.pop(0)
        Bus_List = list(map(lambda x: x[0:-2], Bus_List))
        Bus_List = list(map(lambda x: dict(map(lambda y: y.split(':'),x.split(','))),Bus_List))    
    return Bus_List

        

