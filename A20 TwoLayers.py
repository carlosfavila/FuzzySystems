import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1


# patterns
P=np.array([[0,1,0,1], [0,1,1,0]]) #matrix of patterns

#Yl1=-x+1/2
#Yw11=x

#Yl2=-x+3/2
#Yw12=x

# so, we want the line of the weight 1 points at the middle of the two lines
# proposing x = 0.5, with Yw11=x we get Yw11 = 0.5

# and we also want the line of the weight 2 points at the middle of the two lines
# proposing x = -0.5, with Yw12=x we get Yw12 = -0.5 

w11=[0.5,0.5]
w12=[-0.5,-0.5]

#for point on the first limit line (neuron 1) P1[0.5,0]
b11=-np.dot(w11,[0.5,0])

#for point on the second limit line (neuron 2) P2[1.5,0]
b12=-np.dot(w12,[1.5,0])

W1=[w11,w12]
B1=[[b11],[b12]]

W2=[1,1] # both neurons have the same weight for the second layer

#W*P+b>=0 MINIMUM CONDITION TO GET '1'
#[1,1]*[[1],[1]]+b>=0
#2+b>=0
#b>=-2

#W*P+b<0 MAXIMUM CONDITION TO GET '0'
#[1,1]*[[0],[1]]+b<0 or [1,1]*[[1],[0]]+b<0
#1+b<0 
#b<-1

# so, our bias is between -2 and -1
# we propose b=-1.5

B2=-1.5 

xp=np.arange(-0.5,1.2,0.1)
yp1=-xp+0.5
yp2=-xp+1.5

yp=np.arange(-0.5,2,0.1)

xw1=np.linspace(0,0.5)
yw1=xw1

xw2=np.linspace(0,-0.5)
yw2=xw2

plt.figure(1)


for x in xp:
    for y in yp:
        a1=np.dot(W1,[[x],[y]])+B1
        for i in range(len(a1)):
            a1[i]=hardlim(a1[i])
        a2=np.dot(W2,a1)+B2
        if a2>=0:
            plt.plot(x,y,'bo')
        else:
            plt.plot(x,y,'ro')

plt.plot(P[0][0],P[1][0],'go',P[0][1],P[1][1],'go',P[0][2],P[1][2],'ko',P[0][3],P[1][3],'ko',xp,yp1,'k',xp,yp2,'k',xw1,yw1,'k',xw2,yw2,'k')
plt.grid(True)

plt.show()
