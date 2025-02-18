import unittest
from  models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for base class
    """
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b1.id, 10)

if __name__ == '__main__':
    unittest.main()
