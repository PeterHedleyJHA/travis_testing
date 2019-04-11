import unittest

from no_days_christmas.attempt import get_no_presents_from_true_love

class ChristmasTest(unittest.TestCase):

    def test_true_love_presents(self):
        ans = [1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286,
               364, 455, 560, 680, 816, 969, 1140, 1330, 1540]
        for no_christmas_days,answer in enumerate(ans):
            self.assertEqual(get_no_presents_from_true_love(no_christmas_days+1),answer)


if __name__=="__main__":
    ct = ChristmasTest()
    ct.test_true_love_presents()
