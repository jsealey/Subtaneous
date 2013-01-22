'''
Abstraction for the json package focused on TransmissionData serialzation.

This package offers simple methods for serialzation and deserialization of
TransmissionData objects using JSON specifications. It is dependant on the json
module.
'''

from json import JSONEncoder
from json import loads as jloads
from json import dumps as jdumps

from transmission_data import TransmissionData


def loads(serializedString):
    '''
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
    Used internally to customize JSON encoding and decoding.
    '''
    def default(self, obj):
        '''
        Customizes the encoding of a TransmissionData object.__class__

        Because dumps requires a class with a 'default' function to serialize a
        non built-in type, this function must exist.
        It returns a dictionary because the json module can serialize that
        structure natively.
        '''
        return {'data': obj.Data, 'time': obj.Time}

    @staticmethod
    def Decode(dct):
        '''
        Customizes deserialization of a JSON encoded TransmissionData object.__class__

        To decode the json module requires a function that will be called on all
        dictionaries (I think, or all structures).
        This function is a static method to encapsulate it with the encode
        method.
        It makes a dict with the 'data' key reserved for the TransmissionData
        itself.
        '''
        if 'data' in dct:
            return TransmissionData(dct['data'], dct['time'])
        return dct
