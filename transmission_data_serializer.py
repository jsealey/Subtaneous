from json import JSONEncoder

from transmission_data import TransmissionData


class TransmissionDataSerializer(JSONEncoder):
    def default(self, obj):
        return {'data': obj.Data, 'time': obj.Time}

    @staticmethod
    def Decode(dct):
        if 'data' in dct:
            return TransmissionData(dct['data'], dct['time'])
        return dct
