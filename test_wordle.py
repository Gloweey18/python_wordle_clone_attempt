import unittest
import wordle as worldle
from unittest.mock import patch
from io import StringIO

@patch("sys.stdout",new_callable=StringIO)
class TestWordle(unittest.TestCase):
    def test_text_flie(self):
        file=worldle.get_words()
        self.assertIn("Shush",file)
        self.assertIn("Alive",file)
    @patch("sys.stdin","who\nif\nwhe4s\nwhere")
    def test_input(self,output):
        var=1
        guess=worldle.get_word(var)
        self.assertEqual(output.getvalue().strip(),"Your word should be 5 letters long\nGuess 1 : "+\
            "Your word should be 5 letters long\nGuess 1 : Please enter a word.\nGuess 1 : Guess 2")
        
        