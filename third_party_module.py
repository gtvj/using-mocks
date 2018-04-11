import urllib.request
import json


class ThirdPartyModule:

    def __init__(self, url='not provided'):
        # Makes HTTP request to external service and sets _contents to decoded response
        self._contents = urllib.request.urlopen(url).read().decode('utf-8')

    def response_description(self):
        # Returns string representing the description property
        return json.loads(self._contents)['description']
