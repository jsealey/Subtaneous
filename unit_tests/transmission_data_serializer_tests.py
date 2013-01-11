from unittest import TestCase
import unittest
from time import time
from json import dumps, loads

from transmission_data import TransmissionData
from transmission_data_serializer import TransmissionDataSerializer


class TransmissionDataSerializerTests(TestCase):
    def setUp(self):
        self.ExpectedData = {'first': 1, 'second': 2}

    def test_SerializeWithTime(self):
        expectedTime = time()
        expected = TransmissionDataSerializerTests.GenerateString(expectedTime)
        dataObjWithTime = TransmissionData(self.ExpectedData, expectedTime)
        actual = dumps(
                        dataObjWithTime,
                        cls=TransmissionDataSerializer,
                        sort_keys=True,
                      )
        self.assertEqual(actual, expected)

    def test_SerializeWithOutTime(self):
        dataObjWithoutTime = TransmissionData(self.ExpectedData)
        expected = TransmissionDataSerializerTests.GenerateString(dataObjWithoutTime.Time)
        actual = dumps(
                        dataObjWithoutTime,
                        cls=TransmissionDataSerializer,
                        sort_keys=True,
                      )
        self.assertEqual(actual, expected)

    def test_Deserialize(self):
        curTime = time()
        expected = TransmissionData(self.ExpectedData, curTime)
        jsonString = TransmissionDataSerializerTests.GenerateString(time())
        actual = loads(jsonString, object_hook=TransmissionDataSerializer.Decode)
        self.assertEqual(actual.Time, expected.Time)
        self.assertEqual(actual.Data, expected.Data)

    @staticmethod
    def GenerateString(ExpectedTime):
        string = '{"data": {"first": 1, "second": 2}, "time": %s}'
        # we cast to a string instead of just using a float interpolation
        # because we need the percission to remain and casting
        # to a string maintains trailing 0s correctly
        string %= str(ExpectedTime)
        return string

suite = unittest.TestLoader().loadTestsFromTestCase(TransmissionDataSerializerTests)
unittest.TextTestRunner(verbosity=2).run(suite)
