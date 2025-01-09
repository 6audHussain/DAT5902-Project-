import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCrimeDataPlotTwo(unittest.TestCase):
    def test_plot_two_trendline(self):
        # Create mock data for Plot Two
        data = {
            'Age': ['16-24', '25-34', '35-44', '45-54', '55-64'],
            'Value': [50, 40, 30, 20, 10]
        }
        averageValues = pd.Series(data['Value'], index=data['Age'])

        # Numeric indices for age groups
        age_indices = np.arange(len(averageValues))

        # Fit a linear regression model to the data
        coefficients = np.polyfit(age_indices, averageValues.values, 1)
        trendline = np.poly1d(coefficients)

        # Verify the coefficients and trendline calculation
        self.assertEqual(len(coefficients), 2)  # Should return slope and intercept
        self.assertTrue(np.allclose(trendline(age_indices), coefficients[0] * age_indices + coefficients[1]))

if __name__ == '__main__':
    unittest.main()
