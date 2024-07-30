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



# Top 3 counties based on EV Registrations 

# Geographical distribution at county level
ev_county_distribution = ev_data['County'].value_counts()
top_counties = ev_county_distribution.head(3).index

# filtering the dataset for these top counties
top_counties_data = ev_data[ev_data['County'].isin(top_counties)]

# analyzing the distribution of EVs within the cities of these top counties
ev_city_distribution_top_counties = top_counties_data.groupby(['County', 'City']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')

# visualize the top 10 cities across these counties
top_cities = ev_city_distribution_top_counties.head(10)

plt.figure(figsize=(12, 8))
sns.barplot(x='Number of Vehicles', y='City', hue='County', data=top_cities, palette="magma")
plt.title('Top Cities in Top Counties by EV Registrations')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('City')
plt.legend(title='County')
plt.tight_layout()
plt.show()


# types of electric vehicles 

# Analyze the types of electric vehicles registered in the dataset
ev_type_distribution = ev_data['Electric Vehicle Type'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=ev_type_distribution.values, y=ev_type_distribution.index, palette="rocket")
plt.title('Distribution of Electric Vehicle Types')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('Electric Vehicle Type')
plt.tight_layout()
plt.show()

#ev_data_cleaned.to_excel("/Users/dheerajkushakula/Downloads/new_file.xlsx")