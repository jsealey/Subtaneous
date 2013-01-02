from time import time as CurrentTime


class TransmissionData(object):
    '''Class to handle packaging data with a time stamp'''
    def __init__(self, data, time=None):
        self.data = data
        self.time = CurrentTime() if not time else time
