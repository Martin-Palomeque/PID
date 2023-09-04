
import time
import serial
import numpy as np

# #%% Iniciar controlador serie
# # arduino = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=0, rtscts=0)
# arduino = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=0, rtscts=0)
# arduino.close() 
# arduino.open()
# #%%
# # arduino.open()
# mistr = "a200"
# arduino.write(bytes(mistr,'utf-8'))
# time.sleep(0.05)
# s = arduino.readline(25)
# # s = arduino.readlines()
# print(s)
# # arduino.write(b'a244\n')
# arduino.close()

arduino = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=0, rtscts=0)
time.sleep(2)

arduino.write(bytes('a255\n', 'utf-8'))

time.sleep(2)
arduino.close()