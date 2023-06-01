import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1

x = np.arange(-6,6,0.2)
W11 = [-0.1,-1]; #m=10
W12 = [-0.5,0.25]; #m=-0.5
W13 = [0.5,-0.1]; #m=-0.2
W14 = [0.1,1]; #m=10
W1 = [W11,W12,W13,W14]
b11 = -np.dot(W11 ,[10,4])
b12 = -np.dot(W12 , [2,2])
b13 = -np.dot(W13 , [-2,4])
b14 = -np.dot(W14 , [0,-2])
b1 = [[b11],[b12],[b13],[b14]]
W2 = [1,1,1,1]
b2 = -3.5

xp=np.linspace(-6,6)
yp=np.linspace(-6,6)

for x in xp:
    for y in yp:
        a1=np.dot(W1,[[x],[y]])+b1
        for i in range(len(a1)):
            a1[i]=hardlim(a1[i])
        a2=hardlim(np.dot(W2,a1)+b2)
        if a2==1:
            plt.plot(x,y,'bo')
        else:
            plt.plot(x,y,'ro')



plt.show()
