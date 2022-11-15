import unittest
import main

class TestBot(unittest.TestCase):
    def test_get_word(self):
        result = main.get_word('старт')
    def test_find(self):
        result = main.get_word('Cтарт')

    def test_err(self):
        result = main.get_word('Start')
