# DAT5902-Project-# DAT5902-Project-# Exploring Crime Victimisation Trends in the UK
## An Analysis of Trends and Patterns

---

## 1. Overview
This repository contains an analysis of crime victimisation trends in the UK, focusing on demographic and socio-economic disparities. Using datasets spanning multiple years, the analysis examines victimisation rates in relation to age, ethnicity, income, and geography. The goal is to uncover patterns that can inform policymakers and community initiatives aimed at reducing crime and its impact.

The primary research questions include:
1. What trends in crime victimisation are observable across age groups over time?
2. How do victimisation rates correlate with income levels and ethnicity?
3. How do crime victimisation rates align with population demographics in specific areas, such as London?

The analysis leverages datasets on crime victimisation, household income, and population demographics. Insights derived from this study can guide policy development and resource allocation to enhance public safety and address systemic inequalities.

---

## 2. Project Structure
- **`.circleci/`**: Configuration files for CI/CD integration for automated testing.
- **`Visualisations/`**: Stores visualisations and plots generated from the analysis.
- **`Test/`**: Contains test files to ensure data integrity and script correctness.
- **`victims-of-crime-data.csv`**: The primary dataset on crime victimisation.
- **`household-income-2021.csv`**: Dataset on household income levels by ethnicity.
- **`population-by-ethnicity-and-region-2021.csv`**: Dataset on ethnicity numbers in different regions.
- **`README.md`**: Project documentation and usage instructions.
- **`DatasetCode.py`**: Python script for data preprocessing, analysis, and visualisation.
- **`requirements.txt`**: Python dependencies required for the analysis.

----

## 3. Datasets
### Crime Victimisation Data
- Focus: Victimisation rates by age, ethnicity, and geography (2014–2020).
- Key variables: Age, Ethnicity, Geography, Victimisation Rate, Sample Size.
- Preprocessing: Removed irrelevant columns, filtered invalid data, and standardised geographic labels.

### Household Income Data
- Focus: Income distribution by ethnicity, particularly households earning above GBP 2,000.
- Key variables: Ethnicity, Income Brackets, and Time Periods.
- Preprocessing: Mapped ethnicities to align with victimisation data and filtered relevant income brackets.

### Population Demographics Data
- Focus: Population percentages by ethnicity in UK regions.
- Key variables: Ethnicity, Geography, and Population Percentages.
- Preprocessing: Mapped ethnicities, filtered for London-specific data, and retained relevant variables.

---

## 4. How to Run
To run the analysis locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/6audHussain/DAT5902-Project-.git 
   cd DAT5902-Project-.git 
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the data analysis script:
   ```bash
   python DatasetCode.py
   ```

4. Run the test suite:
   ```bash
   pytest Test/
   ```

5. Visualise the results:
   Navigate to the `Visualisations/` folder to view the generated plots.

---
