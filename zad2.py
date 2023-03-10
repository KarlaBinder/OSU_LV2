import numpy as np
import matplotlib.pyplot as plt

arra= np.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=float)

#Na koliko je osoba izvršeno mjerenje a)
size=len(arra)
print('Izvrseno je mjenjenja na:', size)
size=int(size)

#Odnos visine i tezine b)
x=np.array(arra[:,1])
y=np.array(arra[:,2])
plt.title('Odnos svih visina i tezina')
plt.scatter(x,y,alpha=0.5,c='b', linewidths=1)
plt.show()

#Za svaku 50 osobu c)
x1=x[::50]
y1=y[::50]
plt.title('Odnos visine i tezine svake 50 osobe')
plt.scatter(x1,y1,alpha=0.5,c='y', linewidths=1)
plt.show()

#Min,Max i srednja vrijednost d)
print('Min', x.min())
print('Max:', x.max())
print('Srednja vrijednost:', x.mean())


#Min,Max i srednje vrijednost po spolovima e)
male=(arra[:,0]==1)
female=(arra[:,0]==0)

print('Min muski:', arra[male,1].min())
print('Max muski:', arra[male,1].max())
print('Srednja vrijednost muski:', arra[male,1].mean())

print('Min zene:', arra[female,1].min())
print('Max zene:', arra[female,1].max())
print('Srednja vrijednost zene:', arra[female,1].mean())