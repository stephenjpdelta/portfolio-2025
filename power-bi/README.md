## AHCA Polling Data – Power BI Dashboard

### Overview
This project demonstrates an end-to-end analytics workflow using public polling data
related to the **American Health Care Act (AHCA)**.
The workflow covers raw CSV ingestion, SQL-based preparation, and a two-page
interactive Power BI dashboard.

The dashboard provides an overview of polling activity and public sentiment towards
the AHCA, with the ability to explore trends over time and compare results across
different pollsters.

---

### Data Source
The dataset is sourced from **FiveThirtyEight** and made available via **Kaggle**:

- *FiveThirtyEight – AHCA Polls Dataset*  
  https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-ahca-polls-dataset

The data is provided as a CSV file where each row represents a single poll.

---

### Data Structure (CSV)
Fields include:
- **Pollster** – Organisation conducting the poll
- **Favor (%)** – Percentage of respondents with a favourable view of the AHCA
- **Oppose (%)** – Percentage of respondents with an unfavourable view of the AHCA
- **Start / End** – Poll fieldwork dates
- **Text** – Survey question asked in the poll
- **URL** – Source link for the individual poll

Net favour is calculated as **Favor minus Oppose**.

---

### Data Preparation
- The CSV data was imported into **SQL Server** using SSMS
- SQL queries were used to clean, aggregate, and prepare poll-level data
- The curated dataset was then loaded into **Power BI Desktop** for modelling and visualisation

---

### Dashboard Structure

#### Page 1 – Polling Overview
- Total number of polls
- Average favour, oppose, and net favour across all polls
- Total polls by pollster
- Trend of average favour vs average oppose by poll start date
- Pollster slicer for interactive filtering

#### Page 2 – Pollster Comparison
- Days active per pollster (based on poll fieldwork periods)
- Average favour and average oppose by pollster

---

### Purpose
The dashboard is designed to provide a clear, high-level view of public sentiment
towards the American Health Care Act, while enabling comparison between pollsters
and exploration of sentiment trends over time.

---

### Tools Used
- SQL Server Management Studio (SSMS)
- T-SQL
- Power BI Desktop

---

### Screenshots
![Polling Overview](screenshots/page1_overview.png)
![Pollster Comparison](screenshots/page2_comparison.png)
