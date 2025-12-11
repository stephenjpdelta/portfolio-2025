📘 Multiple Correspondence Analysis of Restaurant Consumer Profiles

Portfolio Project — 2025

⭐ Executive Summary

This project applies Multiple Correspondence Analysis (MCA) to a public dataset of restaurant consumer profiles.
After cleaning the data, engineering BMI and age-group variables, and converting all categorical fields into 65 binary indicators, MCA is used to uncover latent behavioural dimensions within the dataset.

The first two MCA dimensions explain ~49% of the variation and reveal broad patterns relating to lifestyle expressiveness and family/social routines. A third dimension explains an additional ~18% and is included for exploratory analysis in the notebook, although the small dataset limits the interpretability of higher-order components.

K-Means clustering applied to the MCA coordinates identifies a large baseline consumer segment, a more expressive lifestyle-oriented group, and a small outlier segment driven by rare category combinations.

This project demonstrates a complete categorical-analysis workflow, including preprocessing, dimensionality reduction, clustering, and visualisation — while also highlighting the limitations inherent in small, weakly structured datasets.

🔏 Data Source & Licensing

This project uses the Restaurant & Consumer Ratings dataset.

Metadata:

License: CC0 – Public Domain
Free to use, modify, and redistribute without restrictions

Usability score: 7.35

Expected update frequency: Not specified

Tags: Business, Arts & Entertainment, Restaurants

The dataset is in the public domain and may be reused freely.

📂 Dataset Overview

138 rows (raw) → 113 rows after cleaning

19 raw variables → 14 categorical features retained

Variables include:

smoker

drink_level

dress_preference

ambience

marital_status

hijos (children)

interest

personality

religion

activity

budget

engineered BMI category

engineered age decade

🧹 Preprocessing Summary

Key steps:

✔ Text cleaning

Lowercased

Trimmed whitespace

Normalised inconsistent values

✔ Feature engineering

BMI = weight / height²

BMI categories (underweight → class III obesity)

Age grouped into decades (1930s → 2020s)

Removed unrealistic heights (<1.6m)

Removed records with missing values (≈5 rows)

✔ Final cleaned dataset

Saved to:
data/processed/userprofiles_cleaned.csv

🔢 Binary Encoding for MCA

All categorical features were one-hot encoded into 65 binary indicator columns, representing categories such as:

drink_level_social_drinker

ambience_romantic

budget_high

personality_extroverted

age_group_1980s

Saved to:
data/processed/userprofiles_mca_matrix.csv

This matrix forms the input to the MCA.

📊 MCA Results & Interpretation
Explained Variance

Dimension 1: ~28%

Dimension 2: ~21%

Dimension 3: ~18%

Subsequent dimensions: progressively smaller contributions

The first three dimensions explain ~67% of the variation.
The README focuses on Dimensions 1 and 2, while Dimension 3 is explored further in the notebook.

📈 Interpretation of Dimensions

Because the dataset is small and many features are only weakly associated, several categories cluster near the origin, indicating limited discriminatory power. However, interpretable patterns still emerge:

Dimension 1 — Lifestyle Expression & Engagement

Separates respondents with more defined lifestyle patterns (dress preference, ambience choice, activity type, budget level) from those whose profiles are more neutral or weakly structured.

High values: expressive or structured lifestyle preferences

Low values: everyday or non-distinctive patterns

Dimension 2 — Family Orientation & Social Routine

Reflects variation linked to family-related circumstances and social routines.

High values: categories associated with family roles and structured activity

Low values: more independent or work-centred profiles

Interpretation is relative and should be treated cautiously given dataset scale.

🔍 Dimension 3 — Additional Structure (~18%)

Although not used for the primary interpretation, Dimension 3 captures additional variation and is included in the notebook for exploratory purposes.
It provides nuance but is less stable due to low-frequency categories.

🔒 Clustering Results (K=3)

Three consumer segments were identified:

Cluster 1 — Baseline Group (largest)

Centered near the origin

No strong distinguishing preferences

Reflects the dataset’s weak structural separation

Cluster 2 — Higher-Engagement Consumers

More expressive lifestyle patterns

Clearer preferences for activity, ambience, dress style, and budget

Cluster 0 — Outlier Group (very small)

Driven by rare category combinations

Should be interpreted cautiously

🔥 Personality → Indicator Heatmap

A heatmap shows how personality categories relate to binary indicators.
Due to small group sizes, patterns are exploratory only.

Example behaviours:

Hunter-ostentatious: expressive, higher-budget tendencies

Thrifty-protector: frugal, family-oriented tendencies

Conformist / Hard-worker: modest or mixed associations

The heatmap illustrates the method, not definitive behavioural claims.

📁 File Structure
portfolio-2025/
└── data/
    ├── raw/
    │   └── userprofile.csv
    └── processed/
        ├── userprofiles_cleaned.csv
        ├── userprofiles_mca_matrix.csv
        ├── row_coordinates.csv
        ├── column_coordinates.csv
        ├── eigenvalues_explained_inertia.csv
        ├── mca_scree_plot.png
        ├── mca_biplot_dim1_dim2.png
        ├── mca_clusters_dim1_dim2.png
        ├── personality_indicator_heatmap.png
        └── userprofiles_categories.json

🚀 How to Run

From the project root:

python Public.py


Dependencies:

pandas

numpy

matplotlib

scikit-learn

prince

🎯 Conclusion

This project demonstrates a complete end-to-end MCA workflow, including data cleaning, categorical encoding, dimensionality reduction, clustering, and visualisation.
Although the dataset is small and only weakly interdependent, MCA still reveals interpretable axes of variation and provides a foundation for exploratory segmentation analysis.

Additional exploration — including Dimension 3 plots and alternative projections — can be found in the accompanying Jupyter notebook.