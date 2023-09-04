import numpy as np
import matplotlib.pyplot as plt
import time
import serial as ser
import cv2
from tracking import trackTemplate

hline = 200
setpoint = 478 - hline
t0 = time.time()
seg = 80
cmd = 'a0\n'
posiciones = []
tiempo = []
onoff = []

arduino = ser.Serial('COM6', baudrate=9600, bytesize=ser.EIGHTBITS,parity=ser.PARITY_NONE,stopbits=ser.STOPBITS_ONE, timeout=10)

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
template = cv2.imread("template.png")
limites = [195, 272, 30, 600]

time.sleep(2)

while time.time() - t0 < seg:
    tiempo.append(time.time() - t0)
    posiciones.append(trackTemplate(vs, template, limites, GRAFICAR=False)[0])
    pos = posiciones[-1]
    if pos >= setpoint:
        onoff.append(1)
        if cmd != 'a255\n':
            cmd = 'a255\n'
            arduino.write(bytes(cmd, 'utf-8'))
        else:
            continue
    else:
        onoff.append(0)
        if cmd != 'a180\n':
            cmd = 'a180\n'
            arduino.write(bytes(cmd, 'utf-8'))
        else:
            continue 

print(posiciones)


arduino.write(bytes('a0\n', 'utf-8'))
np.savetxt('posiciones-onoff2.csv',
           np.array([tiempo, 478 - np.array(posiciones), onoff]).T, delimiter=',')

fig, ax = plt.subplots()
ax.plot(tiempo, 478 - np.array(posiciones),color = 'cornflowerblue')
ax.axhline(setpoint, color = 'tomato')
plt.grid()
plt.show()

# print(trackTemplate(vs, template, limites, GRAFICAR=False))

time.sleep(2)
arduino.close()