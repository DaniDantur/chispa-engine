class Motor(object):
    """
    DOCUMENTAR
    """

    def __init__(self, indice):
        self.indice = indice
        self.motor_ocupado = False

    def prender_motor(self, velocidad):
        if self.motor_ocupado == True:
            print "El motor " + self.indice + " esta ocupado"
            return

        self.motor_ocupado = True
        if self.indice == 0:
            return "MOTOR " + velocidad + " 0"
        elif self.indice == 1:
            return "MOTOR 0 " + velocidad

    def apagar_motor(self):
        if self.indice == 0:
            return "MOTOR " + velocidad + " 0"
        elif self.indice == 1:
            return "MOTOR 0 " + velocidad

