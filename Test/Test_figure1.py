import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCrimeDataPlotOne(unittest.TestCase):
    def test_plot_one_data_processing(self):
        # Create a mock dataframe to simulate the CSV file
        data = {
            'Value': ['50', '30', '70', '?'],
            'Sample size': ['100', '200', '300', '400'],
            'Time': ["2017/18, 2018/19 and 2019/20", "2017/18, 2018/19 and 2019/20", "2014/15, 2015/16 and 2016/17", "2017/18, 2018/19 and 2019/20"],
            'Geography': ['West Midlands', 'Some Region', 'West Midlands', 'Another Region'],
            'Age': ['16-24', '25-34', '16+', '16-24'],
            'Victims': ['50', '60', '100', '80']
        }

        crimeData = pd.DataFrame(data)

        # Filter data for the latest time period
        plotOne = crimeData[crimeData['Time'] == "2017/18, 2018/19 and 2019/20"]

        # Group by age to calculate averages and totals
        plotOne['Value'] = pd.to_numeric(plotOne['Value'], errors='coerce')
        plotOne['Victims'] = pd.to_numeric(plotOne['Victims'], errors='coerce')
        averageValues = plotOne.groupby('Age')['Value'].mean()
        totalVictims = plotOne.groupby('Age')['Victims'].sum()

        # Remove records for every age group
        averageValues = averageValues[averageValues.index != '16+']
        totalVictims = totalVictims[totalVictims.index != '16+']

        # Assertions to verify data processing
        self.assertFalse(averageValues.index.isin(['16+']).any())
        self.assertFalse(totalVictims.index.isin(['16+']).any())
        self.assertTrue(all(averageValues >= 0))
        self.assertTrue(all(totalVictims >= 0))

if __name__ == '__main__':
    unittest.main()