import logging


class DoesLotsOfLogging:
    """
    Represents a class which does lots of logging, which we do not present when we run our tests
    """

    def __init__(self, stuff_to_do='Not provided'):
        if (stuff_to_do == 'Not provided'):
            logging.error('No argument passed to constructor')
        else:
            logging.info(stuff_to_do)

        self._stuff_to_do = stuff_to_do

    def get_stuff_to_do(self):
        logging.info('Getting stuff to do')
        return self._stuff_to_do
