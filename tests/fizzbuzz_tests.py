import unittest

from src.fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz__3_returns_fizz(self):
        self.assertEqual("fizz", fizz_buzz(3))

    def test_fizz_buzz_6_returns_fizz(self):
        self.assertEqual("fizz", fizz_buzz(6))

    def test_fizz_buzz_5_returns_buzz(self):
        self.assertEqual("buzz", fizz_buzz(5))

    def test_fizz_buzz_10_returns_fizzbuzz(self):
        self.assertEqual("buzz", fizz_buzz(10))

    def test_fizz_buzz_15_returns_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizz_buzz(15))

    def test_fizz_buzz_4_returns_4_as_str(self):
        self.assertEqual("4", fizz_buzz(4))