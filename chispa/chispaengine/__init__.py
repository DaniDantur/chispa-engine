import placas

class Chispa(object):
    """
    DOCUMENTAR
    """

    def __init__(self):
        self.placas = placas.Placas()


def prender():
    chispa = Chispa()
    return chispa
