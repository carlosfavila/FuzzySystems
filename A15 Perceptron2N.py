import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1

# patterns 
P1=[]
P2=[]
for i in range(40):
    P1.append(np.random.randint(-2,3))
    P2.append(np.random.randint(-2,3))

P=np.array([P1, P2]) #matrix of patterns
t1=[]
t2=[]

for i in range(10):
    t1.append(0)
    t2.append(0)
for i in range(10):
    t1.append(0)
    t2.append(1)
for i in range(10):
    t1.append(1)
    t2.append(0)
for i in range(10):
    t1.append(1)
    t2.append(1)

t=np.array([t1,t2]) #matrix of targets

print(P)
print(t)


[R,N]=P.shape 
print(R)
print(N)
S=2 # number of neurons
epoch=10 # number of epochs


W=np.random.rand(S,R) # matrix of weights
b=np.random.rand(S,1) # matrix of bias

print(P[:,39])
print(P[:,38])
print(P[:,37])
print(P[:,0])
print(P[:,1])
print(P[:,2])


"""
for i in range(epoch):
    for j in range(N):
        x=P[:,j]
        l=np.dot(W,x)
        l1=l[0]
        l2=l[1]
        l=np.array([[l1],[l2]])
        y=(l+b)
        l=t[:,j]
        l1=l[0]
        l2=l[1]
        tr=np.array([[l1],[l2]])
        e=tr-y
        W=W+np.dot(e.T,x)
        b=b+e

l=[]
x = np.arange(-3,3.1,0.1)
for i in x:
    for j in x:
        l=np.dot(W,[i,j])
        l1=l[0]
        l2=l[1]
        l=np.array([[l1],[l2]])
        y=l+b

        for k in range(len(y)):
            y[k]=hardlim(y[k])

        if y[0]==0 and y[1]==0:
            plt.plot(i,j,'ro',markersize=1)
        elif y[0]==0 and y[1]==1:
            plt.plot(i,j,'bo',markersize=1)
        elif y[0]==1 and y[1]==0:
            plt.plot(i,j,'go',markersize=1)
        else:
            plt.plot(i,j,'yo',markersize=1)"""
plt.show()