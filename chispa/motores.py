#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

robot = chispa.placas.Duinobot()
robot.prender()

robot.prender_motor(motor=1, velocidad=-100)
robot.prender_motor(motor=0, velocidad=-100)
chispa.esperar(5)
robot.prender_motor(motor=1, velocidad=0)
robot.prender_motor(motor=0, velocidad=0)

#robot.prender_motor(motor=0, velocidad=0)
#robot.prender_motor(motor=1, velocidad=0)

print "Fin"
