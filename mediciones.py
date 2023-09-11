import cv2
import time
import numpy as np
import serial as ser
import pandas as pd
import matplotlib.pyplot as plt
import metodos as met

# ARDUINO
arduino = ser.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=0, rtscts=0)
time.sleep(2)

# CONTROL
ctrl = met.controlador(vs=cv2.VideoCapture(0, cv2.CAP_DSHOW),
                       template=cv2.imread('Imagenes/template.png'),
                       limites=[0, 595, 150, 230],
                       arduino=arduino,
                       setpoint=400,
                       seg=45,
                       min=0,
                       max=255)

if ctrl.min != 0:
    arduino.write(bytes(f'a{ctrl.min}\n', 'utf-8'))
    time.sleep(7)

# MEDICION
t, h, P, I, D = ctrl.PID(0.7, 0, 0)

# FIGURA
plt.style.use('./informes.mplstyle')
fig, ax = plt.subplots(2, 1)
ax[0].plot(t, h)
ax[1].plot(t, P, label='P')
ax[1].plot(t, I, label='I')
ax[1].plot(t, D, label='D')
ax[1].plot(t, P+I+D, label='P + I + D')
ax[0].axhline(ctrl.setpoint, c='k', ls='--')
ax[1].axhline(ctrl.min, c='k', ls='--')
ax[1].axhline(ctrl.max, c='k', ls='--')

ax[1].legend()
plt.show()

# GUARDAR DATOS
df = pd.DataFrame()
df['Time'] = t
df['Position'] = h
df['P'] = P
df['I'] = I
df['D'] = D
df['kp'] = pd.Series([ctrl.Kp],index = [0])
df['ki'] = pd.Series([ctrl.Ki],index = [0])
df['kd'] = pd.Series([ctrl.Kd],index = [0])
df['Setpoint'] = pd.Series([ctrl.setpoint],index = [0])
df['Pixel Lenght'] = pd.Series([ctrl.limites[1] - ctrl.limites[0]],index = [0])

# if input('Queres guardar? [y/n]') == 'y':
# df.to_csv(rf'Mediciones/PID-{ctrl.Kp}-{ctrl.Ki}-{ctrl.Kd}-(min={ctrl.min})-setpoint={ctrl.setpoint}2.csv')
df.to_csv(rf'Mediciones/PID-{ctrl.Kp}-{ctrl.Ki}-{ctrl.Kd}-barrido.csv')

time.sleep(2)
arduino.close()