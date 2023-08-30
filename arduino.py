
import time
import serial
import numpy as np

#%% Iniciar controlador serie
arduino = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=0, rtscts=0)
arduino.close() 
arduino.open()
#%%
mistr = "a200"
arduino.write(bytes(mistr,'utf-8'))
time.sleep(0.05)
s = arduino.readline(25)
print(s)
# arduino.write(b'a244\n')
arduino.close()