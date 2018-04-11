import urllib.request
import json


class ThirdPartyModule:
    """Represents someone else's code - which we don't want to test

    The constructor takes a URL and uses this to request a JSON object from
    an API. It then assigns the result to the private _contents attribute.

    The class exposes a description method which returns a string representing
    the 'description' property of the returns JSON object

    """

    def __init__(self, url='not provided'):
        # Makes HTTP request to external service and sets _contents to decoded response
        self._contents = urllib.request.urlopen(url).read().decode('utf-8')

    def description(self):
        # Returns string representing the description property
        return json.loads(self._contents)['description']
