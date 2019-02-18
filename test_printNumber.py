import unittest
from printNumber import printnumbers


class TestPrintNumber(unittest.TestCase):
    number = 6;

    def test_valid_number(self):
        print('Checking Number Validity ')
        self.assertTrue(printnumbers(self.number) > 0, "Input number is invalid");


if __name__ == '__main__':
    unittest.main()
