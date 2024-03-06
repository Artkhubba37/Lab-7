import time as tm
import numpy as np
from matplotlib import pyplot as mp
massive1=np.random.randint(0,10,(1000,1000))
massive2=np.random.randint(0,10,(1000,1000))
umnojenie=np.multiply(massive1,massive2)
print(tm.perf_counter_ns())
print(umnojenie)

T2data = np.genfromtxt("data2.csv",delimiter=",",usecols=(0),skip_header=1,dtype=float)
t2dataindex=[]
for i in range(1,len(T2data)+1):
    t2dataindex.append(i)
#print(T2data)
#print(t2dataindex)
#print(len(T2data),len(t2dataindex))

mp.plot(t2dataindex,T2data)
mp.title("Данные о кислотности из файла data2.csv")
mp.xlabel("номер образца")
mp.ylabel("кислотность")
mp.show()

x=np.linspace(-2*np.pi,2*np.pi,100)
y=np.sin(x)*np.cos(x)
z=np.sin(x)*np.cos(x)

fig = mp.figure()
ax = mp.axes(111,projection="3d")
mp.title("задание 3")
mp.xlabel("x")
mp.ylabel("y")
ax.plot(x,y,z)
mp.show()


