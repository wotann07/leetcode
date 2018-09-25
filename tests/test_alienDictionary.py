from unittest import TestCase

from alien_dictionary import AlienDictionary


class TestAlienDictionary(TestCase):
    def test_get_alphabet(self):
        alien_d = AlienDictionary(['baa', 'abcd', 'abca', 'cab', 'cad'], 4)
        self.assertTrue(alien_d.get_alphabet())
