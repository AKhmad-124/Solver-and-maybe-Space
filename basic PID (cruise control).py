import numpy as np
import matplotlib.pyplot as plt
import time as pytime


#### Solver settings
dt = 0.1
stop_time = 2
start_time = 0 #start time
step = 0
total_steps = int((stop_time-start_time)/dt)
####
####physical constants
mass = 2
b_friction  = 0.2
####
#### cotroller variables
kp = 4
ki = 3
kd = 0.1**20
Vsp = 60
ErrPrev = Vsp#to not cause a big change in the first step
ErrInt = 0 
####
####initial values
V0 = 0
d0 = 0
####
#### setting up variables
time = np.linspace(start_time,stop_time,total_steps+1)
states = np.zeros((total_steps+1,2))
states[0] = [V0,d0]#v,x
####
####



def controller(Vsp,Vcurr,dt):
    global ErrPrev , ErrInt
    Err = Vsp - Vcurr
    ErrDiff = (Err-ErrPrev)/dt
    ErrInt = ErrInt + Err*dt
    force = kp*Err + ki*ErrInt + kd*ErrDiff 
    ErrPrev = Err

    return force

def f(t,y):
    v,x = y
    total_force = force - v*b_friction
    dvdt = total_force/mass
    dxdt = v
    return np.array([dvdt,dxdt])

# def EularMethod(f,y,h,t):
#      return y + h*f(t,y)

def RK4Solver(f,y,h,t):
    k1 = f(t,y)
    k2 = f(t+h/2,y+k1*h/2)
    k3 = f(t+h/2,y+k2*h/2)
    k4 = f(t+h,y+k3*h)
    kmean = (k1+2*k2+2*k3+k4)/6
    return  y + kmean*h
start_timer = pytime.time()

################ main loop
while(step+1 <= total_steps):
    force = controller(Vsp,states[step,0],dt)
    states[step+1] = RK4Solver(f,states[step],dt,time[step])
    step+=1

########

v = states[:,0]
x = states[:,1]

print("here")
print("--- %s seconds ---" % (pytime.time() - start_timer))


plt.figure(figsize=(15,8))

# plt.plot(time, a, label="Acceleration a(t)")
plt.plot(time, v, label="V ",linewidth=2.5)
Vsp = np.full_like(time,Vsp)
plt.plot(time, Vsp, label="Vsp ",linewidth=2.5)
Verr = Vsp-v
plt.plot(time, Verr, label="Verr ",linewidth=2.5)
plt.xlabel("Time [s]")
plt.ylabel("m/s")
plt.title("Speed VS time")
plt.legend()
plt.grid(True)
plt.xlim(0,stop_time)
# plt.ylim(np.min(Verr)-5,np.max(v)+5)

plt.figure(figsize=(15,8))
plt.plot(time, x, label="d ")

plt.xlabel("Time [s]")
plt.ylabel("Value")
plt.title("distance VS Time")
plt.legend()
plt.grid(True)
plt.show()



