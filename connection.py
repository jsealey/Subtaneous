from json import dumps
from json import loads
from json import JSONEncoder
from json import JSONDecoder
from time import time


class Connection(object):
    """The object defining a coneection from one computer to another"""

    class _Data(object):
        """Internal use for sending and retrieving data from the connections"""
        def __init__(self, **kwargs):
            self.data = kwargs
            self.time = time()

    class _DataEncoder(JSONEncoder):
        """Used for serializing the _Data object"""
        def default(self, obj):
            return obj.__dict__

    def __init__(self, ip):
        self.ip = ip

    def send(self, **kwargs):
        sendData = dumps(_Data(kwargs), cls = _DataEncoder)
