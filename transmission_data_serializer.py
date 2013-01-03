from json import JSONEncoder

from transmission_data import TransmissionData


class TransmissionDataSerializer(JSONEncoder):
    def default(self, obj):
        return {'data': obj.data, 'time': obj.time}

    @staticmethod
    def Decode(data):
        return TransmissionData(data['data'], data['time'])
