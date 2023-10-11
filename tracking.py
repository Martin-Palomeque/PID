import numpy as np
from matplotlib.image import imsave
import cv2
import serial as ser
import time


'''
Contiene todas las funciones útiles para sacar una
foto, cortar la zona solo del tubo, y trackear un
template en una imágen.
'''
class imagenes:
    def __init__(self, vs):
        self.vs = vs
    
    '''
    Saca la foto sin cortar para despues establecer
    manualmente los limites de corte para quedarte
    solo con el tubo despues.
    Por defecto la imagen se guarda como "tubo.png"
    en escala de grises.
    '''
    def sin_cortar(self, nombre='tubo'):
        # Saca foto del tubo y guarda la foto
        frame = self.vs.read()[1]
        tubo = np.mean(frame, axis=2)
        imsave(f'{nombre}.png', tubo, cmap='gray')

    
    '''
    Saca una foto cortada con los limites dados para
    luego establecer manualmente el template del vaso.
    Necesita los limites de corte del tubo y por defecto
    la imágen se guarda como "corte.png" en escala de grises.
    '''
    def cortar(self, limites, nombre='corte'):
        # Define los limites
        min_x, max_x, min_y, max_y = limites
        # Saca una foto para cortar
        corte = self.vs.read()[1]
        # Corta la foto
        corte = corte[min_y:max_y, min_x:max_x, :]
        # Guarda el corte
        corte = np.mean(corte, axis=2)
        imsave(f'{nombre}.png', corte, cmap='gray')
    

    '''
    Es necesario cortar el template a mano (con paint)
    '''
    def template(self):
        print('El template es necesario cortarlo a mano')
    

    '''
    Busca el template en una foto actual. La idea es que la
    cámara está siempre sacando fotos y busca dentro de la foto
    actual la posicion en la que detecta que se encuentra el
    objeto dentro del template.
    Necesita la ubicación donde se encuentra el template y los
    limites para cortar. Devuelve la posición del template dentro
    de la imágen en pixeles.
    '''
    def trackTemplate(self, template, limites, GRAFICAR=False):
        # Saca foto. Si no puede devuelve None
        frame = self.vs.read()[1]
        if frame is None:
            return None
        
        # Cortar zona del tubo
        min_x, max_x, min_y, max_y = limites
        corte = frame[min_y:max_y, min_x:max_x, :]
        
        # Lee el template y lo trackea.Devuelve como posición la esquina superior izquierda.
        template = cv2.imread(f'{template}.png')
        res = cv2.matchTemplate(corte, template, cv2.TM_CCOEFF)
        top_left = cv2.minMaxLoc(res)[3]
        
        if GRAFICAR:
            # Dimensiones del template (para dibujar el rectángulo)
            w, h = template.shape[:-1]
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(corte, top_left, bottom_right, 255, 2)
            cv2.imshow("corte", corte)
        
        return top_left[0]
    


# SACAR FOTOS Y CORTARLAS

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camara = imagenes(vs)

camara.sin_cortar()
camara.cortar(limites=[0, 600, 0, 480])
camara.template()

template = 'c:/path.tp.template.png'
limites = [0, 600, 0, 480]

# ARDUINO

arduino = ser.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.05, xonxoff=0, rtscts=0)
time.sleep(2)

arduino.write(bytes('a255\n', 'utf-8'))

tiempo = []
posicion = []
duracion = 10  # s

t0 = time.time()
while time.time() - t0 < duracion:
    # Appendea tiempos y posiciones
    tiempo.append(time.time() - t0)
    posicion.append(camara.trackTemplate(template=template, limites=limites))


time.sleep(2)
arduino.close()