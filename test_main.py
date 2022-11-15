import unittest
import main

class TestBot(unittest.TestCase):
    def test_get_word(self):
        print('![] test lower case')
        main.get_word('старт')
        print('![] test upper case')
        main.get_word('Старт')
        print('![] test caps lock')
        main.get_word('СТАРТ')

