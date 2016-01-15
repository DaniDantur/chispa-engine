import marblepoint

###TODO:
###Hay que mejorar esto, hay que aplicar herencia y todas esas cosas de Objetos

class Camaras(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.mbp = None

    def Netbook(self):
        self.mbp = marblepoint.Netbook()
        return self.mbp


