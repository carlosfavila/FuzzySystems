import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if x >= 0:
        return 1
    else:
        return 0
    
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

# original points of the pattern
P1=[1,1]
P2=[2,2]
P3=[-1,1]
P4=[-2,2]
P5=[-1,-1]
P6=[0,-2]
P7=[1,-1]
P8=[2,-1]
 #proposed the points of the limit lines (neurons)
 # For the first neuron P1(0.5,0) and P2(0,1)
x1=0.5
y1=0
x2=0
y2=1
m1=slope(x1,y1,x2,y2)

# For the second neuron P3(0,-0.2) and P4(0.5,0)
x3=0
y3=-0.2
x4=0.5
y4=0
m2=slope(x3,y3,x4,y4)

#slopes for the w's for each neuron
w1=-1/m1
w2=-1/m2

#equation of the w's for each neuron
#y1=(-1/m1)*x   
#y2=(-1/m2)*x

#proposing a value of x < 1
x=0.5
y1=w1*x
y2=w2*x

#Soooo....
W1=[x , y1]
W2=[x , y2]

#calculating b1 nd b2
# the proposed poin of the limit line in neuron 1
# P1(0.5,0)
PointN1=[0.5,0]
b1=-(W1[0]*PointN1[0]+PointN1[1]*W1[1])

# the proposed poin of the limit line in neuron 1
# P3(0,-0.2)
PointN2=[0,-0.2]
b2=-(W2[0]*PointN2[0]+PointN2[1]*W2[1])

#so... 
B=[b1 , b2]


X=np.arange(-3,3,0.2)
Y=np.arange(-3,3,0.2)

fig1=plt.figure(1)

for x in X:
    for y in Y:
        a1=hardlim(W1[0]*x+W1[1]*y+B[0])
        a2=hardlim(W2[0]*x+W2[1]*y+B[1])
        if a1==1 and a2==1:
            plt.plot(x,y,'ro')
        elif a1==1 and a2==0:
            plt.plot(x,y,'bo')
        elif a1==0 and a2==1:
            plt.plot(x,y,'go')
        else:
            plt.plot(x,y,'yo')

limline1=[]
limline2=[]
xp1=np.arange(0,W1[0],0.002)
xp2=np.arange(0,W2[0],0.002)

XP=np.arange(-1,2.1,0.1) # just to reduce the size of the plot of Neuron 1
for x in XP:
    limline1.append(-b1/W1[1]-W1[0]/W1[1]*x)
XP2=np.arange(-3,3,0.1) # just to reduce the size of the plot of Neuron 2
for x in XP2:
    limline2.append(-b2/W2[1]-W2[0]/W2[1]*x)

wp1=[]
wp2=[]
for x in xp1:
    wp1.append(w1*x)

for x in xp2:
    wp2.append(w2*x)

plt.plot(XP,limline1,'k-',XP2,limline2,'k-',xp1,wp1,'k-',xp2,wp2,'k-',P1[0],P1[1],'ko',P2[0],P2[1],'ko',P3[0],P3[1],'ko',P4[0],P4[1],'ko',P5[0],P5[1],'ko',P6[0],P6[1],'ko',P7[0],P7[1],'ko',P8[0],P8[1],'ko')
plt.xlabel('P1')
plt.ylabel('P2')   
plt.grid(True) 

plt.show()