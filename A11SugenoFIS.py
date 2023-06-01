import  matplotlib.pyplot  as  plt 
import  numpy  as  np 
import skfuzzy as fuzz



def bell(ini,fin,a,b,c,step):  #--------------------------BELL-----------------------
  u=np.arange(ini,fin,step)
  for i in range(len(u)): 
    u[i]=round(u[i],1) 

  bll=[]

  for k in u:
    bll.append(1/(1+(np.abs((k-c)/a))**(2*b)))

  return([u,bll])

def sigmoid(ini,fin,a,c,step):  #--------------------------SIGMOID-----------------------
  u=np.arange(ini,fin,step)
  for i in range(len(u)): 
    u[i]=round(u[i],1) 

  sgm=[]

  for k in u:
    sgm.append(1/(1+np.exp(-a*(k-c))))

  return([u,sgm])

e=4.5

#----------------creating the MF-------------

error,NB=sigmoid(-20,20,-0.5,-10,0.1)
error,NS=bell(-20,20,2.5,1,-7.5,0.1)
error,C=bell(-20,20,5,1,0,0.1)
error,PS=bell(-20,20,2.5,1,7.5,0.1)
error,PB=sigmoid(-20,20,0.5,10,0.1)

ei=error.index(e)

"""
fig=plt.figure(1)
plt.plot(Universe,NB,Universe,NS,Universe,C,Universe,PS,Universe,PB)
plt.legend(["NB","NS","C","PS","PB"])
plt.show()
"""

#-------------RULES-------------------------

w1=NB[ei]
w2=NS[ei]
w3=C[ei]
w4=PS[ei]
w5=PB[ei]

f1=[]
f2=[]
f3=[]
f4=[]
f5=[]

for k in range(len(error)):
  f1.append(-12)
  f2.append(2*k+8)
  f3.append(0.4*k)
  f4.append(2*k-8)
  f5.append(12)

