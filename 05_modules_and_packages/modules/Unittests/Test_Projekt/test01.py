import unittest

class TestMath(unittest.TestCase):
  def test_addition(self):
    self.assertEqual(2 + 2, 4)
    print('Addition test passed')

suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')