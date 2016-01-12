class Motor(object):
    """
    DOCUMENTAR
    """

    def __init__(self, indice):
        self.indice = str(indice)
        self.motor_ocupado = False
        self.velocidad = 0

    def prender_motor(self, velocidad):
        #if self.motor_ocupado == True:
        #    print "El motor " + self.indice + " esta ocupado"
        #    return

        self.motor_ocupado = True
        self.velocidad = velocidad

        return "MOTOR " + self.indice + " " +  self.velocidad
        

    def apagar_motor(self):
        if self.indice == 0:
            return "MOTOR " + velocidad + " 0"
        elif self.indice == 1:
            return "MOTOR 0 " + velocidad

