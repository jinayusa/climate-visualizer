import pandas as pd

# Load CO2 emissions (per capita, metric tons)
co2 = pd.read_csv('data/co2_emissions.csv')  # Columns: Country Name, Country Code, 1960–2020
co2 = co2.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='CO2')
co2['Year'] = co2['Year'].astype(int)

# Load Global temperature anomalies (annual mean)
temp = pd.read_csv('data/global_temperature.csv')  # Columns: Year, TempAnomaly
temp = temp[['Year', 'TempAnomaly']]

# Average CO2 globally per year
global_avg_co2 = co2.groupby('Year')['CO2'].mean().reset_index()
merged = pd.merge(global_avg_co2, temp, on='Year')

# Save merged file
merged.to_csv('data/merged_global_climate.csv', index=False)
print("✅ Cleaned and merged successfully!")
