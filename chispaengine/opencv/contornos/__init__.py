#TODO: Hacer una clase "on-the-fly" para no tener dos clases dentro del mismo archivo

import cv2

class ContornoUnico(object):
    """
    DOCUMENTAR
    """

    def __init__(self, contorno):
        self.objeto = contorno
        self.area = cv2.contourArea(self.objeto)

    def encuadrar(self):
        return cv2.boundingRect(self.objeto)


class Contornos(object):
    """
    DOCUMENTAR
    """

    def __init__(self, contornos):
        self.objetos = contornos
        self.indice = len(self.objetos)
        self.cantidad = len(self.objetos)

    def __getitem__(self, k):
        return ContornoUnico(self.objetos[k])

    def mas_grande(self):
        o = max(self.objetos, key=cv2.contourArea)
        return ContornoUnico(o)

