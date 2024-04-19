import unittest
def fibonacci(n):
    if n == (0,1):
        return n
    else:
        fibonacci(n-1)+fibonacci(n-2)
    #Suerte!
    
    
class TestFibonacci(unittest.TestCase):
    def test_with_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)
    
    def test_with_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    
    def test_with_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 2)
    
    def test_with_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 2)
    
    def test_with_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    
    def test_with_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)
    



unittest.main()