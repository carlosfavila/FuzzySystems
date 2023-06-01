import matplotlib.pyplot as plt
import numpy as np

def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1

# patterns 
P=np.array([[1,-1,0], [2,2,-1]]) #matrix of patterns
t = np.array([1,0, 0])
print(P)
[R,N]=P.shape 
S=1 # number of neurons
epoch=10 # number of epochs

W=np.random.rand(S,R) # matrix of weights
b=np.random.rand(S,1) # matrix of bias

for i in range(epoch):
    for j in range(N):
        x=P[:,j]
        y=(np.dot(W,x)+b)
        y=hardlim(y)
        #Percetron Training 
        e=t[j]-y
        W=W+e*x
        b=b+e

x = np.arange(-3,3.1,0.1)
plt.figure(1)
for i in x:
    for j in x:
        y=(np.dot(W,[i,j])+b)
        y=hardlim(y)
        if y==0:
            plt.plot(i,j,'ro',markersize=1)
        else:
            plt.plot(i,j,'bo',markersize=1)   
plt.show()

