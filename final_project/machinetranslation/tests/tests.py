import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        with self.assertRaises(ValueError):
            french_to_english(None) # Test when the input is null
        self.assertEqual(french_to_english('Bonjour'),'Hello') # Test when the input Bonjour

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        with self.assertRaises(ValueError):
            english_to_french(None) # Test when the input is null
        self.assertEqual(english_to_french('Hello'),'Bonjour') # Test when the input Bonjour
        


unittest.main()