import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1

#proposing 3 points as the triangle vertices
#P1=[2,4]
#P2=[4,4]
#P3=[2,1]
#P4=[4,1]

#calculating each line equations
#horizontal lines
#Yl1 = 4
#Yl2 = 1

#vertical lines
#yl3 = if x==2 then -inf<=y<inf else 0 
#yl4 = if x==4 then -inf<=y<inf else 0

#xu=np.linspace(1,5)
#plt.figure(1)
#plt.plot(xu,4*np.ones(len(xu)),'k',xu,np.ones(len(xu)),'k',2,4,'go',4,4,'go',2,1,'go',4,1,'go')
#plt.axvline(x=2,color='k') 
#plt.axvline(x=4,color='k')
#So, the weight line equations are:
#Yw11 = 


# so, we want the line of the weight 1 points at the middle of the three lines
# proposing x = 0.5, with Yw11=-1/0.8*x we get Yw11 = -(1/0.8)*(0.5)= -0.625

# and we also want the line of the weight 2 points at the middle of the thre lines
# proposing x = -0.5, with Yw12=1/0.4*x we get Yw12 = (1/0.4)*(-0.5)= -1.25

# and we also want the line of the weight 3 points at the middle of the thre lines
# proposing x = -0.5, with Yw13=-1/0.2*x we get Yw13 = -(1/0.2)*(-0.5)= 2.5
"""
w11=[0.5,-0.625]
w12=[-0.5,-1.25]
w13=[-0.5,2.5]

#for point on the first limit line (neuron 1) P1[0,0.8*0+2.6]
b11=-np.dot(w11,[0,2.6])

#for point on the second limit line (neuron 2) P2[5,−0.4*5+6.2]
b12=-np.dot(w12,[5,4.2])

#for point on the third limit line (neuron 3) P3[3,0.2*3+1.4]
b13=-np.dot(w13,[3,2])

W1=[w11,w12,w13]
B1=[[b11],[b12],[b13]]

W2=[1,1,1] # both neurons have the same weight for the second layer

#W*P+b>=0 MINIMUM CONDITION TO GET '1'
#[1,1,1]*[[1],[1],[1]]+b>=0
#3+b>=0
#b>=-3

#W*P+b<0 MAXIMUM CONDITION TO GET '0'
#[1,1,1]*[[0],[1],[0]]+b<0 or [1,1]*[[1],[0],[0]]+b<0 or [1,1]*[[0],[0],[1]]+b<0
#1+b<0 
#b<-1

# so, our bias is between -3 and -1
# we propose b=-2

B2=-2

xl1=np.linspace(-2,3) #First neuron
yl1=0.8*xl1+2.6

xl2=np.linspace(3,8) #Second neuron
yl2=-0.4*xl2+6.2

xl3 = np.linspace(-2,8) #Third neuron
yl3 = 0.2*xl3+1.4

xw1=np.linspace(0,0.5)
yw1=-(1/0.8)*xw1

xw2=np.linspace(0,-0.5)
yw2=(1/0.4)*xw2

xw3=np.linspace(0,-0.5)
yw3=-(1/0.2)*xw3
"""
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

"""
plt.figure(1)

plt.plot(xl1,yl1,'b',xl2,yl2,'b',xl3,yl3,'b',xw1,yw1,'k',xw2,yw2,'k',xw3,yw3,'k')
plt.plot(3,5,'go',-2,1,'go',8,3,'go')
"""

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

"""
plt.plot(xl1,yl1,'k',xl2,yl2,'k',xl3,yl3,'k',xw1,yw1,'k',xw2,yw2,'k',xw3,yw3,'k')
plt.plot(3,5,'go',-2,1,'go',8,3,'go')
plt.grid(True)"""

plt.show()
