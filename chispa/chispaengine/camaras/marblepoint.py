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
        #TODO: Chequear que este prendida con el metodo .prender()
        (ok, frame) = self.camara.read() 
        return imagen.Imagen(frame)

    def mostrar_controles(self):
        #TODO: Poner nombre de ventana en variable
        #TODO: Escribir texto sobre imagen, avisando que es la imagen original
        (ok, frame) = self.camara.read()

        brillo_actual = int(self.camara.get(cv2.CAP_PROP_BRIGHTNESS) * 100)

        cv2.imshow("Controles", frame)
        cv2.createTrackbar("Brillo", "Controles", 0, 100, self.establecer_brillo)
        cv2.setTrackbarPos("Brillo", "Controles", brillo_actual)


    def establecer_brillo(self, valor):
        self.brillo = valor / float(100)
        self.camara.set(cv2.CAP_PROP_BRIGHTNESS, self.brillo)
