import numpy as np
import matplotlib.pyplot as plt

a0 = 2
v0 = 0
d0 = 0

dt = 0.2
stop_time = 10
start_time = 0 #start time
step = 1 
total_steps = int((stop_time-start_time)/dt)

time = np.linspace(start_time,stop_time,total_steps+1)

veular = np.zeros(total_steps+1)
vrk4 = np.zeros(total_steps+1)
d = np.zeros(total_steps+1)
# a = np.full(total_steps+1,a0)
a = np.sin(time)
cosv = -np.cos(time)+1

veular[0] = v0
vrk4[0] = v0
d[0] = d0

def fsquare(t,a):
    1
    

# def EularMethod(f,to_int,integralprev):#you are here
#     integral = integralprev + to_int*dt
#     return integral

# def RK4Solver(f,to_int,integralprev):
#     k1 = to_int[step-1]
#     k2 = (to_int[step]+to_int[step-1])/2
#     k3 = (to_int[step]+to_int[step-1])/2
#     k4 = to_int[step]
#     kmean = (k1+2*k2+2*k3+k4)/6
#     integral = integralprev + kmean*dt
#     return integral 


# while(step <= total_steps):
#     v[step] = EularMethod(dt,a[step],v[step-1])
#     d[step] = EularMethod(dt,v[step],d[step-1])
#     vrk4[step] = RK4Solver(step,a,vrk4[step-1])

#     step+=1

# plt.figure(figsize=(15,10))

# # plt.plot(time, a, label="Acceleration a(t)")
# plt.plot(time, v, label="Velocity v(t)")
# # plt.plot(time, d, label="postition d(t)")
# plt.plot(time, cosv, label="actual v v(t)")
# error = cosv - v
# plt.plot(time, error, label="error eular v v(t)")
# plt.plot(time, vrk4, label="v rk4 v(t)")
# errorrk4 = cosv - vrk4

# plt.plot(time, errorrk4, label="error rk4 v v(t)")

# plt.xlabel("Time [s]")
# plt.ylabel("Value")
# plt.title("Velocity and Acceleration vs Time")
# plt.legend()
# plt.grid(True)
# plt.show()
