import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Caleb Dorado NC = 0039
print("Caleb Dorado NC = 0039")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread('Montana.jpg')
plt.imshow(mi_imagen)
plt.title('Montaña y Caleb Dorado 0039')
plt.show()
print(" +-+-+-+ Puntos en la imagen +-+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300,620]
y = [100,400,500,950]
plt.scatter(x, y, s=20,c='red')
plt.show()