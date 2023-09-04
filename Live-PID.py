import numpy as np
import matplotlib.pyplot as plt
import time
import serial as ser
import cv2
from tracking import trackTemplate
from matplotlib.animation import FuncAnimation

setpoint = 200
t0 = time.time()
seg = 30
cmd = 'a0\n'
posiciones = []

fig, ax = plt.subplots()

pause = False
arduino = ser.Serial('COM6', baudrate=9600, bytesize=ser.EIGHTBITS,parity=ser.PARITY_NONE,stopbits=ser.STOPBITS_ONE, timeout=10)

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
template = cv2.imread("template.png")
limites = [195, 272, 30, 600]

time.sleep(2)

def animate(i): 
    global pause 

    while pause == False: 
        ax.cla()
        posiciones.append(trackTemplate(vs, template, limites, GRAFICAR=False)[0])
        pos = posiciones[-1]
        print(pos)
        if pos >= setpoint:
            if cmd != 'a255\n':
                cmd = 'a255\n'
                arduino.write(bytes(cmd, 'utf-8'))
            else:
                continue
        else:
            if cmd != 'a200\n':
                cmd = 'a200\n'
                arduino.write(bytes(cmd, 'utf-8'))
            else:
                continue
        ax.plot(posiciones)
        
    else:   #cuando pause cambie de estado, False -> True, devuelve un str de aviso y para la funcion
        print('Stopped Function')
        exit() #termina la ejecucion del codigo


print(posiciones)

arduino.write(bytes('a0\n', 'utf-8'))



# print(trackTemplate(vs, template, limites, GRAFICAR=False))
def onClick(event): #Simplemente es una funcion que cambia el estado de la variable pause
    global pause
    pause ^= True 


fig.canvas.mpl_connect('scroll_event',onClick) #Conecta la figura a un evento. El evento es el scroll del mouse en la figura ('scroll_event') y ejecuta la funcion 'onClick'


ani = FuncAnimation(fig,animate,interval = 16.66)

plt.show()
time.sleep(2)
arduino.close()