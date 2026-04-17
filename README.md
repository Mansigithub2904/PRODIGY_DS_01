# Task 01 - Data Visualization

## Objective
Create a bar chart or histogram to visualize the distribution of data.

## Dataset
World Population Dataset (World Bank)

## Project Structure
Task-01/
│── data/
│── scripts/
│── outputs/

## Steps Performed
1. Downloaded dataset from GitHub
2. Cleaned data:
   - Removed unnecessary columns
   - Converted data from wide to long format
   - Handled missing values
3. Created visualizations:
   - Histogram (Population distribution)
   - Bar chart (Top 10 countries by population)

## Tools Used
- Python
- Pandas
- Matplotlib

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run data cleaning:
   python scripts/data_cleaning.py

3. Run visualization:
   python scripts/visualization.py
   python scripts/visualization2.py

## Output
- outputs/histogram.png
- outputs/barchart.png
