import serial
import time

import motores
#import timers

class Duinobot(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.puerto = "/dev/ttyACM0"
        self.baudios = 115200
        self.prendido = False
        #self.motor0 = motores.Motor(0)
        #self.motor1 = motores.Motor(1)
        self.motores = [motores.Motor(0), motores.Motor(1)]

    def prender(self):
        self.conexion = serial.Serial(self.puerto, self.baudios)
        self.prendido = True
        time.sleep(5)
        self.comunicar_serial("DATAALEATORIA")
        time.sleep(0.2)

    def comunicar_serial(self, cmd):
        if(self.prendido is False):
            print "Prendiste el robot con la funcion prender?"
            print "Ej: robot.prender()"
            return None

        print "Envio "+cmd
        time.sleep(0.25)
        self.conexion.write(cmd)

    def prender_motor(self, motor=None, velocidad=None):
        #TODO:
        #HAY QUE REHACER ESTA FUNCION
        cmd = None

        #print "Velocidad " + str(velocidad) + "\t" + str(self.motores[motor].velocidad)

        if(int(velocidad) == int(self.motores[motor].velocidad)):
            #print "Las velocidades son las mismas, no envio"
            return

        cmd = self.motores[motor].prender_motor(str(velocidad))
        self.comunicar_serial(cmd)

        #timers.timeout(self.apagar_motores, seconds=kwargs['tiempo'])
