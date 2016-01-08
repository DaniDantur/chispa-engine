#!/usr/bin/env python

import chispaengine

barrera = 0
cinta = 1

chispa = chispaengine.prender()

robot = chispa.placas.Duinobot()
robot.prender()

camara = chispa.camaras.Netbook()
camara.prender()

while(True):

    imagen = camara.traer_imagen()
    imagen.mostrar()

    recorte = imagen.recortar([300, 500], [300, 450])
    recorte.mostrar("Recorte")

    #objetos = recorte.buscar_objetos_por_color("verde")
    mascara, objetos = recorte.buscar_objetos_por_color("rojo")
    mascara.mostrar("Mascara")

    if(objetos is not None):
        print "Encontre " + str(objetos.cantidad)

        #for objeto in objetos:
        #    print objeto.area

        objeto_mas_grande = objetos.mas_grande()

        imagen = camara.traer_imagen()
        imagen.mostrar()

        robot.prender_motor(motor=barrera, velocidad=-50)
        chispa.esperar(0.50)
        robot.prender_motor(motor=barrera, velocidad=0)
        chispa.esperar(0.50)
        robot.prender_motor(motor=cinta, velocidad=100)

        print "El area mas grande es " + str(objeto_mas_grande.area)


    chispa.esperar(0.025)


