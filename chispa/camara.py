#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

while(True):

    imagen = camara.traer_imagen()
    imagen.mostrar()

    chispa.esperar(0.025)


