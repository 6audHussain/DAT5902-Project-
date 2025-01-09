import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCrimeDataPlotThree(unittest.TestCase):
    def test_plot_three_combined_data(self):
        # Create mock data for income and victimization rates
        income_data = {
            'Ethnicity (Mapped)': ['Asian/Asian British', 'Black/African/Caribbean/Black British', 'White'],
            'Value': [70, 60, 80]
        }
        victim_data = {
            'Ethnicity': ['Asian/Asian British', 'Black/African/Caribbean/Black British', 'White'],
            'Value': [20, 30, 10]
        }

        incomeData = pd.DataFrame(income_data)
        victimData = pd.DataFrame(victim_data)

        # Group and calculate averages
        incomeByEthnicity = incomeData.groupby('Ethnicity (Mapped)')['Value'].mean()
        victimRateByEthnicity = victimData.groupby('Ethnicity')['Value'].mean()

        # Align and combine data
        combinedData = pd.DataFrame({
            'IncomePercentage(Households>GBP2000)': incomeByEthnicity,
            'AverageVictimizationRate(%)': victimRateByEthnicity
        }).dropna()

        # Verify the combined data
        self.assertEqual(len(combinedData), 3)  # Ensure all ethnicities are included
        self.assertIn('IncomePercentage(Households>GBP2000)', combinedData.columns)
        self.assertIn('AverageVictimizationRate(%)', combinedData.columns)
        self.assertTrue(all(combinedData['IncomePercentage(Households>GBP2000)'] > 0))
        self.assertTrue(all(combinedData['AverageVictimizationRate(%)'] > 0))

if __name__ == '__main__':
    unittest.main()
