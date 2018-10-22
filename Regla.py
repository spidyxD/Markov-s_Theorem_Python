class Regla:
    """""
    def __init__(self,entrada,salida,esFinal,numero):
        self.entrada = entrada
        self.salida = salida
        self.esFinal = esFinal
        self.numero = numero
        self.etiqueta = None
        self.comentario = None
    """""
    def __init__(self, entrada="", salida=""):
        self.entrada = entrada
        self.salida = salida
    """
    def __init__(self, entrada="", salida="", esFinal="", numero="",etiqueta=""):
        self.entrada = entrada
        self.salida = salida
        self.esFinal = esFinal
        self.numero = numero
        self.etiqueta = etiqueta
        self.comentario = None
    """
    def getEntrada(self):
        return self.entrada

    def getSalida(self):
        return self.salida

    def getEsFinal(self):
        return self.esFinal

    def getNumero(self):
        return self.numero

    def getEtiqueta(self):
        return self.etiqueta

    def getComentario(self):
        return self.comentario

    def setEntrada(self,entrada):
        self.entrada = entrada

    def setSalida(self,salida):
        self.salida = salida

    def setEsFinal(self,esFinal):
        self.esFinal = esFinal

    def setNumero(self,numero):
        self.numero = numero

    def setEtiqueta(self,etiqueta):
        self.etiqueta = etiqueta

    def setComentario(self,comentario):
        self.comentario = comentario