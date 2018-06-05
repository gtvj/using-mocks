import unittest
from unittest.mock import MagicMock
import logging
from libraries.does_lots_of_logging import DoesLotsOfLogging


class TestDoesLotsOfLogging(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_constructor_with_argument(self):
        x = DoesLotsOfLogging('Buy paint')

        self.assertEqual(x.get_stuff_to_do(), 'Buy paint')

    def test_constructor_missing_argument(self):
        y = DoesLotsOfLogging()

        self.assertEqual(y.get_stuff_to_do(), 'Not provided')

if __name__ == '__main__':
    unittest.main()
