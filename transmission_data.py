from time import time as CurrentTime


class TransmissionData(object):
    '''Class to handle packaging data with a time stamp'''
    def __init__(self, data, time=None):
        self.Data = data
        self.Time = CurrentTime() if not time else time
