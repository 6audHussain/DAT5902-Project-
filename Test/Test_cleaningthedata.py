import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import sys
import importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

class TestCrimeDataProcessing(unittest.TestCase):
    @patch('subprocess.check_call')
    @patch('importlib.import_module')
    def test_install_and_import(self, mock_import_module, mock_check_call):
        # Simulate package already installed
        mock_import_module.side_effect = None
        install_and_import('dummy_package')
        mock_import_module.assert_called_with('dummy_package')
        mock_check_call.assert_not_called()

    def test_crime_data_column_removal(self):
        # Create a mock dataframe to simulate the CSV file
        data = {
            'Measure': ['some_measure'],
            'Ethnicity_type': ['type1'],
            'Time_type': ['type2'],
            'Geography_type': ['type3'],
            'Geography code': ['code1'],
            'Value_type': ['percent'],
            'Standard Error': [0.1],
            'Lower CI': [0.2],
            'Upper CI': [0.3],
            'Value': ['50'],
            'Sample size': ['100'],
            'Time': ["2014/15, 2015/16 and 2016/17"],
            'Geography': ['West Midlands Region']
        }

        crimeData = pd.DataFrame(data)

        # Drop columns
        crimeData = crimeData.drop(columns=['Measure', 'Ethnicity_type', 'Time_type', 'Geography_type', 'Geography code', 'Value_type', 'Standard Error', 'Lower CI', 'Upper CI'])
        self.assertNotIn('Measure', crimeData.columns)
        self.assertNotIn('Ethnicity_type', crimeData.columns)

if __name__ == '__main__':
    unittest.main()
