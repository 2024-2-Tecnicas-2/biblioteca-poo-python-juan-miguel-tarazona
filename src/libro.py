from publicacion import Publicacion
class Libro(Publicacion):
    def __init__(self,titulo,añoPublicacion,autor,numeroPaginas):
        super().__init__(titulo,añoPublicacion)
        self.autor=autor
        self.numeroPaginas=numeroPaginas
        
    

    def __str__(self):
        publicacion=super().__str__()
        return (
            f"{publicacion}\n"
            f"Autor: {self.autor}\n"
            f"numeroPaginas: {self.numeroPaginas}"
        )

