import serial
import time

import motores
import timers

class Duinobot(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.puerto = "/dev/ttyACM0"
        self.baudios = 115200
        self.prendido = False
        self.motor0 = motores.Motor()
        self.motor1 = motores.Motor()

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

        #print "Envio "+cmd
        time.sleep(0.050)
        self.conexion.write(cmd)

    def prender_motores(self, **kwargs):
        cmd = None


        self.comunicar_serial(cmd)

    def prender_motor(self, motor=None, **kwargs):
        #TODO:
        #HAY QUE REHACER ESTA FUNCION
        cmd = None

        timers.timeout(self.apagar_motores, seconds=kwargs['tiempo'])

    def apagar_motores(self):
        cmd = "MOTOR 0 0"
        self.comunicar_serial(cmd)
        self.motor_ocupado = False
