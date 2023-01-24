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
for f in files:
    fname = f.split()[2]
    fnames.append(fname)
    print(fname)

data_lst =[]

count = 0
for a in files:
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
    plt.title(fnames[count],fontname="MS Gothic")
    plt.xlabel("time")
    plt.ylabel("retation")
    plt.plot(data[0], data[1], linestyle='solid',label=fnames[count])
    plt.plot(data[0], data[3], linestyle='solid',label='rivals of ' + fnames[count])
    plt.legend(loc = 'upper right',prop={"family":"MS Gothic"})
    plt.show()
    count+=1



