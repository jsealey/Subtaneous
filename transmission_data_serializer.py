from json import JSONEncoder

from transmission_data import TransmissionData


class TransmissionDataSerializer(JSONEncoder):
    def default(self, obj):
        pass

    @staticmethod
    def Encode(data):
        pass