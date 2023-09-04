import numpy as np
import cv2
import time

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
    
    return top_left


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
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False)[0])
            pos = posiciones[-1]

            # Chequea posiciones y manda la respuesta correspondiente
            if pos < self.setpoint and cmd != f'a{self.max}\n':
                cmd = f'a{self.max}\n'
                self.arduino.write(bytes(f'a{self.max}\n', 'utf-8'))
            elif pos >= self.setpoint and cmd != f'a{self.min}\n':
                cmd = f'a{self.min}\n'
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
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False)[0])
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
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False)[0])
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
            posiciones.append(trackTemplate(self.vs, self.template, self.limites, GRAFICAR=False)[0])
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

        return np.array(tiempo), np.array(posiciones), np.array(P_list), np.array(I_list), np.array(D_list)
    
    def ZN(self, ):
        pass