#!/usr/bin/env python
# coding=utf-8

from sympy import *
import numpy as np
import pandas as pd

x, r = symbols('x')
vl, vh = 10.0, 100.0
lambs = [1,2,3,4]
T = 3
f = 1.0/(vh-vl)

Rs = []
for lamb in lambs:
	R = []
	for r in xrange(int(vl),int(vh),1):
		integral = integrate((x-vl)/(vh-vl)+x/(vh-vl)*exp(-lamb*T*(1-(r-vl)/(vh-vl))*(1-(x-vl)/(vh-vl))),(x,r,vh))
		R.append(lamb*T*integral)
	Rs.append(R)
Rs = np.array(Rs)
Rs = np.transpose(Rs)

df = pd.DataFrame({
	'lambda=1':Rs[:,0],
	'lambda=2':Rs[:,1],
	'lambda=3':Rs[:,2],
	'lambda=4':Rs[:,3]
	})

print df.head()

df.to_csv('T=3.csv',index=False )
