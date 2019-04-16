import unittest

from no_days_christmas.attempt import get_no_presents_from_true_love
from no_days_christmas.attempt import bubble_sort

class ChristmasTest(unittest.TestCase):

    def test_true_love_presents(self):
        ans = [1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286,
               364, 455, 560, 680, 816, 969, 1140, 1330, 1540]
        for no_christmas_days, answer in enumerate(ans):
            self.assertEqual(get_no_presents_from_true_love(no_christmas_days+1), answer)

    def test_bubble_sort(self):
        array = [3, 4, 5, 2, 3, 3, 4, 4, 3, 35, 3, 4, 9, 10, 11, 2, 3, 2, 43]
        answer = [43, 35, 11, 10, 9, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2]
        bubble_answer = bubble_sort(array)

        for ans, prog_ans in zip(answer, bubble_answer):
            self.assertEqual(ans, prog_ans)


if __name__ == "__main__":
    CT = ChristmasTest()
    CT.test_true_love_presents()
