import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import glob
import csv
from tkinter import filedialog

typ = [('', '*.csv')]
dir = 'C:\\pg'
files = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 
fnames = []
data_lst =[]
count = 0
files_data =[]




for a in files:
    fname = a.split()[2]
    fnames.append(fname)
    print(fname)
    rows = []
    print(a)
    with open(a,encoding="utf-8") as f:   
        reader = csv.reader(f)
        rows = [row for row in reader]
    header = rows.pop(0)
    data = np.float_(np.array(rows).T)
    rivals = [x+y for x,y in zip(data[1],data[2])]
    data = list(data)
    data.append(rivals)
    length =len(data[0])
    print(length)
    #ポップアップで動画の秒数を取得
    layout =[[sg.Text(fname+"の動画時間を教えて下さい")],
             [sg.InputText(default_text="0",key='m',size=(10,10)),sg.Text("分"),sg.InputText(default_text="01",key='s',size=(10,10)),sg.Text("秒")],
             [sg.Button('決定')]]
    window = sg.Window('動画の秒数確認', layout)
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '決定':
            second = int(value['m'])*60+int(value['s'])
            break
    window.close()
    #分秒を秒に変換してからデータ数に合わせて分割し、dataにappendする
    #喰った　 2:24
    #旅じまい  2:51
    #準備できた？　1:36
    print(second)
    seconds =[(second*x)/length for x in range(length)]
    print(seconds)
    data.append(seconds)


    data_lst.append(data)
    plt.title(fnames[count],fontname="MS Gothic")
    plt.xlabel("time (second)")
    plt.ylabel("retation")
    plt.plot(data[4], data[1], linestyle='solid',label=fnames[count])
    plt.plot(data[4], data[3], linestyle='solid',label='rivals of ' + fnames[count])
    plt.legend(loc = 'upper right',prop={"family":"MS Gothic"})
    plt.show()
    count+=1

plt.title("Songs Retation")
plt.xlabel("time (second)")
plt.ylabel("retation")
for x in range(len(files)):
    plt.plot(data_lst[x][4], data_lst[x][1], linestyle='solid',label=fnames[x])
plt.legend(loc = 'upper right',prop={"family":"MS Gothic"})
plt.show()


