import unittest
import rock_paper_scissors
from rock_paper_scissors import playerName, giveBotName


class TestRockPaperScissor(unittest.TestCase):
    def test_playerName(self):
        x = playerName("Elia")
        self.assertEqual(type(x), str)


if __name__ == "__main__":
    unittest.main()