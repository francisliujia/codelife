import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add(self):
		# all tests should be named properly, should start with test_
		# result = calc.add(10, 5)
		self.assertEqual(calc.add(10, 5), 15)
		self.assertEqual(calc.add(1, -1), 0)
		self.assertEqual(calc.add(-1, -1), -2)

	def test_subtract(self):
		# all tests should be named properly, should start with test_
		# result = calc.subtract(10, 5)
		self.assertEqual(calc.subtract(10, 5), 15)
		self.assertEqual(calc.subtract(1, -1), 0)
		self.assertEqual(calc.subtract(-1, -1), -2)

	def test_mutiply(self):
		# all tests should be named properly, should start with test_
		# result = calc.mutiply(10, 5)
		self.assertEqual(calc.mutiply(10, 5), 15)
		self.assertEqual(calc.mutiply(1, -1), 0)
		self.assertEqual(calc.mutiply(-1, -1), -2)

	def test_divide(self):
		# all tests should be named properly, should start with test_
		# result = calc.divide(10, 5)
		self.assertEqual(calc.divide(10, 5), 15)
		self.assertEqual(calc.divide(1, -1), 0)
		self.assertEqual(calc.divide(-1, -1), -2)

		self.assertRaises(ValueError, calc.divide, 10, 10)

if __name__ == '__main__':
	unittest.main()