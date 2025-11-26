# Sales Analysis Project

A Python project that analyzes sales data from an SQLite database and generates visual reports.

## Project Description

This project demonstrates:
- SQLite database operations in Python
- SQL query execution and data analysis
- Data visualization with matplotlib
- Sales reporting and summary generation

## Features

- Creates and populates an SQLite database with sales data
- Runs SQL queries to analyze sales performance
- Generates summary reports in the console
- Creates bar charts visualizing revenue by product

## Files

- `create_database.py` - Creates and populates the SQLite database
- `sales_analysis.py` - Main analysis script with queries and visualization
- `sales_data.db` - SQLite database (ignored in git)
- `sales_chart.png` - Generated chart (ignored in git)

## Installation & Usage

1. Clone this repository:

       (https://github.com/BasavarjYN/sales-analysis-project-task7.git)

2.Run the database setup:

    python create_database.py

3.Run the analysis:

    python sales_analysis.py

4.Requirements
Python 3.x

pandas

matplotlib

5.Install requirements:

      pip install pandas matplotlib

6.Sample Output
The script generates:

Console output with sales summaries

Bar chart saved as sales_chart.png
