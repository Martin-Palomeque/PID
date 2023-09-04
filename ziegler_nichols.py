
import numpy as np
import matplotlib.pyplot as plt
import time
import serial as ser
import cv2
from tracking import trackTemplate

t0 = time.time()
seg = 30
cmd = 'a0\n'
posiciones = []
tiempo = []

arduino = ser.Serial('COM6', baudrate=9600, bytesize=ser.EIGHTBITS,parity=ser.PARITY_NONE,stopbits=ser.STOPBITS_ONE, timeout=10)

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
template = cv2.imread("template.png")
limites = [195, 272, 30, 600]

time.sleep(2)

arduino.write(bytes('a255\n', 'utf-8'))
while time.time() - t0 < seg:
    posiciones.append(trackTemplate(vs, template, limites, GRAFICAR=False)[0])
    pos = posiciones[-1]
    tiempo.append(time.time() - t0)

print(posiciones)


arduino.write(bytes('a0\n', 'utf-8'))
#np.savetxt('pulso.csv', 478 - np.array(posiciones).T, delimiter=',')

fig, ax = plt.subplots()
ax.plot(tiempo, 478 - np.array(posiciones),color = 'cornflowerblue')

plt.grid()
plt.show()

# print(trackTemplate(vs, template, limites, GRAFICAR=False))

time.sleep(2)
arduino.close()