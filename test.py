import numpy as np
from urllib import request
import requests as req
import tkinter
import tkinter.messagebox
import tkinter.ttk
from project_function import *
from function_call import *

def click_bus(text_box):
    global Line_used_list
    Line_Name = text_box.get()
    Line_used_list = consult_Bus_Line(Line_Name)
    if type(Line_used_list) == list:
        if len(Line_used_list) == 0:
            Line_output_list = []
            out_string = '*********** 非常抱歉，未能找到提示的线路 ***********' 
            # 标准字符串差不多这么长(重点是字符串数量)
        else:
            # Line_output_list = list(map(lambda x: x['caption'] , Line_used_list))
            Line_output_list = []
            for item in Line_used_list:
                Line_output_list.append(item['caption'])
            out_string = '  请继续操作，从下面的方框中选择线路和方向  '
    else:
        Line_output_list = []
        out_string = Line_used_list

    Line_combo["values"] = tuple(Line_output_list)
    text_OUT["bg"] = "yellow"
    text_OUT["fg"] = "black"
    text_OUT["text"] = out_string

def get_Line_combo(event):
    global Line_used_list
    global Station_used_list
    global Line_id
    Line_caption = Line_combo.get()
    for item in Line_used_list:
        if item['caption'] == Line_caption:
            Line_id = item['lineId']
            break
    Station_used_list = consult_Line_Station(Line_id)
    if type(Station_used_list == list) :
        if len(Station_used_list) == 0:
            Station_output_list = []
            out_string = '**** 抱歉，未能找到列表选择线路车站信息，请重试 **** '
        else:
            Station_output_list = []
            for item in Station_used_list:
                Station_output_list.append(item['stopName'])
            out_string = '  请继续操作，从下面的方框中选择将要查询的车站  '
    else:
        Station_output_list = []
        out_string = Station_used_list

    Station_combo["values"] = tuple(Station_output_list)
    text_OUT["bg"] = "green"
    text_OUT["fg"] = "black"
    text_OUT["text"] = out_string
            
def get_Bus_combo(event):
    Bus_Stop_Name = Station_combo.get()
    global Station_used_list
    for item in Station_used_list:
        if item['stopName'] == Bus_Stop_Name:
            Station_id = item['stationId']
            Line_id = item['lineId']
            break
    Bus_List = consult_Bus(Line_id,Station_id)
    if type(Bus_List) == list:
        out_string = '实时查询成功_信息如下：\n'
        Bus_List.reverse()
        for item in Bus_List:
            if len(item) == 6:
                temp_string = '第'+str(int(item['"index"'])+1)+'辆车  '+'估计剩余时间: '+item['"eta"']+'s  '+'车号: '+item['"gpsId"']+'\n'
                temp_string1 = '           剩余距离: ' +item['"distance"']+'m  剩余站数: '+item['"stationLeft"']+' \n'
                out_string = out_string + temp_string + temp_string1
            elif len(item) == 5:
                temp_string = '第'+str(int(item['"index"'])+1)+'辆车  '+'估计剩余时间: '+item['"eta"']+'s   '+'\n'
                temp_string1 = '           剩余距离: ' +item['"distance"']+'m  剩余站数: '+item['"stationLeft"']+' \n'
                out_string = out_string + temp_string + temp_string1
            else:
                out_string = '非常抱歉，服务器并不能返回正确的该线路的实时数据 '
    else:
        out_string = Bus_List
        

    text_OUT["bg"] = "gray"
    text_OUT["fg"] = "black"
    text_OUT["text"] = out_string

Line_output_list = []
Station_output_list = []
Bus_output_list = []
out_string = '  暂时没有信息需要输出，请继续操作  '

Line_used_list =[]
Station_used_list = []
Line_id = 0

root = tkinter.Tk()
root.title(' real-time BUS Consult ')

root['height'] = 600
root['width'] =400

label_Line_Name = tkinter.Label(root, text = '请输入线路名称:', justify = tkinter.RIGHT, width = 100)
label_Line_Name.place(x = 30, y = 5, width =100, height =30)

entry_Line = tkinter.Entry(root,text = "")
entry_Line.place(x = 150, y = 5, width = 100, height =30)

button_Line = tkinter.Button(root , text=' 确定 ', command = lambda: click_bus(entry_Line))
button_Line.place(x=270, y=5, width=100, height=30)

label_Line_Information = tkinter.Label(root, text = '请选择线路和方向:', justify = tkinter.RIGHT, width = 100)
label_Line_Information.place(x = 30, y = 50, width =100, height =30)

Line_combo = tkinter.ttk.Combobox(root,values= [])
Line_combo.place(x = 150, y =50 , width =200 , height =30)
Line_combo.bind('<<ComboboxSelected>>', get_Line_combo)

label_Station = tkinter.Label(root, text = '请选择查询站点:', justify = tkinter.RIGHT, width = 100)
label_Station.place(x = 30, y = 100, width =100, height =30)

Station_combo = tkinter.ttk.Combobox(root,values= [])
Station_combo.place(x = 150, y = 100 , width =200 , height =30)
Station_combo.bind('<<ComboboxSelected>>', get_Bus_combo)

text_OUT = tkinter.Message(text="")
text_OUT.place(x=50, y=150, width=300, height=420)
text_OUT["anchor"] = "nw"
text_OUT["aspect"] = 2000
text_OUT["justify"] = "left"
text_OUT["bg"] = "white"
text_OUT["fg"] = "black"
text_OUT["text"] = out_string

def main():
    root.mainloop()

if __name__ == "__main__":
    main()