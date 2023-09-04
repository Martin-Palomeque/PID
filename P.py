import numpy as np
import matplotlib.pyplot as plt
import time
import serial as ser
import cv2
from tracking import trackTemplate

Kp = 1000
setpoint = 300
t0 = time.time()
seg = 50
cmd = 'a0\n'
posiciones = []
tiempo = []

arduino = ser.Serial('COM6', baudrate=9600, bytesize=ser.EIGHTBITS,parity=ser.PARITY_NONE,stopbits=ser.STOPBITS_ONE, timeout=10)

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
template = cv2.imread("template.png")
limites = [40, 630, 215, 295]

time.sleep(2)

while time.time() - t0 < seg:
    posiciones.append(trackTemplate(vs, template, limites, False))
    pos = posiciones[-1]
    if pos <= setpoint:
        if cmd != 'a255\n':
            cmd = 'a255\n'
            arduino.write(bytes(cmd, 'utf-8'))
        else:
            continue
    else:
        if cmd != 'a0\n':
            cmd = 'a0\n'
            arduino.write(bytes(cmd, 'utf-8'))
        else:
            continue

print(posiciones)

time.sleep(2)
arduino.close()