import unittest
from args_kwargs import buscar_persona



class TestBuscarPersona(unittest.TestCase):
    def test_persona_encontrada(self):
        id_esperado = 2
        id_real = buscar_persona('Ana', 'Jimenez')
        self.assertEqual(id_esperado, id_real)

    def test_persona_no_encontrada(self):
        id_esperado = None
        id_real = buscar_persona('María', 'López')
        self.assertEqual(id_esperado, id_real)

    def test_nombres_incorrectos(self):
        id_esperado = 1
        id_real = buscar_persona('Melina', 'Navarro')
        self.assertEqual(id_esperado, id_real)

    def test_apellidos_incorrectos(self):
        id_esperado = None
        id_real = buscar_persona('Juan', 'Pérez García')
        self.assertEqual(id_esperado, id_real)

if __name__ == '__main__':
    unittest.main()
