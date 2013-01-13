'''
TODO Document here
'''

from json import JSONEncoder
from json import loads as jloads
from json import dumps as jdumps

from transmission_data import TransmissionData


def loads(serializedString):
    '''
    .. function:: loads(serializedString)
    Abstraction on json.loads to handle TransmissionData deserialization.

    Takes a serialized TransmissionData object and uses the json module
    to deserialize it.

    :param serializedString: The serialized TransmissionData
    :returns: A TransmissionData obect
    '''
    return jloads(
                    serializedString,
                    object_hook=_TransmissionDataSerializer.Decode,
                 )


def dumps(data, sort_keys=False):
    '''
    .. function:: dumps(data[, sorted=False])
    Abstraction on json.dumps to handle TransmissionData serialization.

    Takes a TransmissionData object and serializes it

    :param data: The data object to be serialized
    :param sort_keys: Optional to sort the json keys defaults to False
    :returns: A serialized TransmissionData string
    '''
    return jdumps(
                    data,
                    cls=_TransmissionDataSerializer,
                    sort_keys=sorted,
                 )


class _TransmissionDataSerializer(JSONEncoder):
    '''
    TODO Document here
    '''
    def default(self, obj):
        '''
        TODO Document here
        '''
        return {'data': obj.Data, 'time': obj.Time}

    @staticmethod
    def Decode(dct):
        '''
        TODO Document here
        '''
        if 'data' in dct:
            return TransmissionData(dct['data'], dct['time'])
        return dct
