import unittest
from unittest.mock import Mock
from my_module import MyModule


class TestMyModule(unittest.TestCase):

    def test_describe_happy_path(self):
        atticus = Mock()
        atticus.description.return_value = 'Interview with Person 1'

        x = MyModule(atticus)

        self.assertEqual(x.describe(), 'Description: Interview with Person 1')

    def test_describe_sad_path(self):
        boo = Mock()
        boo.description.return_value = None

        x = MyModule(boo)

        self.assertEqual(x.describe(), 'The car is on fire, and there\'s no driver at the wheel')


if __name__ == '__main__':
    unittest.main()
