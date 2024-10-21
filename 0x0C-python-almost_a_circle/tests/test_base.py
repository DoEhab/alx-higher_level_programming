import unittest
from base import Base


class TestBase(unittest.TestCase):
    """
    Test class for base class
    """
    def test_base(self):
        b1 = Base()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
