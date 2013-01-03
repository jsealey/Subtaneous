from unittest import TestCase
import unittest
from time import time
from json import dumps

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
        expected = TransmissionDataSerializerTests.GenerateString(dataObjWithoutTime.time)
        actual = dumps(
                        dataObjWithoutTime,
                        cls=TransmissionDataSerializer,
                        sort_keys=True,
                      )
        self.assertEqual(actual, expected)

    @staticmethod
    def GenerateString(ExpectedTime):
        string = '{"data": {"first": 1, "second": 2}, "time": %f}'
        string %= ExpectedTime
        return string

suite = unittest.TestLoader().loadTestsFromTestCase(TransmissionDataSerializerTests)
unittest.TextTestRunner(verbosity=2).run(suite)
