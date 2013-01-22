'''
Module for testing the TransmissionDataSerializer
'''
from unittest import TestCase


class TransmissionDataSerializerTests(TestCase):
    '''
    Class used to make unittest work. Tests TransmissionDataSerializer
    '''
    def setUp(self):
        '''
        Used for defualt setup of all tests
        '''
        self.ExpectedData = {'first': 1, 'second': 2}

    def test_SerializeWithTime(self):
        '''
        Tests serialization when the time is manually inserted.

        Uses json module directly and tests the serialization utility class that
        is used by the higher level abstractions in the module.
        '''
        from time import time
        from json import dumps
        from transmission_data import TransmissionData
        from transmission_data_serializer import _TransmissionDataSerializer
        expectedTime = time()
        expected = self.GenerateString(expectedTime)
        dataObjWithTime = TransmissionData(self.ExpectedData, expectedTime)
        actual = dumps(
                        dataObjWithTime,
                        cls=_TransmissionDataSerializer,
                        sort_keys=True,
                      )
        self.assertEqual(actual, expected)

    def test_SerializeWithOutTime(self):
        '''
        Tests serialization when the time is automatically assigned.

        Uses json module directly and tests the serialization utility class that
        is used by the higher level abstractions in the module.
        '''
        from json import dumps
        from transmission_data import TransmissionData
        from transmission_data_serializer import _TransmissionDataSerializer
        dataObjWithoutTime = TransmissionData(self.ExpectedData)
        expected = self.GenerateString(dataObjWithoutTime.Time)
        actual = dumps(
                        dataObjWithoutTime,
                        cls=_TransmissionDataSerializer,
                        sort_keys=True,
                      )
        self.assertEqual(actual, expected)

    def test_Deserialize(self):
        '''
        Tests deserialization.

        Uses json module directly and tests the serialization utility class that
        is used by the higher level abstractions in the module.
        '''
        from time import time
        from json import loads
        from transmission_data import TransmissionData
        from transmission_data_serializer import _TransmissionDataSerializer
        curTime = time()
        expected = TransmissionData(self.ExpectedData, curTime)
        jsonString = self.GenerateString(time())
        actual = loads(jsonString, object_hook=_TransmissionDataSerializer.Decode)
        self.assertEqual(actual.Time, expected.Time)
        self.assertEqual(actual.Data, expected.Data)

    def test_loads(self):
        '''
        Tests that the loads abstraction for JSON works.
        '''
        from time import time
        from transmission_data_serializer import loads
        expectedTime = time()
        serialzed = self.GenerateString(expectedTime)
        actualData = loads(serialzed)
        self.assertEqual(actualData.Time, expectedTime)
        self.assertEqual(actualData.Data, self.ExpectedData)

    def test_dumps(self):
        '''
        Tests that the dumps abstraction for JSON works.
        '''
        from transmission_data import TransmissionData
        from transmission_data_serializer import dumps
        dataObj = TransmissionData(self.ExpectedData)
        expected = self.GenerateString(dataObj.Time)
        actual = dumps(dataObj, True)
        self.assertEqual(actual, expected)

    @staticmethod
    def GenerateString(ExpectedTime):
        '''
        Utility function to create a JSON string with a given time.

        This is used for testing by building a json string that can be compared
        against to determine if serialization was successful. The param
        sets the value at the 'time' key.
        '''
        string = '{"data": {"first": 1, "second": 2}, "time": %s}'
        # we cast to a string instead of just using a float interpolation
        # because we need the percission to remain and casting
        # to a string maintains trailing 0s correctly
        string %= str(ExpectedTime)
        return string
