from unittest import TestCase


class _TransmissionDataSerializerTests(TestCase):
    '''
    TODO Document here
    '''
    def setUp(self):
        '''
        TODO Document here
        '''
        self.ExpectedData = {'first': 1, 'second': 2}

    def test_SerializeWithTime(self):
        '''
        TODO Document here
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
        TODO Document here
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
        TODO Document here
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
        Tests that the dumps abstraction for JSON works
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
        TODO Document here
        '''
        string = '{"data": {"first": 1, "second": 2}, "time": %s}'
        # we cast to a string instead of just using a float interpolation
        # because we need the percission to remain and casting
        # to a string maintains trailing 0s correctly
        string %= str(ExpectedTime)
        return string
