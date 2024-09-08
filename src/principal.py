from libro import Libro
from revista import Revista
if __name__ == '__main__':
    li=Libro("overlord",2020,"pedro",200)
    rv=Revista("cocina en casa",2019,20,"semana")
    print(li.__str__())
    print(rv.__str__())

   
