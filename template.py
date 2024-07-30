import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

ev_data = pd.read_excel("/Users/dheerajkushakula/Downloads/Electric_Vehicle_Population_Data.xlsx")

print(ev_data.head())
print(ev_data.info())

#Data Cleaning 

#Handling missing values
print(ev_data.isnull().sum())  # missing values present

ev_data.dropna(inplace=True)  # drop rows with missing values
print(ev_data.isnull().sum())  # no missing values present

print(ev_data.info())

# EV Adoption Over TIme: 
# Analyze the growth of the EV Population by model year
# By visualizing no.of EV Registered by model year.

sns.set_style("whitegrid")
plt.figure(figsize=(12,6))
ev_adoption_by_year = ev_data['Model Year'].value_counts().sort_index()
sns.barplot(x=ev_adoption_by_year.index, y=ev_adoption_by_year.values, palette="viridis")
plt.title('EV Adoption Over Time')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles Registered')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




#ev_data_cleaned.to_excel("/Users/dheerajkushakula/Downloads/new_file.xlsx")