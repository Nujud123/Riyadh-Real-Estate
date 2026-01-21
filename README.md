# 🏙️ Riyadh Real Estate — Data Analysis & Dashboard

Analyze real-estate prices in Riyadh and uncover the factors influencing market trends


## Project Overview

This project explores Riyadh’s real estate market through data cleaning,
feature engineering, exploratory analysis, and interactive
visualizations.
A Streamlit dashboard was built to help users understand pricing
patterns, neighborhood trends, and key factors affecting property
values.

Live Dashboard:



## Repository Structure

app.py
clean_data.csv
requirements.txt
README.md


## Objectives

-   Clean and preprocess real-estate data from Riyadh
-   Explore pricing trends and neighborhood differences
-   Identify features most influential to property prices
-   Build an interactive dashboard for market exploration


## Data Cleaning & Preparation

-   Handling missing values
-   Fixing data types
-   Removing duplicates
-   Engineering features such as Price_per_m2
-   Exporting cleaned dataset for dashboard


## Exploratory Data Analysis

Includes:
- Price and area distributions
- Price per m² variation across districts
- Property characteristics vs. price
- Heatmaps, bar charts, scatterplots


## Key Insights

-   Neighborhood strongly influences price
-   Property type and area have significant impact
-   High variation in price per m² among districts
-   Some non-linear relationships observed


## Tech Stack

Python, pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit,
Jupyter


## How to Run

Clone: git clone https://github.com/Nujud123/Riyadh-Real-Estate.git

Virtual Environment: 
python -m venv .venv
.\.venv\Scripts\Activate.ps1    

Install: pip install -r requirements.txt

Run: streamlit run app.py


## Dashboard Features

-   Pricing trends
-   Price per m² by district
-   Compare property types
-   Explore distributions & correlations


## Dataset

Includes: price, area, neighborhood, property type, bedrooms, bathrooms,
and more.
Clean version: clean_data.csv


## Future Enhancements

-   Add predictive models
-   More dashboard filters
-   Map-based visualization

## Author

Nujud Almaleki
GitHub: https://github.com/Nujud123


Support
