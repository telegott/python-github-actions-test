import unittest

from app.adder import Adder


class TestAdder(unittest.TestCase):

    def test_add(self):
        adder = Adder(number=5)
        self.assertEqual(adder.add(5), 9)
