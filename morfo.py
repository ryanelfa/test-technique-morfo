import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
from pynsee.download import download_file


url = "https://drive.google.com/uc?id=1R4wcMGxFHUCFsIzID16bYfziGLwO_0gw"
morfo_plant_data = pd.read_csv(url)

# Checking the first values in our file
## print(morfo_plant_data.head())

# We start by counting the number of occurrences of each family
number_families = morfo_plant_data['FAMILY'].value_counts().head(5)

# Display top 5 plant families
plt.figure(figsize=(10, 6))
number_families.plot(kind='bar', color='red')
plt.title('Top 5 Most Represented Plant Families')
plt.xlabel('FAMILY')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
##plt.show()

# We start by listing all the different "CO BENEFITS" and their potential duplicates
# We notice that there are many missing values, so we replace them with empty character strings
morfo_plant_data['CO BENEFITS'].fillna('missing values', inplace=True)
# We then transform the "CO BENEFITS" into different lists, which we concatenate to form a single list.
morfo_plant_data['CO BENEFITS'] = morfo_plant_data['CO BENEFITS'].apply(lambda x: x.split(','))
all_co_benefits = [co_benefit for sublist in morfo_plant_data['CO BENEFITS'] for co_benefit in sublist]
co_benefit_counts = pd.Series(all_co_benefits).value_counts()

# Display of different co-benefits and potential duplicates
##print("Different CO BENEFITS:")
##print(co_benefit_counts.index.tolist())

# Display the 10 most common co-benefits with a bar graph
plt.figure(figsize=(10, 6))
co_benefit_counts.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Most Common CO BENEFITS')
plt.xlabel('CO BENEFIT')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
##lt.show()

# Now let's calculate the average, median and standard deviation of the size, diameter and seeds/kg columns 
# First of all we will create a function which will give us the mean when an interval is provided
# Function to convert intervals into numerical values using the average
def interval_to_mean(interval):
    if isinstance(interval, str):
        parts = interval.split()
        if len(parts) == 3 and parts[1] == '–':
            return (int(parts[0]) + int(parts[2])) / 2 
    return float(interval)

#We delete the first line because it does not contain data but units.
morfo_plant_data_without_row1 = pd.read_csv(url, skiprows=1)

# We now apply this function to the various columns
for col in ['SIZE', 'DIAMETER', 'SEEDS/KG']:
    morfo_plant_data_without_row1[col] = morfo_plant_data_without_row1[col].apply(interval_to_mean)

# Before calculating the various statistical values, we remove any missing values.
# morfo_plant_data.dropna(subset=['SIZE', 'DIAMETER', 'SEEDS/KG'], inplace=True)
morfo_plant_data_cleaned = morfo_plant_data_without_row1.dropna(subset=['SIZE', 'DIAMETER', 'SEEDS/KG'])
# Finally, we calculate the various statistical values we're interested in
# i.e. the mean, median and standard deviation for each column
average = morfo_plant_data_cleaned[['SIZE', 'DIAMETER', 'SEEDS/KG']].mean()
median = morfo_plant_data_cleaned[['SIZE', 'DIAMETER', 'SEEDS/KG']].median()
std = morfo_plant_data_cleaned[['SIZE', 'DIAMETER', 'SEEDS/KG']].std()

# Various statistical values are displayed
##print("Average:")
##print(average)
##print("\nMedian:")
##print(median)
##print("\nStandard Deviation:")
##print(std)

# I'm getting an error message telling me that the SIZE key is not recognized, even though I can see it in the data file.
# but due to time constraints I can't correct this problem
