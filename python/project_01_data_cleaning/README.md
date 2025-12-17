# Airbnb Listings — Data Cleaning Pipeline (Python)



## Overview

This project demonstrates a **robust, auditable data cleaning pipeline** for Airbnb listings data, implemented in Python and presented as a Jupyter Notebook.



The emphasis is on **real-world data problems** rather than toy examples:



* malformed UTF-8 text (mojibake)

* inconsistent data types

* percentage values stored as strings

* missing and incomplete records

* transparent, defensible cleaning decisions



The pipeline produces:



* an **audit / workings dataset** (with intermediate and derived columns)

* a **final, analysis-ready dataset** with a clean, minimal schema



---



## Dataset

Source dataset (Kaggle):  

https://www.kaggle.com/datasets/ulrikthygepedersen/airbnb-listings



The raw data reflects typical issues found in scraped or aggregated listings data, including inconsistent encodings, mixed formats, and substantial missingness in host-level fields.



---



## Key Cleaning Steps



### Text Cleaning (Encoding Repair)

The pipeline repairs mojibake caused by common encoding errors (for example `CafÃ© → Café`).



It combines:



* `ftfy`

* encoding round-trips (`cp1252`, `latin-1`)

* Unicode normalisation (NFC)



Quality checks include:



* counts of rows changed

* detection of remaining suspicious strings

* side-by-side before/after examples



---



### Data Type Standardisation

Several columns are normalised to appropriate types:



* dates parsed safely with coercion (`host_since`)

* boolean-like fields mapped to a true boolean dtype

* percentage strings (e.g. `"95%"`) converted to numeric proportions (`0.95`)

* categorical fields explicitly typed



---



### Missing Value Handling

Missing data is handled using transparent, domain-aware rules:



* `bedrooms` imputed using **group-wise medians** by property type

* review score fields filled consistently

* derived indicator fields added (e.g. `has_reviews`)



---



### Feature Engineering

Structured features are derived from semi-structured text:



* amenities parsed into `amenities_count`

* boolean flags derived (e.g. `has_wifi`)

* raw and cleaned amenities retained in the audit output



---



## Quality Assurance (QA)

Quality assurance is built directly into the cleaning pipeline and runs alongside the transformations.



This includes:



* rule-level logging of **how many rows each transformation affects**

* visual checks of missingness before and after cleaning

* side-by-side examples of edited text fields

* detection of duplicate column names and identical-content columns



All QA information is also saved to `cleaning_log.csv`.



---



## Outputs



### Audit / Workings Dataset

**`listings_cleaned_with_workings.csv`**



This file includes raw fields, cleaned versions, and intermediate working columns.  

It is intended for transparency, debugging, and reproducibility.



---



### Final Dataset

**`listings_final.csv`**



This is a lean, analysis-ready dataset containing one authoritative version of each field and relevant engineered features.  

Intermediate working columns are removed.



---



## Skills Demonstrated



* Data cleaning and preprocessing in Python

* Handling real-world text encoding issues (UTF-8 / mojibake)

* Robust type conversion and validation

* Missing-data strategies grounded in domain logic

* Feature engineering for downstream analysis

* Built-in QA and auditability for data pipelines

* Clear separation of working vs final outputs

* Reproducible analysis using Jupyter Notebooks



---



## Notes

The notebook is designed to run top-to-bottom in a fresh kernel.



Cleaning decisions are intentionally explicit rather than hidden, and the two-output approach mirrors professional data curation workflows.



