import cv2

import contornos as objetos
import umbrales_colores_objeto as colores

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
        self.hay_zona = False
        self.__tabla_de_colores = colores.Colores()
        self.__zona_puntos = []

    def seleccionar_zona(self):
        self.__zona_puntos = []
        cv2.imshow("Seleccionar zona", self.imagen)
        cv2.setMouseCallback("Seleccionar zona", self.mouse_cb)


    def mouse_cb(self, ev, x, y, f, parametros):
        #TODO: Poner todos los valores en constantes
        #TODO: Colores y anchos parametrizables
        #TODO: Hacer que el cuadrado se actualice mientras uno mueve el mouse
        if ev != cv2.EVENT_LBUTTONDOWN and ev != cv2.EVENT_LBUTTONUP:
            return

        if ev == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.imagen, (x, y), 5, (0 ,0, 255), -1)
        elif ev == cv2.EVENT_LBUTTONUP:
            cv2.circle(self.imagen, (x, y), 5, (0 ,0, 255), -1)

        cv2.imshow("Seleccionar zona", self.imagen)
        self.__zona_puntos.append((x, y))

        if len(self.__zona_puntos) == 2:
            cv2.rectangle(self.imagen, self.__zona_puntos[0], self.__zona_puntos[1], (0, 255, 0), 2)
            cv2.imshow("Seleccionar zona", self.imagen)
            self.hay_zona = self.__zona_puntos


    def mostrar(self, titulo="Chispa"):
        #TODO: Parametros para la ventana, tiempo por defecto que sea configurable
        #TODO: Deberia usar de titulo el nombre del objeto
        cv2.imshow(titulo, self.imagen)
        cv2.waitKey(1)
    
    def recortar(self, pt1, pt2):
        #TODO: Un solo parametro que traiga ambos puntos
        #TODO: Chequear que se pueda recortar, que el tamano de corte no sea mayor que la imagen o negativo
        recorte = self.imagen[pt1[1]:pt2[1], pt1[0]:pt2[0]]
        return Imagen(recorte)

    def buscar_objetos_por_color(self, color):
        #TODO: Hay que hacer tabla de colores, y hacer herramientas para configurarlos
        #TODO: Que se pueda pasar por parametro un color si no existe en la tabla
        #TODO: Definir como se van a devolver los valores

        if color not in self.__tabla_de_colores.colores:
            print "No se encuentra "+ color +" en la tabla de colores"
            return

        min_color = self.__tabla_de_colores.colores[color][0]
        max_color = self.__tabla_de_colores.colores[color][1]

        color_minimo = (min_color[0], min_color[1], min_color[1])
        color_maximo = (max_color[0], max_color[1], max_color[1])
        frame_hsv = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)

        mascara = cv2.inRange(frame_hsv, color_minimo, color_maximo)
        mascara = cv2.erode(mascara, None, iterations=2)
        mascara = cv2.dilate(mascara, None, iterations=2)

        (_, cnts, _) = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if(len(cnts) == 0):
            return Imagen(mascara), None

        return Imagen(mascara), objetos.Contornos(cnts)
        
