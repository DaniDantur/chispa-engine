import serial
import duinobot

class Placas(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.duinobot = None

    def duinobot(self):
        self.duinobot = duinobot.Duinobot(self)

