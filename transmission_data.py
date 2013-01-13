from time import time as CurrentTime


class TransmissionData:
    '''
    TODO Document here
    '''
    def __init__(self, data, time=None):
        '''
        TODO Document here
        '''
        self.Data = data
        self.Time = CurrentTime() if time is None else time
