#!/usr/bin/env python

import time
import chispaengine


chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

while(True):

    imagen = camara.traer_imagen()
    imagen.mostrar()
    chispa.esperar()


