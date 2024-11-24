assert sum([1, 2, 3]) == 6, "Should be 6"
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2,2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


# The Test results we see allow us to visualize the errors we have. In this case it prompts the and assertion error that only happens when an assertion is false such as 5!=6 in which 5 is the sum total of the ints provided and we have a comment to the side of the error letting us know the proper solution.