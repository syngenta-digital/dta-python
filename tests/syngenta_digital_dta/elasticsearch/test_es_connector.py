import uuid
import unittest
import warnings
import json

from syngenta_digital_dta.elasticsearch.es_connector import ESConnector
from tests.syngenta_digital_dta.elasticsearch.mocks import MockESAdapter

class ESConnectorTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        warnings.simplefilter('ignore', ResourceWarning)
        self.maxDiff = None

    def test_class_port(self):
        mock_adapter = MockESAdapter()
        connector = ESConnector(mock_adapter)
        self.assertEqual(connector.port, mock_adapter.port)

    def test_class_port_nonlocalhost(self):
        mock_adapter = MockESAdapter('dev.aws.com')
        connector = ESConnector(mock_adapter)
        self.assertEqual(connector.port, mock_adapter.port)
