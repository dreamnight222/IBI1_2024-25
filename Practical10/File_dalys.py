# import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# set working directory
os.chdir(r"C:\users\lenovo\IBI1_2024-25\Practical10")

# import data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Displays the first 10 rows of the third column (year)
print("data of first ten lines")
years_first_10 = dalys_data.iloc[0:10, 2]
print(years_first_10)
# The 10th recorded year for Afghanistan is 1999

# Filtering the data for the year 1990 using Boolean indexing
dalys_1990 = dalys_data.loc[dalys_data['Year'] == 1990, ['Entity', 'DALYs']]
print("\nDALYs data for 1990")
print(dalys_1990.head())

# Calculate the average DALYs for the UK and France
uk_data = dalys_data.loc[dalys_data['Entity'] == "United Kingdom", ["Year","DALYs"]]
france_data = dalys_data.loc[dalys_data['Entity'] == "France", ["Year","DALYs"]]
uk_mean = uk_data['DALYs'].mean()
france_mean = france_data['DALYs'].mean()
print("\nAverage DALYs")
print(uk_mean)
print(france_mean)
#uk_mean is higher than france_mean

# Graph the United Kingdom DALYs over time
plt.figure(figsize=(10, 6))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-', label='United Kingdom')
plt.xlabel('year')
plt.ylabel('DALYs')
plt.title('UK DALYs changes over time')
plt.xticks(uk_data['Year'], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('uk_dalys.png')
plt.show()

