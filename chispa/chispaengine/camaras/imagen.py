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

    def mostrar(self, titulo="Chispa"):
        #TODO: Parametros para la ventana, tiempo por defecto que sea configurable
        cv2.imshow(titulo, self.imagen)
        cv2.waitKey(1)
    
    def recortar(self, pt1, pt2):
        #TODO: Chequear que se pueda recortar, que el tamano de corte no sea mayor que la imagen o negativo
        recorte = self.imagen[pt1[0]:pt1[1], pt2[0]:pt2[1]]
        return Imagen(recorte)
