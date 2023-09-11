import cv2
from metodos import imagenes as img

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)

camara = img(vs)

camara.sin_cortar(nombre='Imagenes/tubo')
camara.cortar(limites=[0, 595, 150, 230], nombre='Imagenes/corte')