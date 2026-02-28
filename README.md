# 🏠 Bengaluru Real Estate Investment Analysis & ML Dashboard

![image alt](https://github.com/suhailapathoor35-dotcom/Banglore-realestate/blob/971bb958b8844203c9c31073961634d72acf6740/dashboard%20bangluru.png)

## Dashboard
📌 Project Overview

This project performs an end-to-end real estate investment analysis on 13,000+ property listings from Bengaluru. The objective was to identify high-potential investment locations using data cleaning, feature engineering, predictive modeling, and interactive dashboard visualization.

The project combines Data Analytics and Machine Learning to simulate ROI, rental yield, and investment scoring.
## 🎯 Business Objective

Identify the best locations for property investment

Analyze price trends and area distribution

Simulate 5-year ROI and rental yield

Build a predictive model for property price estimation

Create an interactive dashboard for decision-making
## 🛠 Tools & Technologies

Python (Pandas, NumPy, Scikit-learn)

SQL (Data extraction & transformation)

Power BI (Dashboard & KPI Visualization)

Excel (Initial validation & formatting)
## 📊 Data Processing & Cleaning

Handled missing values and removed high-null columns (e.g., society)

Standardized total_sqft values and converted ranges to numeric

Removed price outliers using price-per-sqft filtering

Created new features:

price_per_sqft

rental_yield

roi_5yr (5-Year Return on Investment simulation)

investment_score (normalized scoring metric)

Eliminated extreme BHK and sqft anomalies
![image alt](https://github.com/suhailapathoor35-dotcom/Banglore-realestate/blob/971bb958b8844203c9c31073961634d72acf6740/page1st.png)
![image alt](https://github.com/suhailapathoor35-dotcom/Banglore-realestate/blob/971bb958b8844203c9c31073961634d72acf6740/IMAGE2.png)
## 🤖 Machine Learning Model

Algorithm Used: Linear Regression

Target Variable: Price

Features: total_sqft, bath, bhk, price_per_sqft

Model Performance:

R² Score: 0.71

The model explains 71% of the variance in property prices based on selected features.
## 📈 Dashboard Highlights (Power BI)

The interactive dashboard includes:

KPI Cards (Avg Price per Sqft, Avg ROI, Rental Yield, Best Location)

ROI Comparison by Location

Rental Yield Analysis

Investment Score Ranking

Scatter Plot (Price vs Sqft by BHK)

Dynamic Filters (Location, Price Category, BHK)

Top Identified Investment Location: Whitefield (based on investment scoring model)
## 🔍 Key Insights

Certain mid-priced locations offer higher ROI compared to premium zones.

Investment score normalization helps balance rental yield and capital appreciation.

## 🚀 Conclusion

This project demonstrates:

End-to-end data analytics workflow

Feature engineering for financial simulation

Supervised Machine Learning for regression modeling

Business-focused dashboard design

Investment-based data storytelling
Price per sqft is a strong driver of overall property valuation.
## 📂 Project Structure

Data Cleaning & Feature Engineering (Python)

ML Modeling (Scikit-learn)

Dashboard Development (Power BI)

Insight & Reporting
## 📌 Author

Suhaila P
Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning
