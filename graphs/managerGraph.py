#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:50:06 2018

@author: ll14m3k
"""


import mySQLdb
import panadas as pd
from pandas import DataFrame
import plotly.plotly as py
from plotly.graph_objs import *
import matplotlib.pyplot as plt
import numpy as np



def weeklyTakings(#weekCommencing):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="XXXX", db="world")
    cursor = conn.cursor()
    cursor.execute('select Week, Day, Takings');
    rows = cursor.fetchall()
    str(rows)[0:300]
    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'Week', 1: 'Day', 2: 'Takings'}, inplace=True);
    df = df.sort(['Takings'], ascending=False);
    
    
    
    
    x = np.array([0,1,2,3,4,5,6])
    y = np.array([0,1000,2000,3000])
    my_xticks = ['Monday','Tuesday','Wednesday','Thursday', 'Friday']
    plt.xticks(x, my_xticks)
    plt.xlabel(’Day of Week’)
    plt.ylabel(’Takings in £’)
    plt.plot(x, y)
    plt.show()