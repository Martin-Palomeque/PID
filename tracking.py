
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image






def trackTemplate(vs, template, limites, GRAFICAR=True):
    # Leer frame
    min_x, max_x, min_y, max_y = limites
    frame = vs.read()[1]
    
    # Romper el loop cuando termina el video
    if frame is None:
        return None, None
    
    # Cortar zona del tubo
    corte = frame[min_y:max_y, min_x:max_x, :]
    
    # Rotar la imagen
    # corte = np.transpose(corte, (1, 0, 2))
    
    # Dimensiones del template (para dibujar el rectángulo)
    w, h = template.shape[:-1]
    
    # Trackear el template
    res = cv2.matchTemplate(corte, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    if GRAFICAR:
        cv2.rectangle(corte, top_left, bottom_right, 255, 2)
        cv2.imshow("corte", corte)
    
        key = cv2.waitKey() & 0xFF
        # fin = False
        
        # # if the 'q' key is pressed, stop the loop
        # if key == ord("l"):
        #     print("track")
        #     fin = True  
    
    return top_left


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
