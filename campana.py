from error import LargoExcedido
from datetime import datetime

class Campana:
    def __init__(self, nombre, anuncios, fecha_inicio, fecha_termino):
        self.nombre = nombre
        self.anuncios = anuncios
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedido("El nombre excede los 250 caracteres")
        self._nombre = value

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        try:
            self._fecha_inicio = datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Formato de fecha de inicio inválido. Use DD-MM-YYYY.")

    @property
    def fecha_termino(self):
        return self._fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value):
        try:
            self._fecha_termino = datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Formato de fecha de término inválido. Use DD-MM-YYYY.")

    def __str__(self):
        anuncios_str = ", ".join([anuncio.__class__.__name__ for anuncio in self.anuncios])
        return f"Campaña: {self.nombre}\nInicio: {self.fecha_inicio.strftime('%Y-%m-%d')}\nTérmino: {self.fecha_termino.strftime('%Y-%m-%d')}\nAnuncios: {anuncios_str}"
