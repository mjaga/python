import unittest
from sumAmount import SumAmount


class TestSumObject(unittest.TestCase):
    sumAmtObj = SumAmount({'Rick': 20, 'Amit': -42});

    def test_is_positive_total(self):
        print('Is Total Sum Amount positive?')
        self.assertTrue(self.sumAmtObj.aggregatetotal() > 0, "Total Sum Amount is negative");


if __name__ == '__main__':
    unittest.main()