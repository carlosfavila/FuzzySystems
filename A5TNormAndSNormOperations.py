# -*- coding: utf-8 -*-
"""A5 TNorm and SNorm Operation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wrTDLmVBqEqBHriPa60g0OUYsUBljKut
"""

import matplotlib.pyplot as plt
import numpy as np

#Creating the Universe and the lists of the MF
universe=np.arange(-15, 15, 0.1)
A=[]
B=[]
tdp=[]
sds=[]

#Creating the Membership Functions
for k in universe:
  A.append(1/(1+((k+5)/7.5)**4))
  B.append(1/(1+((k-5)/5)**2))

#For Drastic Product
for k in range(len(universe)):
  if B[k]==1:
    tdp.append(A[k])
  elif A[k]==1:
    tdp.append(B[k])
  elif (A[k] and B[k])<1:
    tdp.append(0)
  else:
    tdp.append(1)

for k in range(len(universe)):
  if B[k]==0:
    sds.append(A[k])
  elif A[k]==0:
    sds.append(B[k])
  elif (B[k] and A[k])>0:
    sds.append(1)
  else:
    sds.append(0)
  

fig=plt.figure(figsize=(10,10),tight_layout=True)
fig.supylabel('Membership Degree')
fig.suptitle("T-Norm & S-Norm Operators")

plt.subplot(4,2,1)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(min(A[k],B[k])) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Tmin(A,B)")
plt.grid(True)

plt.subplot(4,2,2)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(max(A[k],B[k])) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Smax(A,B)")
plt.grid(True)

plt.subplot(4,2,3)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(A[k]*B[k]) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Tap(A,B)")
plt.grid(True)

plt.subplot(4,2,4)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(A[k]+B[k]-A[k]*B[k]) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Sas(A,B)")
plt.grid(True)

plt.subplot(4,2,5)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(max(0,(A[k]+B[k]-1))) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Tbp(A,B)")
plt.grid(True)

plt.subplot(4,2,6)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(min(1,(A[k]+B[k]))) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Sbs(A,B)")
plt.grid(True)

plt.subplot(4,2,7)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(tdp[k]) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Tdp(A,B)")
plt.grid(True)

plt.subplot(4,2,8)
plt.plot(universe,A,'--r',universe,B,'--g',universe,[(sds[k]) for k in range(len(universe))],'#2a85b0')
plt.xlabel("Universe")
plt.title("Sds(A,B)")
plt.grid(True)