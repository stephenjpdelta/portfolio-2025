\# SQL Project 01 — AHCA Polling Analysis



\*\*Dataset:\*\* `ahca\_polls.csv` (imported into SQLite as `ahca\_polls`)  

\*\*Tools:\*\* SQLite + DB Browser for SQLite  

\*\*Objective:\*\* Explore public polling responses to the American Health Care Act (AHCA), focusing on pollster activity, public opinion trends, question text patterns, and data quality.



---



\## 1. Dataset Description



The dataset contains polling results for AHCA-related questions.  

It includes the following columns:



\- \*\*Start\*\* — Poll start date  

\- \*\*End\*\* — Poll end date  

\- \*\*Pollster\*\* — Name of the polling organisation  

\- \*\*Favor\*\* — Percentage who favour the AHCA  

\- \*\*Oppose\*\* — Percentage who oppose the AHCA  

\- \*\*Url\*\* — Link to poll source (may be missing)  

\- \*\*Text\*\* — Exact survey wording  



---



\## 2. Key Questions Explored



The SQL script answers a range of analytical questions, including:



\- How many polls are in the dataset?  

\- How many distinct pollsters are there?  

\- Which pollsters are most active?  

\- What are the overall averages of Favor and Oppose?  

\- Which pollsters show the highest support or opposition?  

\- What is the earliest and most recent poll?  

\- How do favor/oppose levels vary by month?  

\- What distinct question texts appear?  

\- Which polls explicitly mention “health care”?  

\- Which polls show Favor > Oppose (and vice versa)?  

\- Are there polls with unusual totals (Favor + Oppose < 75 or > 95)?  

\- How many polls are missing URLs?  



---



\## 3. Methods Used



The SQL analysis uses:



\- \*\*Aggregation:\*\* COUNT, SUM, AVG, MIN, MAX  

\- \*\*Grouping:\*\* GROUP BY for pollster-level and monthly trends  

\- \*\*Filtering:\*\* WHERE for text search, missing URLs, and opinion comparisons  

\- \*\*Ordering \& limiting:\*\* ORDER BY, LIMIT  

\- \*\*String functions:\*\* SUBSTR() for month extraction  

\- \*\*Data quality checks:\*\* Identifying missing URLs and odd value totals  



---



\## 4. Insights \& Findings



Some notable patterns include:



\- Several pollsters appear frequently, showing uneven representation.  

\- Average levels of \*\*Oppose\*\* tend to exceed \*\*Favor\*\* across most polls.  

\- A subset of polls show very high opposition levels (top Oppose > 70%).  

\- Monthly trends indicate shifts over time in public support/opposition.  

\- URLs are missing for a number of polls, indicating incomplete metadata.  

\- Question wording varies widely; some mention “health care” directly while others do not.  



---



\## 5. Files in This Project



\- \*\*`project\_01\_polling\_analysis.sql`\*\* — Complete SQL analysis  

\- \*\*`project\_01\_summary.md`\*\* — This summary document  



---



\*\*Project Status:\*\* Complete. Ready for upload to GitHub.



