#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

robot = chispa.placas.Duinobot()

robot.prender()

robot.prender_servo(servo=0, angulo=1)
chispa.esperar(1)
robot.prender_servo(servo=0, angulo=45)
robot.prender_servo(servo=0, angulo=90)
robot.prender_servo(servo=0, angulo=180)

