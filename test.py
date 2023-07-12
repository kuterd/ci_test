import unittest

class TestSimple(unittest.TestCase):
    def test_addition(self):
        return self.assertEqual(123 + 123, 246)
    def test_broken(self):
        return self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
