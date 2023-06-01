import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1
    
b=-0.25
w=[0.5,0.25]

X=np.arange(-3,3,0.2)
Y=np.arange(-3,3,0.2)

fig1=plt.figure(1)
for x in X:
    for y in Y:
        a=hardlim(w[0]*x+w[1]*y+b)
        if a==1:
            plt.plot(x,y,'ro')
        else:
            plt.plot(x,y,'bo')
        
limline=[]
xp=np.arange(0,0.5,0.2)
for x in X:
    limline.append(-b/w[1]-w[0]/w[1]*x)


wp=[]
for x in xp:
    wp.append(0.5*x)
plt.plot(X,limline,'k-',xp,wp,'k-')
plt.xlabel('P1')
plt.ylabel('P2')     
plt.show()