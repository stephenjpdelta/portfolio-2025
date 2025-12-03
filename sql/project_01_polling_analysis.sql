-- =========================================================
-- Project: SQL Project 01 – AHCA Polling Analysis
-- Dataset: ahca_polls.csv (imported into SQLite as table ahca_polls)
-- Author: [Your Name]
--
-- Description:
--   Exploratory analysis of polling data on the AHCA, including:
--   - Pollster activity and performance
--   - Overall favor vs oppose levels
--   - Trends over time
--   - Question text patterns
--   - Data quality checks (missing URLs, odd totals)
-- =========================================================


/***********************************************************
SECTION 1: DATASET OVERVIEW
Basic counts and sample rows to understand the dataset size
and structure.
***********************************************************/


-- Q01: Total number of polls in the dataset
-- Purpose: Get the overall size of the dataset.
SELECT 
    COUNT(*) AS total_polls
FROM ahca_polls;


-- Q02: Number of polls conducted by YouGov
-- Purpose: See how many polls are attributed specifically to YouGov.
SELECT 
    COUNT(*) AS yougov_polls
FROM ahca_polls
WHERE Pollster = 'YouGov';


-- Q03: Sample of rows from the polling table
-- Purpose: Inspect a few rows to understand columns and values.
SELECT 
    *
FROM ahca_polls
LIMIT 10;



/***********************************************************
SECTION 2: POLLSTERS & THEIR ACTIVITY
How many pollsters there are, who they are, and how busy they are.
***********************************************************/


-- Q04: Number of distinct pollsters
-- Purpose: Count how many unique pollsters appear in the dataset.
SELECT 
    COUNT(DISTINCT Pollster) AS distinct_pollsters
FROM ahca_polls;


-- Q05: List of distinct pollster names
-- Purpose: See the full list of pollsters in alphabetical order.
SELECT 
    DISTINCT Pollster
FROM ahca_polls
ORDER BY Pollster;


-- Q06: Distinct pollster–favor combinations
-- Purpose: Show unique combinations of Pollster and Favor value.
-- Note: This can reveal the spread of Favor values per pollster.
SELECT DISTINCT
    Pollster,
    Favor
FROM ahca_polls
ORDER BY Favor;


-- Q07: Number of polls per pollster
-- Purpose: See which pollsters are most active (by count of polls).
SELECT 
    Pollster,
    COUNT(*) AS num_polls
FROM ahca_polls
GROUP BY Pollster
ORDER BY num_polls DESC;


-- Q08: Average Favor per pollster
-- Purpose: Compare pollsters based on average Favor scores.
SELECT 
    Pollster,
    AVG(Favor) AS avg_favor
FROM ahca_polls
GROUP BY Pollster
ORDER BY avg_favor DESC;


-- Q09: Total Favor per pollster
-- Purpose: Sum of Favor values per pollster (workload × support).
SELECT 
    Pollster,
    SUM(Favor) AS total_favor
FROM ahca_polls
GROUP BY Pollster
ORDER BY total_favor DESC;


-- Q10: Average Favor and Oppose per pollster
-- Purpose: Compare pollsters on both support and opposition.
SELECT 
    Pollster,
    AVG(Favor)  AS avg_favor,
    AVG(Oppose) AS avg_oppose
FROM ahca_polls
GROUP BY Pollster
ORDER BY avg_favor DESC;


-- Q11: Descriptive statistics per pollster
-- Purpose: For each pollster, show:
--   - number of polls
--   - average favor
--   - average oppose
--   - first poll date
--   - last poll date
SELECT
    Pollster,
    COUNT(*)      AS num_polls,
    AVG(Favor)   AS avg_favor,
    AVG(Oppose)  AS avg_oppose,
    MIN(Start)   AS first_poll,
    MAX(End)     AS last_poll
FROM ahca_polls
GROUP BY Pollster
ORDER BY num_polls DESC;


-- Q12: All rows for a specific pollster (IPSOS)
-- Purpose: Drill down into one pollster’s individual polls.
SELECT 
    *
FROM ahca_polls
WHERE Pollster = 'IPSOS';



/***********************************************************
SECTION 3: OVERALL OPINION LEVELS
Aggregate favor/oppose values across the entire dataset.
***********************************************************/


-- Q13: Average Favor and Oppose (overall), rounded to 1 decimal
-- Purpose: Get central tendency of support vs opposition.
SELECT
    ROUND(AVG(Favor),  1) AS avg_favor,
    ROUND(AVG(Oppose), 1) AS avg_oppose
FROM ahca_polls;


-- Q14: Total Favor and total Oppose (overall)
-- Purpose: Sum all Favor and Oppose values across the dataset.
SELECT
    SUM(Favor)  AS total_favor,
    SUM(Oppose) AS total_oppose
FROM ahca_polls;



/***********************************************************
SECTION 4: DATE RANGE & TRENDS OVER TIME
Poll start/end dates and monthly favor/oppose trends.
***********************************************************/


-- Q15: Most recent poll end date
-- Purpose: See how up-to-date the polling data is.
SELECT 
    MAX(End) AS most_recent_poll_end
FROM ahca_polls;


-- Q16: Earliest poll start date
-- Purpose: See when the polling period begins.
SELECT 
    MIN(Start) AS earliest_poll_start
FROM ahca_polls;


-- Q17: Monthly average Favor and Oppose
-- Purpose: Create a 'month' value from Start date (assumes MM/DD/…)
--          and compute average Favor and Oppose per month.
SELECT
    SUBSTR(Start, 1, 2)            AS month,
    ROUND(AVG(Favor),  1)          AS avg_favor,
    ROUND(AVG(Oppose), 1)          AS avg_oppose
FROM ahca_polls
GROUP BY month
ORDER BY month;



/***********************************************************
SECTION 5: QUESTION TEXT ANALYSIS
Look at the distinct question wordings and health-care-related text.
***********************************************************/


-- Q18: Count of distinct question texts
-- Purpose: See how many unique question wordings are used.
SELECT 
    COUNT(DISTINCT Text) AS distinct_text_count
FROM ahca_polls;


-- Q19: List of distinct question texts
-- Purpose: Inspect all unique survey question texts.
SELECT DISTINCT
    Text
FROM ahca_polls
ORDER BY Text;


-- Q20: Polls where the question text mentions "health care"
-- Purpose: Filter polls whose text references health care explicitly.
SELECT 
    *
FROM ahca_polls
WHERE Text LIKE '%health care%';



/***********************************************************
SECTION 6: FAVOR VS OPPOSE OUTCOMES
Compare polls where Favor > Oppose vs Oppose > Favor, and extremes.
***********************************************************/


-- Q21: Polls where Favor is greater than Oppose
-- Purpose: Identify polls with net positive support.
SELECT 
    *
FROM ahca_polls
WHERE Favor > Oppose;


-- Q22: Polls where Oppose is greater than Favor
-- Purpose: Identify polls with net opposition.
SELECT 
    *
FROM ahca_polls
WHERE Oppose > Favor;


-- Q23: Count of polls where Oppose > Favor
-- Purpose: How many polls show net opposition?
SELECT 
    COUNT(*) AS polls_oppose_greater
FROM ahca_polls
WHERE Oppose > Favor;


-- Q24: Poll with the highest Favor value
-- Purpose: Find the single most favorable poll result.
SELECT 
    *
FROM ahca_polls
ORDER BY Favor DESC
LIMIT 1;


-- Q25: Poll with the highest Oppose value
-- Purpose: Find the single strongest opposition result.
SELECT 
    *
FROM ahca_polls
ORDER BY Oppose DESC
LIMIT 1;


-- Q26: Polls with unusual total (Favor + Oppose)
-- Purpose: Flag polls where Favor + Oppose is < 75 or > 95,
--          which may indicate undecided/other response patterns
--          or potential data issues.
SELECT 
    *
FROM ahca_polls
WHERE (Favor + Oppose) < 75
   OR (Favor + Oppose) > 95;



/***********************************************************
SECTION 7: URL COMPLETENESS & DATA QUALITY
Check which polls have missing or present URLs.
***********************************************************/


-- Q27: Count of polls without a URL
-- Purpose: Measure how many polls lack a web link (URL missing or blank).
SELECT 
    COUNT(*) AS polls_without_url
FROM ahca_polls
WHERE Url IS NULL OR Url = '';


-- Q28: Pollster and URL where a URL is present
-- Purpose: List pollsters with associated URLs (non-empty).
SELECT 
    Pollster,
    Url
FROM ahca_polls
WHERE Url IS NOT NULL
  AND Url <> '';
