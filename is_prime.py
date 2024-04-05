import unittest

    
def is_prime(n):
# Comenzamos el bucle desde 2, ya que ningún número menor a 2 puede ser primo.
# Terminamos el bucle en int(n/2) + 1, ya que ningún número mayor que la mitad de n puede dividir a n.
    for i in range(2, int(n/2) + 1):
        # Si n es divisible por i, entonces n no es primo, así que devolvemos False.
        if (n % i) == 0:
            return False
# Si el bucle termina sin encontrar ningún divisor, entonces n es primo, así que devolvemos True.
    return True
    


class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_prime(1)
        self.assertEqual(result, True)
    
    def test_2(self):
        result = is_prime(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_prime(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_prime(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_prime(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_prime(6)
        self.assertEqual(result, False)


unittest.main()
