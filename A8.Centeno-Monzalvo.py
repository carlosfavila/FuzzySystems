import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.arange(0, 10, 0.1)
y = np.arange(0, 10, 0.1)
z = np.arange(0, 10, 0.1)

A1 = [1/(1+np.exp(3*(i-5))) for i in x]
A2 = [1/(1+np.exp(-3*(i-5))) for i in x]

B1 = [np.exp((-1/2)*((i-2.5)/2)**2) for i in y]
B2 = [np.exp((-1/2)*((i-7.5)/2)**2) for i in y]

C1 = [1/(1+np.exp(3*(i-5))) for i in z]
C2 = [np.exp((-1/2)*((i-7.5)/2)**2) for i in z]

a = round(float(input("Ingresa el valor en x: ")), 1)
b = round(float(input("Ingresa el valor en y: ")), 1)

rule1 = np.fmin(A1[int(a*10)], B1[int(b*10)])
min1 = a if A1[int(a*10)]<B1[int(b*10)] else b
rule2 = np.fmin(A1[int(a*10)], B2[int(b*10)])
min2 = a if A1[int(a*10)]<B2[int(b*10)] else b
rule3 = np.fmin(A2[int(a*10)], B1[int(b*10)])
min3 = a if A2[int(a*10)]<B1[int(b*10)] else b
rule4 = np.fmin(A2[int(a*10)], B2[int(b*10)])
min4 = a if A2[int(a*10)]<B2[int(b*10)] else b

c1max = np.fmax(rule1, rule2)
c2max = np.fmax(rule3, rule4)

cut1 = np.fmin(C1, np.full(len(C1),c1max))
cut2 = np.fmin(C2, np.full(len(C2),c2max))
finalcut = np.fmax(cut1, cut2)

plt.figure(1)
plt.subplot(311)
plt.plot(x, A1, 'b', linewidth=1.5, label='A1')
plt.plot(x, A2, 'g', linewidth=1.5, label='A2')
plt.legend(loc='best')
plt.grid()

plt.subplot(312)
plt.plot(y, B1, 'k', linewidth=1.5, label='B1')
plt.plot(y, B2, 'y', linewidth=1.5, label='B2')
plt.legend(loc='best')
plt.grid()

plt.subplot(313)
plt.plot(z, C1, 'c', linewidth=1.5, label='C1')
plt.plot(z, C2, 'm', linewidth=1.5, label='C2')
plt.legend(loc='best')
plt.grid()

plt.figure(2)
plt.subplot(431)
plt.plot(x, A1, 'b', linewidth=1.5, label='A1')
plt.plot(a, A1[int(a*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(434)
plt.plot(x, A1, 'b', linewidth=1.5, label='A1')
plt.plot(a, A1[int(a*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(437)
plt.plot(x, A2, 'g', linewidth=1.5, label='A2')
plt.plot(a, A2[int(a*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(4,3,10)
plt.plot(y, A2, 'g', linewidth=1.5, label='A2')
plt.plot(a, A2[int(a*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(432)
plt.plot(y, B1, 'k', linewidth=1.5, label='B1')
plt.plot(b, B1[int(b*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(435)
plt.plot(y, B2, 'k', linewidth=1.5, label='B2')
plt.plot(b, B2[int(b*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(438)
plt.plot(y, B1, 'y', linewidth=1.5, label='B1')
plt.plot(b, B1[int(b*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(4,3,11)
plt.plot(y, B2, 'y', linewidth=1.5, label='B2')
plt.plot(b, B2[int(b*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(433)
plt.plot(z, C1, 'c', linewidth=1.5, label='C1')
plt.plot(min1, C1[int(min1*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(436)
plt.plot(z, C2, 'c', linewidth=1.5, label='C2')
plt.plot(min2, C2[int(min2*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(439)
plt.plot(z, C1, 'm', linewidth=1.5, label='C1')
plt.plot(min3, C1[int(min3*10)], 'ro', markersize=5)
plt.grid()

plt.subplot(4,3,12)
plt.plot(z, C2, 'm', linewidth=1.5, label='C2')
plt.plot(min4, C2[int(min4*10)], 'ro', markersize=5)
plt.grid()

plt.figure(3)
plt.plot(z,C1, 'b', linewidth=1.5, label='C1')
plt.plot(z,C2, 'g', linewidth=1.5, label='C2')
plt.plot(z,cut1, 'y--', linewidth=1.5, label='cut1')
plt.plot(z,cut2, 'k--', linewidth=1.5, label='cut2')
plt.plot(z,finalcut, 'r--', linewidth=1.5, label='finalcut')
plt.axvline(fuzz.defuzz(z,finalcut, 'centroid'), linewidth=0.5, color='m', label='Centroid')
plt.ylabel('Membresia')
plt.xlabel('Universo')
plt.title("Defuzzificacion por el metodo del centroide")
plt.legend(loc='best')
plt.grid()
plt.show()
