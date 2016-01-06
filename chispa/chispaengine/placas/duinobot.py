import serial
import time

class Duinobot(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.puerto = "/dev/ttyACM0"
        self.baudios = 115200
        self.prendido = False

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
        self.conexion.write(cmd)

    def prender_motores(self, **kwargs):
        cmd = None

        if 'velocidad' not in kwargs:
            cmd = "MOTOR 100 100"
        else:
            cmd = "MOTOR "+str(kwargs['velocidad'])+" "+str(kwargs['velocidad'])

        self.comunicar_serial(cmd)

    def prender_motor(self, motor=None, **kwargs):
        #TODO:
        #HAY QUE REHACER ESTA FUNCION
        cmd = None

        if motor is None:
            print "No se especifico motor"
            return None

        if motor is 0:
            if 'velocidad' not in kwargs:
                cmd = "MOTOR 100 0"
            else:
                cmd = "MOTOR "+str(kwargs['velocidad'])+" 0"
            
        elif motor is 1:
            if 'velocidad' not in kwargs:
                cmd = "MOTOR 0 100"
            else:
                cmd = "MOTOR 0 "+str(kwargs['velocidad'])

        self.comunicar_serial(cmd)

    def apagar_motores(self):
        cmd = "MOTOR 0 0"
        self.comunicar_serial(cmd)
