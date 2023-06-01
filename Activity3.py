import numpy as np
import matplotlib.pyplot as plt

#hard limit function in python
def hardlim(x):
    if (x<0).all():
        return 0
    else:
        return 1

p = np.array([[1,-1,0], [2,2,-1]])
T = np.array([[1], [0], [0]])
[R,N] = p.shape
[S,n] = [T.shape[0],1]
W = np.random.rand(S,R) #rand(S,R)
print(W)
b = np.random.rand(S,1) #rand(S,1)
print(b)

epochs = 10
for i in range(epochs):
    for j in range(N):
        a = hardlim(np.dot(W,p[:,j]) + b)
        e = T[j] - a
        W = W + e*p[:,j].T
        b = b + e
        
#Testing
x = np.arange(-3,3.1,0.1)
y = np.arange(-3,3.1,0.1)
for i in x:
    for j in y:
        a = hardlim(np.dot(W,[i,j]) + b)
        if a == 0:
            plt.plot(i,j,'r.',markersize=1)
        else:
            plt.plot(i,j,'b.',markersize=1)

plt.scatter(p[0][0], p[1][0], color='green',marker='o')
plt.scatter(p[0][1], p[1][1], color='magenta',marker='o')
plt.scatter(p[0][2], p[1][2], color='yellow', marker = 'o')

plt.show()