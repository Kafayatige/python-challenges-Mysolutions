import unittest
from prime_number import is_prime

class PrimeNumberTestCase(unittest.TestCase):
    def test_valid_prime_numbers_7(self):
        self.assertTrue(is_prime(7))

    def test_invalid_minus2(self):
        with self.assertRaises(ValueError):
            is_prime(-2)

    def test_invalid_strings(self):
      with self.assertRaises(TypeError):
          is_prime("19")

    def test_not_prime_number(self):
        self.assertFalse(is_prime(90))
