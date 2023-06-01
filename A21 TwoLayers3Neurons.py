import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1

#proposing 3 points as the triangle vertices
#P1=[3,5]
#P2=[-2,1]
#P3=[8,3]

#calculating each line equation
#Yl1 = 0.8*xl1+2.6
#Yl2 = −0.4x+6.2
#yl3 = 0.2x+1.4

#So, the weight line equations are:
#Yw11=-1/0.8*x
#Yw12=1/0.4*x
#Yw13=-1/0.2*x


# so, we want the line of the weight 1 points at the middle of the three lines
# proposing x = 0.5, with Yw11=-1/0.8*x we get Yw11 = -(1/0.8)*(0.5)= -0.625

# and we also want the line of the weight 2 points at the middle of the thre lines
# proposing x = -0.5, with Yw12=1/0.4*x we get Yw12 = (1/0.4)*(-0.5)= -1.25

# and we also want the line of the weight 3 points at the middle of the thre lines
# proposing x = -0.5, with Yw13=-1/0.2*x we get Yw13 = -(1/0.2)*(-0.5)= 2.5

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

xw2=np.linspace(0,-0.2)
yw2=(1/0.4)*xw2

xw3=np.linspace(0,-0.2)
yw3=-(1/0.2)*xw3

plt.figure(1)

plt.plot(xl1,yl1,'b',xl2,yl2,'b',xl3,yl3,'b',xw1,yw1,'k',xw2,yw2,'k',xw3,yw3,'k')
plt.plot(3,5,'go',-2,1,'go',8,3,'go')

xp=np.linspace(-3,9)
yp=np.linspace(-1,6)
for x in xp:
    for y in yp:
        a1=np.dot(W1,[[x],[y]])+B1
        for i in range(len(a1)):
            a1[i]=hardlim(a1[i])
        a2=np.dot(W2,a1)+B2
        if a2==1:
            plt.plot(x,y,'bo')
        else:
            plt.plot(x,y,'ro')

plt.plot(xl1,yl1,'k',xl2,yl2,'k',xl3,yl3,'k',xw1,yw1,'k',xw2,yw2,'k',xw3,yw3,'k')
plt.plot(3,5,'go',-2,1,'go',8,3,'go')
plt.grid(True)

plt.show()

#280601
