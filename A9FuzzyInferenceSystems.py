import  matplotlib.pyplot  as  plt 
import  numpy  as  np 
import skfuzzy as fuzz


# FIRST FIGURE
#Create Universe lists
X=list(np.arange(1,10,0.1))
Y=list(np.arange(1,10,0.1))
Z=list(np.arange(1,10,0.1))

#Fixes the Universe lists
for i in range(len(X)):
  X[i]=round(X[i],1)
  Y[i]=round(Y[i],1)
  Z[i]=round(Z[i],1)

#Ask for the universe's value 
x=float(input("Introduce a X value: "))
y=float(input("Introduce a y value: "))

#finds the index of the universe where the input value is
xi=X.index(x)
yi=Y.index(y)


A1=[]
A2=[]
B1=[]
B2=[]
C1=[]
C2=[]

#create membership functions
for k in X:                                                                     
  A1.append(1/(1+np.exp(3*(k-5))))
  A2.append(1/(1+np.exp(-3*(k-5))))

for k in Y:
  B1.append(np.exp((-1/2)*((k-2.5)/2)**2))
  B2.append(np.exp((-1/2)*((k-7.5)/2)**2))
for k in Z:
  C1.append(1/(1+np.exp(3*(k-5))))
  C2.append(np.exp((-1/2)*((k-7.5)/2)**2))

#lists from the input value to the end of the universe
uxvals=X[xi:]
uyvals=Y[yi:]

valA1=[]
valA2=[]
valB1=[]
valB2=[]

#create a list of the same value to graphic a line
for k in range(len(uxvals)):
  valA1.append(A1[xi])
  valA2.append(A2[xi])

for j in range(len(uyvals)):
  valB1.append(B1[yi])
  valB2.append(B2[yi])

# Fuzzy Inference System RULES
# First and Second Step
l1=min(A1[xi],B1[yi])
l2=min(A1[xi],B2[yi])
l3=min(A2[xi],B1[yi])
l4=min(A2[xi],B2[yi])

#Third Step
la=max(l1,l2)
lb=max(l3,l4)

#Fourth and Fifth Step
C1X=[min(la,C1[k]) for k in range(len(Z))]
C2X=[min(lb,C2[k]) for k in range(len(Z))]

#Sixth Step
finalCL=[max(C1X[k],C2X[k]) for k in range(len(Z))]
#print(finalCL)

fmFCL=np.asarray(finalCL)
#print(fmFCL)
fZ=np.asarray(Z)
cent=fuzz.defuzz(fZ,fmFCL,'centroid')


#FIGURE 1
fig=plt.figure(1)
fig.supylabel('Membership Degree')
fig.suptitle("Fuzzy Inference System")

plt.subplot(3,1,1)
plt.plot(X,A1,X,A2)
plt.title("A")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["A1=High Temperature","A2=Low Temperature"])

plt.subplot(3,1,2)
plt.plot(Y,B1,Y,B2)
plt.title("B")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["B1=Low Humidity","B2=High Humidity"])

plt.subplot(3,1,3)
plt.plot(Z,C1,Z,C2)
plt.title("C")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["C1=Low Speed","C2=High Speed"])
#plt.show()

#-------------------------------------------------------------------------------

#SECOND FIGURE
#FIGURE 2
fig2=plt.figure(2)
fig2.supylabel('Membership Degree')
fig2.suptitle("Fuzzy Inference System Rules")

plt.subplot(4,3,1)
plt.plot(X,A1,'#6b0e46',uxvals,valA1,'--k',x,A1[xi],"-s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["A1"])

plt.subplot(4,3,2)
plt.plot(Y,B1,"#104b51",uyvals,valB1,'--k',y,B1[yi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["B1"])

plt.subplot(4,3,3)
plt.plot(Z,C1,"#bc5090",Z,[la for i in range(len(Z))],"--k",Z,C1X,'x')
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["C1"])

plt.subplot(4,3,4)
plt.plot(X,A1,"#6b0e46",uxvals,valA1,'--k',x,A1[xi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["A1"])

plt.subplot(4,3,5)
plt.plot(Y,B2,"#ffa600",uyvals,valB2,'--k',y,B2[yi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["B2"])

plt.subplot(4,3,6)
plt.plot(Z,C1,"#bc5090",Z,[la for i in range(len(Z))],"--k",Z,C1X,'x')
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["C1"])

plt.subplot(4,3,7)
plt.plot(X,A2,"#aec200",uxvals,valA2,'--k',x,A2[xi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["A2"])

plt.subplot(4,3,8)
plt.plot(Y,B1,"#104b51",uyvals,valB1,'--k',y,B1[yi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["B1"])

plt.subplot(4,3,9)
plt.plot(Z,C2,"#50fdfd",Z,[lb for i in range(len(Z))],"--k",Z,C2X,'x')
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["C2"])

plt.subplot(4,3,10)
plt.plot(X,A2,"#aec200",uxvals,valA2,'--k',x,A2[xi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["A2"])

plt.subplot(4,3,11)
plt.plot(Y,B2,"#ffa600",uyvals,valB2,'--k',y,B2[yi],"s")
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["B2"])

plt.subplot(4,3,12)
plt.plot(Z,C2,"#50fdfd",Z,[lb for i in range(len(Z))],"--k",Z,C2X,'x')
plt.xlabel("Universe")
plt.grid(True)
plt.legend(["C2"])
#plt.show()

#-------------------------------------------------------------------------------
fig3=plt.figure(3)
plt.plot(Z,C1,"#bc5090",Z,C2,"#50fdfd",
         Z,C1X,'k',
         Z,C2X,'y',
         Z,finalCL,'x')
plt.axvline(cent, linewidth=0.5, color='m', label='Centroid')
plt.title("Fuzzy Inference Systems")
plt.ylabel("Membership Degree")
plt.xlabel("Universe ")
plt.grid(True)
plt.show()