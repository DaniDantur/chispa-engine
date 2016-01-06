import cv2
import imagen

class Netbook(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        #TODO: Pasar parametros para camara
        self.brillo = None
        self.camara = None
        self.prendida = False

    def prender(self):
        #TODO: Aplicar parametros para camara
        self.camara = cv2.VideoCapture(0)

    def traer_imagen(self):
        #TODO: Chequear que lea bien de la camara
        (ok, frame) = self.camara.read() 
        return imagen.Imagen(frame)
