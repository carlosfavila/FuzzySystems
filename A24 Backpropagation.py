import  numpy as np
import matplotlib.pyplot as plt
import random as rand
def logsig(x):
    return 1/(1+np.exp(-x))

p=np.arange(-2,2,0.1)
a=np.pi/4*p
targets=1+np.sin(a)

S1=2 #Number of neurons in the first layer
S2=1 #Number of neurons in the second layer

w1=rand.randrange(S1,1)
b1=rand.randrange(S1,1)
w2=rand.randrange(S2,S1)
b2=rand.randrange(S2,1)

alpha=0.1

epoch=1000

# TRAINING
for x in range(epoch):
    for y in range(len(p)):
        a1=logsig(w1*p[y]+b1)
        a2=logsig(w2*a1+b2)
        e=targets[y]-a2
        delta2=e*a2*(1-a2)
        #Calculate the sentitivities backwards
        delta1=a1*[[(1-a1)*a1 , 0],[0,(1-a2)*a2]]*w2.T*delta2


        #Update the weights and biases
        w2=w2-alpha*delta2*a1.T
        b2=b2-alpha*delta2

        w1=w1-alpha*delta1*p[y].T
        b1=b1-alpha*delta1
