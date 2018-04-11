class MyModule:
    """This is our code - which we do want to test

    The constructor expects a description_provider (an instance
    of ThirdPartyModule) which it uses to create the string
    returned by its describe() method

    """

    def __init__(self, description_provider):
        self._description_provider = description_provider

    def describe(self):
        description = self._description_provider.description()

        if isinstance(description, str):
            return f'Description: {description}'
        elif isinstance(description, type(None)):
            return f'The car is on fire, and there\'s no driver at the wheel'
