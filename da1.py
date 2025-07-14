import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('annual.csv')

# ===========================
# 1. Basic Data Inspection
# ===========================

print("🔹 First 5 rows of the dataset:")
print(df.head())

print("\n🔹 Dataset Information:")
print(df.info())

print("\n🔹 Statistical Summary:")
print(df.describe())

print("\n🔹 Missing Values:")
print(df.isnull().sum())

# ===========================
# 2. Handle Missing Values
# ===========================

# Fill numeric columns with median
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Fill non-numeric (object) columns with mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ===========================
# 3. Basic Plotting with Matplotlib
# ===========================

# 3.1 Line plot of numeric columns over time (if 'year' exists)
if 'year' in df.columns:
    plt.figure(figsize=(10, 5))
    for col in num_cols:
        if col != 'year':
            plt.plot(df['year'], df[col], marker='o', label=col)
    plt.title('Numeric Column Trends Over Years')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 3.2 Histogram of all numeric columns
for col in num_cols:
    plt.figure(figsize=(6, 4))
    plt.hist(df[col], bins=30, color='lightblue', edgecolor='black')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# 3.3 Boxplot of all numeric columns
for col in num_cols:
    plt.figure(figsize=(4, 5))
    plt.boxplot(df[col])
    plt.title(f'Boxplot of {col}')
    plt.ylabel(col)
    plt.tight_layout()
    plt.show()
