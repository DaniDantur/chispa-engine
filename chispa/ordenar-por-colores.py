#!/usr/bin/env python

import time
import chispaengine

chispa = chispaengine.prender()

robot = chispa.placas.Duinobot()
camara = chispa.camaras.Netbook()

robot.prender()
camara.prender()

colores_a_buscar = ["verde", "rojo"]
hay_objeto_de_color = False


while(True):
    imagen = camara.traer_imagen()
    imagen.mostrar("Camara")

    zona_elegir_color = imagen.recortar([80, 200], [300, 450])
    zona_elegir_color.mostrar("Zona para elegir color")


    for color in colores_a_buscar:
        if(hay_objeto_de_color):
            color = hay_objeto_de_color

        #print "Busco tapitas de color " + color

        m, objetos = zona_elegir_color.buscar_objetos_por_color(color)
        m.mostrar("M")

        if(objetos is not None):
            print "Hay tapita de color " + color

            hay_objeto_de_color = color

            if(hay_objeto_de_color == "verde"):
                angulo = 90
            elif(hay_objeto_de_color == "rojo"):
                angulo = 180

            robot.prender_servo(servo=0, angulo=angulo)

        else:
            hay_objeto_de_color = None
            robot.prender_servo(servo=0, angulo=0)


    chispa.esperar(0.025)



