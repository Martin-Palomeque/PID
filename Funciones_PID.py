def I(t2,t1,acumulado,error,ki):
    dt = t2-t1
    acumulado += error*dt
    i = ki*acumulado
    return i,acumulado #Acumulado es necesario para que pueda considerar la evolucion de la funcion sin meter ki en el medio

def P(error,kp):
    return kp*error

def D(t2,t1,error2,error1,kd):
    dt = t2-t1
    de = error2-error1
    return kd*(de/dt)
