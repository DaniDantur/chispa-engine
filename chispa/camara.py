#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

robot = chispa.placas.Duinobot()
robot.prender()

colores = ["verde", "rojo"]

hay_objeto_de_color = False

while(True):
    imagen = camara.traer_imagen()
    imagen.mostrar()

    recorte = imagen.recortar([80, 600], [300, 450])
    recorte.mostrar("Recorte")

    for color in colores:

        #Si encontre un objeto en la cinta, sigo buscando objetos solo de ese color
        if(hay_objeto_de_color):
            color = hay_objeto_de_color
    
        print "Buscando objetos de " + color

        if(color == "rojo"):
            velocidad = -100
        elif(color == "verde"):
            velocidad = 100

        mascara, objetos = recorte.buscar_objetos_por_color(color)
        mascara.mostrar("Mascara")

        if(objetos is not None):
            hay_objeto_de_color = color
            print "Encontre objetos de color " + hay_objeto_de_color

            robot.prender_motor(motor=0, velocidad=velocidad)

        else:
            hay_objeto_de_color = None
            robot.prender_motor(motor=0, velocidad=0)

    chispa.esperar(0.025)


