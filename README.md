# Nigeria Inflation Dashboard

An end-to-end data analysis project tracking Nigeria's Consumer Price Index (CPI) and inflation trends using data from the **National Bureau of Statistics (NBS)**.

## Project Overview

This project analyses Nigeria's inflation landscape — headline CPI, food inflation, core inflation, and urban vs. rural breakdowns — using Python for data processing and Power BI for interactive dashboards.

## Key Insights
- Food inflation has consistently outpaced headline CPI by 3-6 percentage points
- Urban centres (Lagos, Abuja) experience faster price transmission than rural zones
- Energy price shocks (PMS deregulation, FX pass-through) show clear CPI lag effects
- Naira depreciation correlates with a 45-60 day import-price transmission lag

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python (pandas, matplotlib, seaborn) | Data cleaning & EDA |
| Power BI | Interactive dashboards |
| Excel | Raw NBS data formatting |
| Jupyter Notebook | Analysis pipeline |

## Project Structure
```
nigeria-inflation-dashboard/
├── data/
│   ├── raw/                    # Raw NBS CPI data (CSV)
│   └── processed/              # Cleaned and transformed data
├── notebooks/
│   └── inflation_analysis.ipynb
├── dashboard/
│   └── screenshots/            # Dashboard PNG exports
├── src/
│   └── data_pipeline.py
└── README.md
```

## Data Sources
- [NBS Nigeria](https://nigerianstat.gov.ng/) — CPI & Inflation Reports
- [CBN Statistical Bulletin](https://www.cbn.gov.ng/)
- [World Bank Open Data](https://data.worldbank.org/country/NG)

## How to Run
```bash
git clone https://github.com/TheKingSegun/nigeria-inflation-dashboard.git
cd nigeria-inflation-dashboard
pip install -r requirements.txt
jupyter notebook notebooks/inflation_analysis.ipynb
```

## About
Built by **David** — Senior Data Analyst with expertise in Nigerian macroeconomic data and business analytics.
