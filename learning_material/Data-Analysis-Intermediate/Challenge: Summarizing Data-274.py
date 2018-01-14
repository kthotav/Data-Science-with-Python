## 2. Introduction to the Data ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")

recent_grads = pd.read_csv("recent-grads.csv")

all_ages.head(5)

recent_grads.head(5)

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()


all_major_categories_aa = all_ages['Major_category'].unique()
all_major_categories_rg = recent_grads["Major_category"].unique()

for major in all_major_categories_aa:
    
    sum_for_major = all_ages[all_ages['Major_category'] == major]["Total"].sum()
    aa_cat_counts[major] = sum_for_major
    
for major in all_major_categories_rg:
    
    sum_for_major = recent_grads[recent_grads['Major_category'] == major]['Total'].sum()
    rg_cat_counts[major] = sum_for_major
    
aa_cat_counts

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wages_total = recent_grads["Low_wage_jobs"].sum()
total_jobs = recent_grads["Total"].sum()

low_wage_proportion = float(low_wages_total/total_jobs)

print(low_wage_proportion)
print(low_wage_proportion*100)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0


for major in majors:
    
    aa = all_ages[all_ages["Major"] == major]
    
    rg = recent_grads[recent_grads["Major"] == major]
    
    aa_unemployment_rate = aa["Unemployment_rate"].values[0]
    rg_unemployment_rate = rg["Unemployment_rate"].values[0]
    
    
    if rg_unemployment_rate < aa_unemployment_rate:
        rg_lower_count += 1
        
print(rg_lower_count)