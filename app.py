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
