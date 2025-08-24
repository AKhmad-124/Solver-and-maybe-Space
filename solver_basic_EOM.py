import numpy as np
import matplotlib.pyplot as plt
import time as pytime

a0 = 2
v0 = 0
d0 = 0

dt = 0.5
stop_time = 25000
start_time = 0 #start time
step = 0
total_steps = int((stop_time-start_time)/dt)
time = np.linspace(start_time,stop_time,total_steps+1)

####physics
force = 20
mass = 2
b_friction  = 0.2
####

yeular = np.zeros(total_steps+1)
vrk4 = np.zeros(total_steps+1)
drk4 = np.zeros(total_steps+1)

states = np.zeros((total_steps+1,2))

yeular[0] = 0
vrk4[0] = 0
drk4[0] = 0
states[0] = [0,0]

def f(t,y):
    v,x = y
    total_force = force - v*b_friction
    dvdt = total_force/mass
    dxdt = v
    return np.array([dvdt,dxdt])

    

def EularMethod(f,y,h,t):
     return y + h*f(t,y)

def RK4Solver(f,y,h,t):
    k1 = f(t,y)
    k2 = f(t+h/2,y+k1*h/2)
    k3 = f(t+h/2,y+k2*h/2)
    k4 = f(t+h,y+k3*h)
    kmean = (k1+2*k2+2*k3+k4)/6
    return  y + kmean*h
start_timer = pytime.time()

while(step+1 <= total_steps):

    # yeular[step+1] = EularMethod(f,yeular[step],dt,time[step])
    states[step+1] = RK4Solver(f,states[step],dt,time[step])
    # print(states)
    # vrk4[step+1] = state[0]
    # drk4[step+1] = state[1]
    step+=1
# print(yrk4)
# print(yrk4,time)
t_dense = np.linspace(start_time, stop_time, 1000)

# y_exact = np.exp(np.sin(t_dense))

# y_to_size = np.exp(np.sin(time))
plt.figure(figsize=(15,8))
v = states[:,0]
# print(v)
x = states[:,1]
print("here")
print("--- %s seconds ---" % (pytime.time() - start_timer))
# plt.plot(time, a, label="Acceleration a(t)")
plt.plot(time, v, label="v ")
plt.xlabel("Time [s]")
plt.ylabel("Value")
plt.title("rk4 vs exact vs eular")
plt.legend()
plt.grid(True)

plt.figure(figsize=(15,8))
plt.plot(time, x, label="d ")
diff = vrk4 - yeular
# plt.plot(time, diff, label="diff ")
# plt.plot(t_dense, y_exact, label="exact ")
# plt.plot(time, d, label="postition d(t)")
# errorRK4 = y_to_size - yrk4 
# errorEular = y_to_size - yeular 

# plt.plot(time, errorEular, label="eular error")
# plt.plot(time, errorRK4, label="rk4 error ")

plt.xlabel("Time [s]")
plt.ylabel("Value")
plt.title("rk4 vs exact vs eular")
plt.legend()
plt.grid(True)
plt.show()



