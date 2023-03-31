import unittest
from translator import french_to_english, english_to_french
class TestEnglishFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('Hello'),None)# test if null is given output is null
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # tests when hello is given output is Bonjour
       
        
class TestFrenchEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("Bonjor"),None) # test if null is given output is null
        self.assertEqual( french_to_english("Bonjour"), "Hello")  # tests when hello is given output is Bonjour
       
        
unittest.main()