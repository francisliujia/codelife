import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('james', 'austin')
        self.assertEqual(formatted_name, 'James Austin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, formatted_name, 'Wolfgang Mozart Amadeus')


if __name__ == '__main__':
    unittest.main()