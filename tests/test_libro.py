import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from libro import Libro
class TestLibro(unittest.TestCase):
   
  
    def test__init__(self):
        valor_esperado_titulo = "overlord"
        valor_esperado_año = 2020
        valor_esperado_autor = "pedro"
        valor_esperado_numero_paginas = 200

        mi_cuenta =Libro("overlord",2020,"pedro",200)
        self.assertEqual(valor_esperado_titulo, mi_cuenta.titulo)
        self.assertEqual(valor_esperado_año, mi_cuenta.añoPublicacion)
        self.assertEqual(valor_esperado_autor, mi_cuenta.autor)
        self.assertEqual(valor_esperado_numero_paginas, mi_cuenta.numeroPaginas)
        
if __name__ == '__main__':
    unittest.main()
