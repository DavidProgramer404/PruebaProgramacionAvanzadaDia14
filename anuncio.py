from error import SubTipoInvalido

class Anuncio:
    SUB_TIPOS = []

    def __init__(self, alto, ancho, sub_tipo=None):
        self.alto = alto
        self.ancho = ancho
        self.sub_tipo = sub_tipo

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        if value < 1:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = value

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        if value < 1:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = value

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value and value not in self.SUB_TIPOS:
            raise SubTipoInvalido("Subtipo no válido")
        self._sub_tipo = value

    def __str__(self):
        return f"Anuncio ({self.alto}x{self.ancho}) - Subtipo: {self.sub_tipo}"

class Video(Anuncio):
    SUB_TIPOS = ["instream", "outstream"]

    def __init__(self, alto, ancho, duracion, sub_tipo):
        super().__init__(alto, ancho, sub_tipo)
        self.duracion = duracion

    def c_anuncio(self):
        print("Compresión de Video no implementada aún.")

    def r_anuncio(self):
        print("Recorte de Video no implementado aún.")

class Display(Anuncio):
    SUB_TIPOS = ["tradicional", "native"]

    def __init__(self, alto, ancho, sub_tipo):
        super().__init__(alto, ancho, sub_tipo)
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalido("Subtipo no válido para Display")

    def c_anuncio(self):
        print("Compresión de Display no implementada aún.")

    def r_anuncio(self):
        print("Redimensionamiento de Display no implementado aún.")

class Social(Anuncio):
    SUB_TIPOS = ["facebook", "linkedin"]

    def __init__(self, alto, ancho, sub_tipo):
        super().__init__(alto, ancho, sub_tipo)
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalido("Subtipo no válido para Social")

    def c_anuncio(self):
        print("Compresión de Social no implementada aún.")

    def r_anuncio(self):
        print("Redimensionamiento de Social no implementado aún.")
