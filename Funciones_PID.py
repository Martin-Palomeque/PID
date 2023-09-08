def I(t2,t1,error,ki):
    dt = t2-t1
    return ki*error*dt

def P(kp,error):
    return kp*error

def D(t2,t1,error2,error1,kd):
    dt = t2-t1
    de = error2-error1
    return kd*(de/dt)
