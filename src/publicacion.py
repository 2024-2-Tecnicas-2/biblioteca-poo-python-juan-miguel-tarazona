class Publicacion:
    def __init__(self,titulo,añoPublicacion):
        self.titulo=titulo
        self.añoPublicacion=añoPublicacion

    def __str__(self):
        return (
                f"Titulo: {self.titulo}\n"
                f"Año de publicaion: {self.añoPublicacion}")

    
