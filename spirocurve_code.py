# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 03:53:22 2021

@author: DHRUV
"""

import math as m
import numpy as np
import csv 
import pandas as pd
import os


x = []
y = []
coordinates  = []

R = 8
r = 1
a = 4 

nRev = 2*10
pi = m.pi


lim  = pi*nRev

lat = 34.02057455926032
long = -118.28544662053403

f = open("demofile2_smaller.txt", "a")

for t in np.arange(0.0,lim,0.04):
    tx = (R+r)*(m.cos((r/R)*t)) - a*m.cos((1+r/R)*t)
    ty = (R+r)*(m.sin((r/R)*t)) - a*m.sin((1+r/R)*t)
    
    X = lat + 0.001*tx
    Y = long + 0.001*ty
    
    x.append(X)
    y.append(Y)
    
    f.write(str(Y) + ','+str(X)+'\n')

f.close()




