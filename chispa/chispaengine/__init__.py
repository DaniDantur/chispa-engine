import cv2

import placas
import camaras

class Chispa(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.placas = placas.Placas()
        self.camaras = camaras.Camaras()

    def esperar(self):
        cv2.waitKey(25)


def prender():
    chispa = Chispa()
    return chispa
