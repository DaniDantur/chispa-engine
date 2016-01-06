import duinobot

###TODO:
###Hay que mejorar esto, hay que aplicar herencia y todas esas cosas de Objetos

class Placas(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.dbt = duinobot.Duinobot()

    def Duinobot(self):
        return self.dbt
