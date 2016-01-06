#!/usr/bin/env python

import time
import chispaengine

chispa = chispaengine.prender()

robot = chispa.placas.Duinobot()

#robot.prender()
#robot.prender_motores()
#time.sleep(1)
#robot.apagar_motores()

robot.prender_motor(motor=0, velocidad=75)


