import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from revista import Revista
class TestRevista(unittest.TestCase):
    def test__init__(self):
        valor_esperado_titulo = "cocina en casa"
        valor_esperado_año = 2019
        valor_esperado_numRe = 20
        valor_esperado_nomRe = "semana"

        mi_cuenta =Revista("cocina en casa",2019,20,"semana")
        self.assertEqual(valor_esperado_titulo, mi_cuenta.titulo)
        self.assertEqual(valor_esperado_año, mi_cuenta.añoPublicacion)
        self.assertEqual(valor_esperado_numRe, mi_cuenta.numRevista)
        self.assertEqual(valor_esperado_nomRe, mi_cuenta.nomRevistas)
        
if __name__ == '__main__':
    unittest.main()
