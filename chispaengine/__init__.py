import time
import cv2


from partes_robot import placas
from partes_robot import camaras

class Chispa(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.placas = placas.Placas()
        self.camaras = camaras.Camaras()

    def esperar(self, espera=0.025, **kwargs):
        #TODO: Convertir entre milisegundos y segundos, permitir parametros para cada uno
        cv2.waitKey(1)
        time.sleep(espera)


def prender():
    chispa = Chispa()
    return chispa
