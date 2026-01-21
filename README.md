# 🏙️ Riyadh Real Estate — Data Analysis & Dashboard

Analyze real-estate prices in Riyadh and explore factors influencing market trends through interactive visualizations.

## Live Dashboard
- Streamlit App: https://riyadh-real-estate-tlxw6t3shmmyfqrteyzcyb.streamlit.app/

## Project Overview
This project explores Riyadh’s real estate market using:
- Data cleaning & preprocessing
- Feature engineering (e.g., `Price_per_m2`)
- Exploratory Data Analysis (EDA)
- A Streamlit dashboard for interactive exploration

## Repository Structure
- `app.py` — Streamlit dashboard
- `clean_data.csv` — cleaned dataset used by the dashboard
- `assets/` — images/icons used in the UI
- `requirements.txt` — project dependencies
- `README.md` — project documentation

## Objectives
- Clean and preprocess Riyadh real-estate data
- Explore pricing trends and district differences
- Highlight features that influence property prices
- Build an interactive dashboard for market exploration

## Data Cleaning & Preparation
- Handling missing values
- Fixing data types
- Removing duplicates
- Feature engineering (e.g., `Price_per_m2`)
- Exporting a cleaned dataset for dashboard use

## Exploratory Data Analysis
Includes:
- Price and area distributions
- Price per m² variation across districts
- Property characteristics vs price
- Visualizations such as bar charts and scatter plots

## Key Insights
- District/neighborhood has strong influence on price
- Property type and area significantly impact value
- High variation in price per m² among districts
- Some non-linear relationships observed

## Tech Stack
Python, pandas, numpy, matplotlib, streamlitو seaborn, scikit-learn

## How to Run Locally

### 1) Clone the repository
```bash
git clone https://github.com/Nujud123/Riyadh-Real-Estate.git
cd Riyadh-Real-Estate
```

### 2) Create & activate a virtual environment (Windows)
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the app
```bash
streamlit run app.py
```

## Dashboard Features

- Pricing trends

- Price per m² by district

- Compare property types

- Explore distributions & patterns

## Dataset

The dataset includes features such as:
price, area, district, property type, bedrooms, bathrooms, and more.

Clean version used by the app: `clean_data.csv`

## Future Enhancements

- Add predictive models

- Add more dashboard filters

- Map-based visualization (district-level mapping)

## Author

Nujud Almaleki
GitHub: https://github.com/Nujud123