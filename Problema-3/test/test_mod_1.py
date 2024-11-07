# tests/test_mcd_calculadora.py

import unittest
from src.modulo_1 import mcd_euclides

class TestMcdCalculadora(unittest.TestCase):
    # Prueba de casos básicos
    def test_mcd_10_5(self):
        self.assertEqual(mcd_euclides(10, 5), 5)
    
    def test_mcd_48_18(self):
        self.assertEqual(mcd_euclides(48, 18), 6)
    
    def test_mcd_56_98(self):
        self.assertEqual(mcd_euclides(56, 98), 14)

    # Prueba con números pequeños
    def test_mcd_7_3(self):
        self.assertEqual(mcd_euclides(7, 3), 1)
    
    def test_mcd_101_10(self):
        self.assertEqual(mcd_euclides(101, 10), 1)

    # Prueba con un número primo
    def test_mcd_13_29(self):
        self.assertEqual(mcd_euclides(13, 29), 1)

    # Prueba con números negativos (la función debe manejar números negativos correctamente)
    def test_mcd_negativos(self):
        self.assertEqual(mcd_euclides(-48, 18), 6)
        self.assertEqual(mcd_euclides(48, -18), 6)
        self.assertEqual(mcd_euclides(-48, -18), 6)

if __name__ == '__main__':
    unittest.main()
