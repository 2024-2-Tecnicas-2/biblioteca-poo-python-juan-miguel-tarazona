from publicacion import Publicacion
class Revista(Publicacion):
    def __init__(self,titulo,añoPublicacion,numRevista,nomRevista):
        super().__init__(titulo,añoPublicacion)
        self.numRevista=numRevista
        self.nomRevistas=nomRevista

    def __str__(self):
        publicacion=super().__str__()
        return (
            f"{publicacion}\n"
            f"numero de revista: {self.numRevista}\n"
            f"nombre de la revista: {self.nomRevistas}"
        )