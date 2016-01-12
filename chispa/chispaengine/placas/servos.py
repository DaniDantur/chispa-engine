class Servo(object):
    """
    DOCUMENTAR
    """

    def __init__(self, indice):
        self.indice = str(indice)
        self.angulo = 0

    def prender_servo(self, angulo):
        self.angulo = angulo

        return "SERVO " + self.indice + " " + self.angulo


