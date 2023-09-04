
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image


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
    
        key = cv2.waitKey() 
    
    return top_left


# Trackear imagen si se corre directamente
if __name__ == '__main__':

    vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Abrir template
    template = cv2.imread("template.png")

    limites = [40, 630, 215, 295]
    pos = trackTemplate(vs, template, limites)
    print(pos)

    #I = np.mean(frame,axis=2)
    #I_corte = np.mean(corte,axis=2)
    
    #matplotlib.image.imsave('imagen.png', I,cmap='gray')
    #matplotlib.image.imsave('corte.png', I_corte,cmap='gray')
