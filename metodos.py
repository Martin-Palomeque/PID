import numpy as np
import cv2
import time
from matplotlib.image import imsave

def trackTemplate(vs, template, limites, GRAFICAR=False):
    # Leer frame
    frame = vs.read()[1]
    if frame is None:
        return None, None
    
    # Cortar zona del tubo
    min_x, max_x, min_y, max_y = limites
    corte = frame[min_y:max_y, min_x:max_x, :]
    
    # Trackear el template
    res = cv2.matchTemplate(corte, template, cv2.TM_CCOEFF)
    top_left = cv2.minMaxLoc(res)[3]
    
    if GRAFICAR:
        # Dimensiones del template (para dibujar el rectángulo)
        w, h = template.shape[:-1]
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(corte, top_left, bottom_right, 255, 2)
        cv2.imshow("corte", corte)
    
    return top_left[0]


class imagenes:
    def __init__(self, vs):
        self.vs = vs
    
    def sin_cortar(self, nombre='tubo'):
        # Saca foto del tubo y guarda la foto
        frame = self.vs.read()[1]
        tubo = np.mean(frame, axis=2)
        imsave(f'{nombre}.png', tubo, cmap='gray')
        # Guarda el nombre de la foto a cortar
        self.a_cortar = nombre
    
    def cortar(self, limites, nombre='corte'):
        # Define los limites
        min_x, max_x, min_y, max_y = limites
        # Intenta leer imagen a cortar y si no saca una
        try:
            corte = cv2.imread(f'{self.a_cortar}.png')
        except AttributeError:
            corte = self.vs.read()[1]
        # Corta la imagen
        corte = corte[min_y:max_y, min_x:max_x, :]
        # Guarda el corte
        corte = np.mean(corte, axis=2)
        imsave(f'{nombre}.png', corte, cmap='gray')
    
    def template(self):
        print('El template siempre lo cortamos a mano, ni me caliento')


class controlador:
    def __init__(self, vs, template, limites, arduino, setpoint, seg=60, min=200, max=255):
        # Constantes de camara
        self.vs = vs
        self.template = template
        self.limites = limites
        # Arduino
        self.arduino = arduino
        # Constantes de medicion
        self.setpoint = setpoint
        self.seg = seg
        self.min = min
        self.max = max

    def on_off(self):
        # Crea las listas vacias que van a ser nuestras mediciones
        posiciones = []
        tiempo = []
        onoff = []
        cmd = ''
        
        t0 = time.time()
        while time.time()- t0 < self.seg:
            # Appendea tiempos y posiciones
            tiempo.append(time.time() - t0)
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False))
            pos = posiciones[-1]

            # Chequea posiciones y manda la respuesta correspondiente
            if pos < self.setpoint and cmd != f'a{self.max}\n':
                cmd = f'a{self.max}\n'
                self.arduino.write(bytes(f'a{self.max}\n', 'utf-8'))
            elif pos >= self.setpoint and cmd != f'a{self.min}\n':
                cmd = f'a{self.min}\n'
                self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))
            
        self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))
        
        return np.array(tiempo), np.array(posiciones), np.array(onoff)

    
    def P(self, Kp):
        # Crea las listas vacias que van a ser nuestras mediciones
        posiciones = []
        tiempo = []
        P_list = []

        t0 = time.time()
        while time.time() - t0 < self.seg:
            # Appendea tiempos y posiciones
            tiempo.append(time.time() - t0)
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False))
            pos = posiciones[-1]

            # Calcula el error y la entrada
            error = self.setpoint - pos
            P = Kp*error
            P_list.append(P)

            # Chequea los bounds de la entrada y manda lo correspondiente
            if P > self.max:
                self.arduino.write(bytes(f'a{self.max}\n', 'utf-8'))
            elif P < self.min:
                self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))
            else:
                self.arduino.write(bytes(f'a{int(P)}\n', 'utf-8'))

        self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))
        
        return np.array(tiempo), np.array(posiciones), np.array(P)
    
    def PI(self, Kp, Ki):
        # Crea las listas vacias que van a ser nuestras mediciones
        posiciones = []
        tiempo = []
        P_list = []
        I_list = []

        t0 = time.time()
        while time.time() - t0 < self.seg:
            # Appendea tiempos y posiciones
            tiempo.append(time.time() - t0)
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False))
            pos = posiciones[-1]

            # Calcula el error, el P y el I
            error = self.setpoint - pos

            P = Kp*error
            P_list.append(P)

            if len(tiempo) > 1:
                I += Ki*(tiempo[-1] - tiempo[-2])*error
            else:
                I = 0
            I_list.append(I)

            # Chequea los bounds de la entrada y manda lo correspondiente
            if P + I > self.max:
                self.arduino.write(bytes(f'a{self.max}\n', 'utf-8'))
            elif P + I < self.min:
                self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))
            else:
                self.arduino.write(bytes(f'a{int(P + I)}\n', 'utf-8'))
        
        self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))

        return np.array(tiempo), np.array(posiciones), np.array(P_list), np.array(I_list)
    
    def PID(self, Kp, Ki, Kd):
        # Crea las listas vacias que van a ser nuestras mediciones
        posiciones = []
        tiempo = []
        P_list = []
        I_list = []
        D_list = []

        t0 = time.time()
        while time.time() - t0 < self.seg:
            # Appendea tiempos y posiciones
            tiempo.append(time.time() - t0)
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False))
            pos = posiciones[-1]

            # Calcula el error, el P, el I y el D
            error = self.setpoint - pos

            # P
            P = Kp*error
            P_list.append(P)
            # I y D
            if len(tiempo) > 1:
                I += Ki*(tiempo[-1] - tiempo[-2])*error
                D = Kd*(error - error_ant) / (tiempo[-1] - tiempo[-2])
            else:
                I = 0
                D = 0
            I_list.append(I)
            D_list.append(D)
            error_ant = error

            # Chequea los bounds de la entrada y manda lo correspondiente
            if P + I + D > self.max:
                self.arduino.write(bytes(f'a{self.max}\n', 'utf-8'))
            elif P + I + D < self.min:
                self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))
            else:
                self.arduino.write(bytes(f'a{int(P + I + D)}\n', 'utf-8'))


        self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))

        return np.array(tiempo), np.array(posiciones), np.array(P_list), np.array(I_list), np.array(D_list)
    
    def ZN(self, inicial=220, final=255, control='PID', tiempo_control=10):
        # posiciones = []
        # tiempo = []
        
        # self.arduino.write(bytes(f'a{inicial}\n', 'utf-8'))
        # time.sleep(tiempo_control)
        # self.arduino.write(bytes(f'a{final}\n', 'utf-8'))

        # # PUEDE SER QUE TIRE ERROR
        # t0 = time.time()
        # while time.time() - t0 < tiempo_control or posiciones[-2] - posiciones[-1] > 2:
        #     tiempo.append(time.time() - t0)
        #     posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False))
        
        # self.arduino.write(bytes(f'a{self.min}\n', 'utf-8'))

        # max_diff = np.max(np.diff(posiciones))
        # i_max_diff = np.argmax(np.diff(posiciones))
        # if len(i_max_diff) > 1:
        #     i_max_diff = i_max_diff[int(len(i_max_diff) / 2)]
        pass