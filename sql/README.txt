## AHCA Polling Data – SQL Analysis (SQLite)

### Overview
This project focuses on analysing polling data related to the
**American Health Care Act (AHCA)** using SQL.
The analysis was carried out using **SQLite**, with queries executed via
**DB Browser for SQLite**.

The project demonstrates the use of SQL for data exploration,
aggregation, and metric calculation, independent of BI or reporting tools.

---

### Data Source
The dataset used is the *FiveThirtyEight AHCA Polls* dataset, sourced via Kaggle:

https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-ahca-polls-dataset

The raw data is provided as a CSV file (`ahca_polls.csv`), where each row
represents a single poll.

---

### Data Structure
Key fields include:
- **Pollster**
- **Favor (%)**
- **Oppose (%)**
- **Start / End**
- **Text** (poll question)
- **URL** (source link)

---

### Analysis Approach
- Imported the CSV file into an SQLite database
- Executed approximately **25 SQL queries** to explore and analyse the data
- Queries covered:
  - Aggregations and summary statistics
  - Grouping by pollster
  - Time-based analysis using poll start and end dates
  - Calculation of derived metrics such as **net favour**

All analysis was performed directly in SQL without the use of SQL Server
or BI tools.

---

### Tools Used
- SQLite
- DB Browser for SQLite
- SQL

---

### Related Projects
The same dataset is also used in a separate Power BI dashboard project,
where SQL Server is used for data preparation and visualisation.
This SQL project focuses purely on querying and analysis using SQLite.
