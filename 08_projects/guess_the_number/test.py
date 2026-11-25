import unittest
from guess_the_number import random_number, guesses_plus, guess_count, message

class TestGuessTheNum(unittest.TestCase):
    def test_rn(self):
        for i in range(1000):
            self.assertGreaterEqual(random_number(),1)
            self.assertLessEqual(random_number(), 100)

    def test_gp(self):
        self.assertLessEqual(guesses_plus(), guess_count + 1)

    
    

if __name__ == "__main__":
    unittest.main()
