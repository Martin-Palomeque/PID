import numpy as np
import matplotlib.pyplot as plt
import time
import serial as ser
import cv2
from tracking import trackTemplate

Kp = 1000
setpoint = 278
t0 = time.time()
seg = 35
cmd = 'a0\n'
posiciones = []
tiempo = []

arduino = ser.Serial('COM6', baudrate=9600, bytesize=ser.EIGHTBITS,parity=ser.PARITY_NONE,stopbits=ser.STOPBITS_ONE, timeout=10)

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
template = cv2.imread("template.png")
limites = [195, 272, 30, 600]

time.sleep(2)

while time.time() - t0 < seg:
    posiciones.append(478 - trackTemplate(vs, template, limites, GRAFICAR=False)[0])
    pos = posiciones[-1]
    tiempo.append(time.time() - t0)
    error = setpoint - pos
    P = Kp*error
    if P > 255:
        arduino.write(bytes(f'a255\n', 'utf-8'))
    elif P < 180:
        arduino.write(bytes(f'a180\n', 'utf-8'))
    else:
        arduino.write(bytes(f'a{int(P)}\n', 'utf-8'))


print(posiciones)

arduino.write(bytes('a0\n', 'utf-8'))
# np.savetxt('posiciones.csv', np.array(posiciones).T, delimiter=',')

fig, ax = plt.subplots()
ax.plot(tiempo, posiciones,color = 'cornflowerblue')
# ax.axhline(hline, color = 'tomato')
plt.grid()
plt.show()

# print(trackTemplate(vs, template, limites, GRAFICAR=False))

time.sleep(2)
arduino.close()