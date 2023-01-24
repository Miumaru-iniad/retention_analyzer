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

for a in files:
    rows = []
    print(a)
    with open(a,encoding="utf-8") as f:   
        reader = csv.reader(f)
        rows = [row for row in reader]
    header = rows.pop(0)
    data = np.float_(np.array(rows).T)
    plt.xlabel("time")
    plt.ylabel("reitation")
    plt.plot(data[0], data[1], linestyle='solid')
    plt.plot(data[0], data[2], linestyle='solid')
    plt.show()



