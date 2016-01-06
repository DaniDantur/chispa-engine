#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

while(True):

    imagen = camara.traer_imagen()
    imagen.mostrar()

    recorte = imagen.recortar([300, 500], [300, 450])
    recorte.mostrar("Recorte")

    chispa.esperar(0.025)


