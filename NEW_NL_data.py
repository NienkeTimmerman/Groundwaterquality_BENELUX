import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('dit is een test')

#read file and rename the columns
df = pd.read_csv('NL_new_data_GW.csv', sep=',')
df.rename(columns = {'observedPropertyDeterminandLabel':'pollutant', 'resultObservedValue':'concentration' , 'resultUom':'unit', 'phenomenonTimeSamplingDate_year':'year'}, inplace = True)
df = (df[['pollutant', 'concentration', 'unit', 'year']])

#selecting pollutants from dataframe
ammonium_pollutant = ['Ammonium']
nitrate_pollutant = ['Nitrate']
selected_data_ammonium = df[df['pollutant'].isin(ammonium_pollutant)]
selected_data_nitrate = df[df['pollutant'].isin(nitrate_pollutant)]

# Calculate overall mean for each pollutant
overall_ammonium_mean = selected_data_ammonium['concentration'].mean()
overall_nitrate_mean = selected_data_nitrate['concentration'].mean()

print("Overall Mean Ammonium concentration:")
print(overall_ammonium_mean)

print("Overall Mean Nitrate concentration:")
print(overall_nitrate_mean)

#create figure
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

#create histogram for ammonium
ammonium_pivot_data = selected_data_ammonium.pivot_table(index='year', columns='pollutant', values='concentration', aggfunc=np.mean)
ammonium_pivot_data.plot(kind='bar', stacked=False, ax=axes[0], color='gold')
axes[0].set_title('Ammonium')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Concentration in mg/L')
sns.despine()

ammonium_target_value = 0.304
axes[0].axhline(y=ammonium_target_value, color='red', linestyle='--', label='Target')

#create histogram for nitrate
nitrate_pivot_data = selected_data_nitrate.pivot_table(index='year', columns='pollutant', values='concentration', aggfunc=np.mean)
nitrate_pivot_data.plot(kind='bar', stacked=False, ax=axes[1], color='blue')
axes[1].set_title('Nitrate')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Concentration in mg/L')

nitrate_target_value = 50.0
axes[1].axhline(y=nitrate_target_value, color='red', linestyle='--', label='Target')

#add legend
axes[0].legend(title='Pollutant', bbox_to_anchor=(1.05, 1), loc='upper left')
axes[1].legend(title='Pollutant', bbox_to_anchor=(1.05, 1), loc='upper left')


plt.suptitle('Groundwater pollution in the Netherlands', fontweight='bold')
plt.tight_layout()
plt.savefig("Groundwater pollution in the Netherlands.png")

