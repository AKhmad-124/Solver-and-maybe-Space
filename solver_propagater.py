import numpy as np
import matplotlib.pyplot as plt

a0 = 2
v0 = 0
d0 = 0

dt = 0.2
stop_time = 3000
start_time = 0 #start time
step = 0
total_steps = int((stop_time-start_time)/dt)
time = np.linspace(start_time,stop_time,total_steps+1)


yeular = np.zeros(total_steps+1)
yrk4 = np.zeros(total_steps+1)

yeular[0] = 1
yrk4[0] = 1

def f(t,y):
    return np.cos(t)*y

def EularMethod(f,y,h,t):
     return y + h*f(t,y)

def RK4Solver(f,y,h,t):
    k1 = f(t,y)
    k2 = f(t+h/2,y+k1*h/2)
    k3 = f(t+h/2,y+k2*h/2)
    k4 = f(t+h,y+k3*h)
    kmean = (k1+2*k2+2*k3+k4)/6
    return  y + kmean*h

while(step+1 <= total_steps):

    yeular[step+1] = EularMethod(f,yeular[step],dt,time[step])
    yrk4[step+1] = RK4Solver(f,yrk4[step],dt,time[step])
    
    step+=1
print(yrk4)
# print(yrk4,time)
t_dense = np.linspace(start_time, stop_time, 1000)

y_exact = np.exp(np.sin(t_dense))

y_to_size = np.exp(np.sin(time))
plt.figure(figsize=(15,8))

# plt.plot(time, a, label="Acceleration a(t)")
plt.plot(time, yeular, label="eular ")
plt.plot(time, yrk4, label="rk4 ")
plt.plot(t_dense, y_exact, label="exact ")
# plt.plot(time, d, label="postition d(t)")
errorRK4 = y_to_size - yrk4 
errorEular = y_to_size - yeular 

plt.plot(time, errorEular, label="eular error")
plt.plot(time, errorRK4, label="rk4 error ")

plt.xlabel("Time [s]")
plt.ylabel("Value")
plt.title("rk4 vs exact vs eular")
plt.legend()
plt.grid(True)
plt.show()



