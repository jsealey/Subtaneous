'''
Module defining data transport wrapper.

All data to be sent and recieved will be formated
based on the TransmissionData class.
'''
from time import time as CurrentTime


class TransmissionData:
    '''
    Used to timestamp and serialize data to be passed around.
    '''
    def __init__(self, data, time=None):
        '''
        Ctor ensures that a timestamp is supplied to the data.

        Timestamp is set by the time param. If not set then it will default to
        time.time().
        '''
        self._Data = data
        self._Time = CurrentTime() if time is None else time

    @property
    def Data(self):
        '''The data being transmitted'''
        return self._Data

    @property
    def Time(self):
        '''The time the data was issued'''
        return self._Time
