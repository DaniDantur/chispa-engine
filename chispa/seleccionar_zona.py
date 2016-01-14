#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

imagen_inicial = camara.traer_imagen()
imagen_inicial.seleccionar_zona()


while(True):
    imagen = camara.traer_imagen()
    imagen.mostrar()

    if imagen_inicial.hay_zona:
        print "Tenemos zona"

        punto1 = imagen_inicial.hay_zona[0]
        punto2 = imagen_inicial.hay_zona[1]

        zona = imagen.recortar(punto1, punto2)
        zona.mostrar("Recorte")

    else:
        print "No hay zona definida todavia"


    chispa.esperar(0.025)
