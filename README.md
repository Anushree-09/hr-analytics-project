# HR Analytics ETL Pipeline & Dashboard

# Overview
Developed an end-to-end ETL pipeline using Python to process HR data, load it into MySQL, and build an interactive Power BI dashboard to analyze employee attrition and workforce insights.

# Tech Stack
- Python (Pandas, SQLAlchemy)
- MySQL
- Power BI

# ETL Process
- Extract: Loaded HR dataset from CSV  
- Transform: Cleaned data, handled missing values, created age groups, and converted attrition to numeric  
- Load: Stored processed data in MySQL (`hr_analytics` table)  

# Dashboard
Power BI Report: https://app.powerbi.com/groups/me/list?experience=power-bi

# Key Insights:
- Employee Count & Attrition Rate  
- Attrition by Department & Job Role  
- Workforce Distribution (Age, Gender, Department)  
- Salary Analysis by Job Role  

# Run the Project
```bash
pip install -r requirements.txt
python main.py
