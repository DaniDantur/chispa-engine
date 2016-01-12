class Motor(object):
    """
    DOCUMENTAR
    """

    def __init__(self, indice):
        self.indice = str(indice)
        self.velocidad = 0

    def prender_motor(self, velocidad):
        self.velocidad = velocidad

        return "MOTOR " + self.indice + " " +  self.velocidad
        

    def apagar_motor(self):
        if self.indice == 0:
            return "MOTOR " + velocidad + " 0"
        elif self.indice == 1:
            return "MOTOR 0 " + velocidad

