import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday1 = calculate(2020, 2, 29)
        self.assertEqual(weekday1, -1)

        weekday2 = calculate(2012, 2, 29)
        self.assertEqual(weekday2, 2)

        weekday3 = calculate(2011, 2, 29)
        self.assertEqual(weekday3, -1)

        weekday4 = calculate('2011', 2, 29)
        self.assertEqual(weekday4, -1)

        weekday5 = calculate(2016, 7, 25)
        self.assertEqual(weekday5, 0)

        weekday6 = calculate(2017, 5, 12)
        self.assertEqual(weekday6, 4)

        weekday7 = calculate(2000, 13, 29)
        self.assertEqual(weekday7, -1)

        weekday8 = calculate(2017, 5, 9)
        self.assertEqual(weekday8, 1)

        retcode1 = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode1, 0)

        retcode2 = main(("--syear", "2001", "--month", "2", "--day", "30"))
        self.assertNotEqual(retcode2, 0)

        retcode3 = main(("--syear", "2001", "2", "--day", "30"))
        self.assertNotEqual(retcode3, 0)

        retcode4 = main(("--syear", "2001", "--month", "2", "--day", "30", "10"))
        self.assertNotEqual(retcode4, 0)

if __name__ == '__main__':
    unittest.main()
