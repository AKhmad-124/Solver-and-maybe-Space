import numpy as np
import matplotlib.pyplot as plt

#### Solver settings
dt = 0.001
stop_time = 3.5
start_time = 0
total_steps = int((stop_time-start_time)/dt)

#### physical constants
mass = 2
b_friction  = 0.2

#### setpoint
Vsp = 60

def run_sim(kp, ki, kd):
    """Run one simulation with given kp, ki, kd. Return time, v, x"""
    ErrPrev = Vsp     # initialize error
    ErrInt = 0.0
    force = 0.0
    ErrDiff_prev = Vsp
    N = 5

    # time and states
    time = np.linspace(start_time, stop_time, total_steps+1)
    states = np.zeros((total_steps+1, 2))  # v, x
    states[0] = [0, 0]  # v0, x0

    def controller(Vsp, Vcurr, dt):
        nonlocal ErrPrev, ErrInt,ErrDiff_prev
        Err = Vsp - Vcurr
        alpha = N*dt / (1 + N*dt)   
        ErrDiff = alpha*((Err - ErrPrev)/dt) + (1-alpha)*ErrDiff_prev
        # ErrDiff = (Err - ErrPrev)/dt
        ErrInt += Err*dt
        force = kp*Err + ki*ErrInt + kd*ErrDiff
        ErrPrev = Err
        return force

    def f(t, y, force):
        v, x = y
        total_force = force - v*b_friction
        dvdt = total_force/mass
        dxdt = v
        return np.array([dvdt, dxdt])

    def RK4Solver(f, y, h, t, force):
        k1 = f(t, y, force)
        k2 = f(t+h/2, y+k1*h/2, force)
        k3 = f(t+h/2, y+k2*h/2, force)
        k4 = f(t+h, y+k3*h, force)
        kmean = (k1+2*k2+2*k3+k4)/6
        return y + kmean*h

    # main loop
    for step in range(total_steps):
        force = controller(Vsp, states[step,0], dt)
        states[step+1] = RK4Solver(f, states[step], dt, time[step], force)

    v = states[:,0]
    x = states[:,1]
    return time, v, x


### sweep for kp
kp_values = np.linspace(0,10,9)
ki_fixed, kd_fixed = 0, 0
plt.figure(figsize=(12,6))
for kp in kp_values:
    time, v, x = run_sim(kp, ki_fixed, kd_fixed)
    plt.plot(time, v, label=f"kp={kp}", linewidth=2)
plt.plot(time, np.full_like(time, Vsp), 'k--', label="Vsp", linewidth=2)
plt.xlabel("Time [s]"); plt.ylabel("Velocity [m/s]")
plt.title("Effect of kp on Controller Response at ki=kd=0")
plt.legend(); plt.grid(True)
plt.show()


# ### sweep for ki
ki_values = np.linspace(0,9,10)
kp_fixed, kd_fixed = 6.25, 0
plt.figure(figsize=(12,6))
for ki in ki_values:
    time, v, x = run_sim(kp_fixed, ki, kd_fixed)
    plt.plot(time, v, label=f"ki={ki}", linewidth=2)
plt.plot(time, np.full_like(time, Vsp), 'k--', label="Vsp", linewidth=2)
plt.xlabel("Time [s]"); plt.ylabel("Velocity [m/s]")
plt.title(f"Effect of ki on Controller Response at kp={kp_fixed} and kd={kd_fixed}")
plt.legend(); plt.grid(True)
plt.show()


### sweep for kd
kd_values = np.linspace(1.95,-1.95,10)
# kd_values = [-1.7]
kp_fixed, ki_fixed = 9, 7
plt.figure(figsize=(12,6))
for kd in kd_values:
    time, v, x = run_sim(kp_fixed, ki_fixed, kd)
    plt.plot(time, v, label=f"kd={kd}", linewidth=2)
plt.plot(time, np.full_like(time, Vsp), 'k--', label="Vsp", linewidth=2)
plt.xlabel("Time [s]"); plt.ylabel("Velocity [m/s]")
plt.title(f"Effect of kd on Controller Response at kp={kp_fixed} and ki={ki_fixed}")
plt.legend(); plt.grid(True)
plt.xlim(0,stop_time)
# plt.ylim(0,np.max(v)+5)
plt.show()
