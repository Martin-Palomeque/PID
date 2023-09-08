import numpy as np
import matplotlib.pyplot as plt
import serial as ser
import cv2
import time
from tracking import trackTemplate
from Funciones_PID import P,I,D


ki = 1
kp = 1
kd = 1
setpoint = 200
t0 = time.time()
seg = 30
cmd = 'a150\n' #Puede ser 0, es simplemente el estado default de poder del arduino. Un valor no nulo permite reducir el tiempo de respuesta al inicio de la prueba, siempre que este no haga levitar el vaso
posiciones = []
tiempo = []
tubo_en_pixel = 478 #Largo en pixeles que tiene el tubo
arduino = ser.Serial('COM6', baudrate=9600, bytesize=ser.EIGHTBITS,
                     parity=ser.PARITY_NONE,stopbits=ser.STOPBITS_ONE,
                       timeout=10)
vs = cv2.VideoCapture(0,cv2.CAP_DSHOW)
template = cv2.imread('template.png')
limites = [] #Limites del tubo
time.sleep(2) #Tiempo necesario para que no le lleguen comandos muy rapido al arduino y se joda todo

integral = 0
error = []
señal = [] #Para guardar la evolucion de la señal mandada

while time.time() - t0 < seg:
    if len(tiempo) < 1: #En la primera iteracion no puede calcular I ni D
        posiciones.append(tubo_en_pixel - trackTemplate(vs,template,limites,GRAFICAR=False)[0])
        pos = posiciones[-1]
        tiempo.append(time.time() - t0)
        error.append(setpoint - pos)
        P = P(error[-1],kp)
        if P > 255:
            arduino.write(bytes(f'a255\n', 'utf-8'))
        elif P < 180:
            arduino.write(bytes(f'a180\n', 'utf-8'))
        else:
            arduino.write(bytes(f'a{int(P)}\n', 'utf-8'))
    else:
        posiciones.append(tubo_en_pixel - trackTemplate(vs, template, limites, GRAFICAR=False)[0])
        pos = posiciones[-1]
        tiempo.append(time.time() - t0)
        error.append(setpoint - pos)
        I,integral = I(tiempo[-2],tiempo[-1],integral,error[-1],ki)
        P = P(error[-1],kp)
        D = D(tiempo[-2],tiempo[-1],error[-2],error[-1],kd)
        PID = P + I + D
        if PID > 255:
            arduino.write(bytes(f'a255\n', 'utf-8'))
        elif PID < 180:
            arduino.write(bytes(f'a180\n', 'utf-8'))
        else:
            arduino.write(bytes(f'a{int(I)}\n', 'utf-8'))

np.savetxt(f'PID-{seg}s-{kp}-{ki}-{kd}.csv', np.array(posiciones).T,setpoint,tubo_en_pixel, delimiter=',')

fig, ax = plt.subplots()
ax.plot(tiempo, posiciones,color = 'cornflowerblue')

plt.grid()
plt.show()

# print(trackTemplate(vs, template, limites, GRAFICAR=False))

time.sleep(2)
arduino.close()