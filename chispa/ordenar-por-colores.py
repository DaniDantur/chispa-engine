#!/usr/bin/env python

import time
import chispaengine

chispa = chispaengine.prender()

robot = chispa.placas.Duinobot()
robot.prender()

print "Encendido"
robot.prender_motor(motor=0, velocidad=-50)
chispa.esperar(0.50)
robot.prender_motor(motor=0, velocidad=0)


