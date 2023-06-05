import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1


#FIRST WE'RE DOING THE TRIANGLE.

#proposing 3 points as the triangle vertices
#P1=[2,2]
#P2=[1,1]
#P3=[3,1]

#so, for this we have 3 lines (neurons):
# Yl1 - 2= (2-1/2-1)*(X-2) -> Yl1 = X
# Yl2 - 2= (2-1/2-3)*(x-2) -> Yl2 = -X+4

#So, the weight line equations are:
# Yw11 = -X
# Yw12 = X
# Yw13 = inf

# so, we want the line of the weight 1 points at the middle of the three lines
# proposing x = 1, with Yw11=-x we get Yw11 = -1

# and we also want the line of the weight 2 points at the middle of the thre lines
# proposing x = -1, with Yw12=x we get Yw12 = -1

# and we also want the line of the weight 3 points at the middle of the thre lines
# in this case, the weight 3 is a vertical line, so we can propose x=0 and in Yw13=1

w11=[1,-1]
w12=[-1,-1]
w13=[0,1]

#NOW WE'RE DOING THE SQUARE
#P1=[1,1]
#P2=[3,1]
#P3=[3,0]
#P4=[1,0]

#so, for this we have 4 lines (neurons):
# Xl4 = 1 (vertical line)
# Xl5 = 3 (vertical line)
# Yl6 = 0
# Yl7 = 1

#So, the weights are:
w14=[1,0]
w15=[-1,0]
w16=[0,1]
w17=[0,-1]

#CALCULATING THE BIAS's
#for point on the first limit line (neuron 1) P1[0,0]
b11=-np.dot(w11,[0,0])

#for point on the second limit line (neuron 2) P2[0,4]
b12=-np.dot(w12,[0,4])

#for point on the third limit line (neuron 3) P3[0,1]
b13=-np.dot(w13,[0,1])

#for point on the fourth limit line (neuron 4) P4[1,1]
b14=-np.dot(w14,[1,1])

#for point on the fifth limit line (neuron 5) P5[3,1]
b15=-np.dot(w15,[3,1])

#for point on the sixth limit line (neuron 6) P6[2,0]
b16=-np.dot(w16,[2,0])

#for point on the seventh limit line (neuron 7) P7[2,1]
b17=-np.dot(w17,[2,1])


W1=[w11,w12,w13,w14,w15,w16,w17]
B1=[[b11],[b12],[b13],[b14],[b15],[b16],[b17]]


#2nd layer AND
W2=[[1,1,1,0,0,0,0], # this line is the sum of the weights of the triangle
    [0,0,0,1,1,1,1]] # this line is the sum of the weights of the square

#W*P+b>=0 MINIMUM CONDITION TO GET '1'
#[1,1,1,0,0,0,0]*[[a1],[a2],[a3],[a4],[a5],[a6],[a7]]+b>=0
#[0,0,0,1,1,1,1]

#W*P+b<0 MAXIMUM CONDITION TO GET '0'
#[1,1,1,0,0,0,0]*[[a1],[a2],[a3],[a4],[a5],[a6],[a7]]+b<0
#[0,0,0,1,1,1,1]

# for the triangle
#[1,1,1]*[[a1],[a2],[a3]]+b>=0 # to get '1'
#[1,1,1]*[[1],[1],[1]]+b>=0
# 3+b>=0 -> b>=-3
#[1,1,1]*[[a1],[a2],[a3]]+b<0 # to get '0'
#[1,1,1]*[[1],[1],[0]]+b<0 
# 2+b<0 -> b<-2
# -3<=b<-2 -> b=-2.5

# for the square
#[1,1,1,1]*[[a4],[a5],[a6],[a7]]+b>=0 # to get '1'
#[1,1,1,1]*[[1],[1],[1],[1]]+b>=0
# 4+b>=0 -> b>=-4
#[1,1,1,1]*[[a4],[a5],[a6],[a7]]+b<0 # to get '0'
#[1,1,1,1]*[[1],[1],[1],[0]]+b<0
# 3+b<0 -> b<-3
# -4<=b<-3 -> b=-3.5

B2=[[-2.5],[-3.5]]

#----------------------------------------3rd layer OR

W3=[1,1] # both inputs have the same weight (same importance)

#W*P+b>=0 MINIMUM CONDITION TO GET '1'
#[1,1]*[[1],[0]]+b>=0 or [1,1]*[[0],[1]]+b>=0
# 1+b>=0 -> b>=-1

#W*P+b<0 MAXIMUM CONDITION TO GET '0'
#[1,1]*[[0],[0]]+b<0 
# 0+b<0 -> b<0

#-1<=b<0 -> b=-0.5

B3=[-0.5]


xl1=np.arange(1,2.1,0.1)
yl1=xl1

xl2=np.arange(2,3.1,0.1)
yl2=-xl2+4

yl3=[]
xl3=np.arange(1,3.1,0.1)
for i in range(len(xl3)):
    yl3.append(1)

xp=np.arange(0,4,0.1)
yp=np.arange(0,2.5,0.1)

for x in xp:
    for y in yp:
        a1=np.dot(W1,[[x],[y]])+B1
        for i in range(len(a1)):
            a1[i]=hardlim(a1[i])
        a2=np.dot(W2,a1)+B2
        for i in range(len(a2)):
            a2[i]=hardlim(a2[i])
        a3=hardlim(np.dot(W3,a2)+B3)
        
        if a3==1:
            plt.plot(x,y,'bo')
        else:
            plt.plot(x,y,'ro')

plt.plot(xl1,yl1,'k',xl2,yl2,'k',xl3,yl3,'k')
plt.axvline(x=1, ymin=0.0, ymax=0.5, color='k')
plt.axvline(x=3, ymin=0.0, ymax=0.5, color='k')
plt.show()
