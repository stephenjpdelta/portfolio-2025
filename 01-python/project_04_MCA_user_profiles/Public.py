# =============================================================================
# Main.py – MCA on Restaurant Consumer User Profiles
# Full pipeline: preprocess → dummy-code → MCA → plots → clustering
# Outputs are organised into:
#   data/processed/          (cleaned data)
#   data/processed/mca/      (all MCA outputs)
# =============================================================================

from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import prince  # MCA implementation


# =============================================================================
# SECTION 1: USER SETTINGS
# =============================================================================

# Raw input CSV (relative to repo root)
RAW_CSV_PATH = Path("data/raw/restaurant-data-and-consumer-ratings/userprofile.csv")

# Cleaned data directory (relative)
PROCESSED_DIR = Path("data/processed")

# MCA outputs directory (subfolder of processed)
MCA_DIR = PROCESSED_DIR / "mca"

# Column to use as grouping variable for the heatmap
ROLE_COLUMN = "personality"        # or "interest", "activity", etc.

# Number of MCA dimensions
N_COMPONENTS = 5

# Number of clusters for k-means
N_CLUSTERS = 3

# Ensure folders exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
MCA_DIR.mkdir(parents=True, exist_ok=True)


# =============================================================================
# SECTION 2: LOAD RAW DATA
# =============================================================================

print("Loading raw data from:", RAW_CSV_PATH)
df = pd.read_csv(RAW_CSV_PATH)
print("Original shape:", df.shape)


# =============================================================================
# SECTION 3: PREPROCESSING
# =============================================================================

# 3.1 Remove irrelevant columns if present
cols_to_drop = [c for c in ["latitude", "longitude", "the_geom_meter", "color"] if c in df.columns]
df = df.drop(columns=cols_to_drop)
print("After dropping lat/long/geom/color:", df.shape)

# 3.2 Clean text columns: strip whitespace & lowercase
obj_cols = df.select_dtypes(include="object").columns
for col in obj_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

# 3.3 Ensure birth_year is numeric
if "birth_year" in df.columns:
    df["birth_year"] = pd.to_numeric(df["birth_year"], errors="coerce")

# 3.4 Compute BMI = weight (kg) / height^2 (m^2)
df["bmi"] = df["weight"] / (df["height"] ** 2)

# 3.5 Remove clearly unrealistic adult heights (< 1.6m)
df = df[df["height"] >= 1.6]
print("After filtering height >= 1.6m:", df.shape)

# 3.6 Create BMI clinical categories
df["bmi_group"] = pd.cut(
    df["bmi"],
    bins=[0, 18.5, 25, 30, 35, 40, np.inf],
    labels=["underweight", "normal", "overweight", "obesity_i", "obesity_ii", "obesity_iii"],
    include_lowest=True,
)

# 3.7 Create 10-year age bins from 1930 onwards
if "birth_year" in df.columns:
    age_bins = np.arange(1930, 2031, 10)  # [1930, 1940, ..., 2030]
    age_labels = [f"{y}s" for y in range(1930, 2030, 10)]

    df["age_group"] = pd.cut(
        df["birth_year"],
        bins=age_bins,
        labels=age_labels,
        right=False
    )
else:
    df["age_group"] = np.nan

# 3.8 Drop numeric fields not needed for MCA
for col in ["birth_year", "height", "weight", "bmi"]:
    df = df.drop(columns=[col], errors="ignore")

# 3.9 Drop userID if present (identifier, not useful for MCA)
df = df.drop(columns=["userID"], errors="ignore")

# 3.10 Drop rows with ANY missing values
df = df.dropna()
print("After dropna:", df.shape)

print("\nCleaned dataframe (first 5 rows):")
print(df.head())

# Save the cleaned dataset
cleaned_path = PROCESSED_DIR / "userprofiles_cleaned.csv"
df.to_csv(cleaned_path, index=False)
print(f"\nSaved cleaned dataset to: {cleaned_path}")


# =============================================================================
# SECTION 4: BUILD BINARY MATRIX (DUMMY-CODED)
# =============================================================================

categorical_cols = df.columns
X = pd.get_dummies(df[categorical_cols], drop_first=False)

# Ensure numeric 0/1
X = X.astype(int)

print("\nMCA matrix shape:", X.shape)
print("MCA preview:")
print(X.head())

# Save binary matrix
mca_matrix_path = PROCESSED_DIR / "userprofiles_mca_matrix.csv"
X.to_csv(mca_matrix_path, index=False)
print(f"Saved MCA matrix to: {mca_matrix_path}")

binary_cols = list(X.columns)
X_binary = X.copy()


# =============================================================================
# SECTION 5: FIT MCA
# =============================================================================

n_components = min(N_COMPONENTS, len(binary_cols))
print(f"\nRunning MCA with {n_components} dimensions...")

mca = prince.MCA(
    n_components=n_components,
    n_iter=5,
    copy=True,
    check_input=True,
    random_state=42,
).fit(X_binary)

row_coords = mca.row_coordinates(X_binary)
col_coords = mca.column_coordinates(X_binary)
eigenvalues = mca.eigenvalues_

# Handle explained inertia depending on prince version
try:
    explained_attr = mca.explained_inertia_
    explained = explained_attr() if callable(explained_attr) else explained_attr
except AttributeError:
    total = eigenvalues.sum()
    explained = eigenvalues / total if total > 0 else np.zeros_like(eigenvalues)

eigs_df = pd.DataFrame({
    "dimension": np.arange(1, len(eigenvalues) + 1),
    "eigenvalue": eigenvalues,
    "explained_inertia": explained
})


# =============================================================================
# SECTION 6: SAVE MCA OUTPUTS
# =============================================================================

# Align respondent coordinates with cleaned df index
row_coords.index = df.index

row_coords.to_csv(MCA_DIR / "row_coordinates.csv")
col_coords.to_csv(MCA_DIR / "column_coordinates.csv")
eigs_df.to_csv(MCA_DIR / "eigenvalues_explained_inertia.csv", index=False)

# Save categories per variable
categories = {col: sorted(df[col].unique()) for col in df.columns}
with open(MCA_DIR / "userprofiles_categories.json", "w") as f:
    json.dump(categories, f, indent=4)

print(f"\nSaved MCA outputs to: {MCA_DIR}")


# =============================================================================
# SECTION 7: SCREE PLOT
# =============================================================================

plt.figure(figsize=(6, 4))
plt.plot(eigs_df["dimension"], eigs_df["explained_inertia"], marker="o")
plt.title("MCA – Scree Plot")
plt.xlabel("Dimension")
plt.ylabel("Explained Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig(MCA_DIR / "mca_scree_plot.png", dpi=300)
plt.close()


# =============================================================================
# SECTION 8: BIPLOT (DIM 1 vs DIM 2)
# =============================================================================

if n_components >= 2:
    fig, ax = plt.subplots(figsize=(8, 8))

    # Respondents
    ax.scatter(row_coords[0], row_coords[1], s=10, alpha=0.3, label="Respondents")

    # Variables (categories)
    ax.scatter(col_coords[0], col_coords[1], marker="x", s=60, label="Variables")

    for i, label in enumerate(col_coords.index):
        ax.text(col_coords.iloc[i, 0], col_coords.iloc[i, 1], label, fontsize=7)

    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlabel("Dimension 1")
    ax.set_ylabel("Dimension 2")
    ax.set_title("MCA Biplot (Dim 1 vs Dim 2)")
    ax.legend()
    plt.tight_layout()
    plt.savefig(MCA_DIR / "mca_biplot_dim1_dim2.png", dpi=300)
    plt.close()


# =============================================================================
# SECTION 9: CLUSTERING IN MCA SPACE
# =============================================================================

if n_components >= 2:
    X_mca = row_coords.iloc[:, :n_components].values
    kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_mca)

    # Save cluster labels
    df[["cluster"]].to_csv(MCA_DIR / "cluster_assignments.csv")

    # Cluster plot
    fig, ax = plt.subplots(figsize=(8, 8))
    scatter = ax.scatter(row_coords[0], row_coords[1], c=df["cluster"], cmap="tab10", alpha=0.7)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlabel("Dimension 1")
    ax.set_ylabel("Dimension 2")
    ax.set_title("MCA – Clusters")
    plt.colorbar(scatter, label="Cluster")
    plt.tight_layout()
    plt.savefig(MCA_DIR / "mca_clusters_dim1_dim2.png", dpi=300)
    plt.close()


# =============================================================================
# SECTION 10: HEATMAP (GROUP → INDICATOR)
# =============================================================================

if ROLE_COLUMN in df.columns:
    df_role = pd.concat(
        [df[[ROLE_COLUMN]].reset_index(drop=True),
         X_binary.reset_index(drop=True)],
        axis=1
    )
    role_theme = df_role.groupby(ROLE_COLUMN)[binary_cols].mean()

    plt.figure(figsize=(max(8, len(binary_cols)*0.4), max(6, len(role_theme)*0.4)))
    plt.imshow(role_theme.values, aspect="auto")
    plt.colorbar(label="Proportion = 1")
    plt.xticks(np.arange(len(binary_cols)), binary_cols, rotation=90)
    plt.yticks(np.arange(len(role_theme.index)), role_theme.index)
    plt.title(f"{ROLE_COLUMN} → Indicator Heatmap")
    plt.tight_layout()
    plt.savefig(MCA_DIR / f"{ROLE_COLUMN}_indicator_heatmap.png", dpi=300)
    plt.close()
else:
    print(f"\nROLE_COLUMN '{ROLE_COLUMN}' not found; skipping heatmap.")


# =============================================================================
# DONE
# =============================================================================

print("\nAll done!")
print("Cleaned data saved to:", PROCESSED_DIR.resolve())
print("MCA outputs saved to:", MCA_DIR.resolve())
