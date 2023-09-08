import numpy as np
import matplotlib.pyplot as plt
import serial as ser
import cv2
import time
from tracking import trackTemplate
from Funciones_PID import P,I


ki = 1
kp = 1
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

while time.time() - t0 < seg:
    if len(tiempo) < 1: #Cuando la longitud sea 1, le va a agregar otro numero y se va a poder hacer la resta de dt
        posiciones.append(tubo_en_pixel - trackTemplate(vs,template,limites,GRAFICAR=False)[0])
        pos = posiciones[-1]
        tiempo.append(time.time() - t0)
        error = setpoint - pos
        P = P(error,kp)
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
        error = setpoint - pos
        I = I(tiempo[-2],tiempo[-1],error,ki)
        P = P(error,kp)
        PI = P + I
        if PI > 255:
            arduino.write(bytes(f'a255\n', 'utf-8'))
        elif PI < 180:
            arduino.write(bytes(f'a180\n', 'utf-8'))
        else:
            arduino.write(bytes(f'a{int(I)}\n', 'utf-8'))

