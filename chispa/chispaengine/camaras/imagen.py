import cv2

class Imagen(object):
    """
    DOCUMENTAR
    """

    def __init__(self, frame):
        #TODO: Rellenar las propiedades con la data del frame
        self.imagen = frame
        self.ancho = None
        self.alto = None
        self.cantidad_de_canales = None
        self.modelo_de_colores = None

    def mostrar(self):
        #TODO: Parametros para la ventana
        cv2.imshow("Chispa", self.imagen)
