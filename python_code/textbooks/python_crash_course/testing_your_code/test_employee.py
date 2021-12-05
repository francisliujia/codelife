import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.eric = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)


if __name__ == '__main__':
    unittest.main()