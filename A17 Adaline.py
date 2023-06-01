import matplotlib.pyplot as plt
import numpy as np


def purelin(x):
    return x    

# patterns 
P=np.array([[1,-1,0], [2,2,-1]]) #matrix of patterns
t = np.array([1,-1, 1])
print(P)
[R,N]=P.shape 
S=1 # number of neurons
epoch=10 # number of epochs

#WEIGHTS AND BIAS
W=np.random.rand(S,R) # matrix of weights
b=np.random.rand(S,1) # matrix of bias

R=np.dot(P,P.T) 
eigen=np.linalg.eigvals(R)
alpha=1/(4*max(eigen)) 

for i in range(epoch):
    for j in range(N):
        x=P[:,j]
        aa=purelin((np.dot(W,x)+b))
        e=t[j]-aa
        W=W+alpha*e*x
        b=b+alpha*e

x = np.arange(-3,3.1,0.1)
plt.figure(1)
for i in x:
    for j in x:
        y=(np.dot(W,[i,j])+b)
        y=purelin(y)
        if y==0:
            plt.plot(i,j,'ro',markersize=1)
        else:
            plt.plot(i,j,'bo',markersize=1)   
plt.show()

