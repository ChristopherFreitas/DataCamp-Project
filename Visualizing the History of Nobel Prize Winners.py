# Project Instructions

# Analyze Nobel Prize winner data and identify patterns by answering the following questions:

# What is the most commonly awarded gender and birth country?

# Store your answers as string variables top_gender and top_country.
# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?

# Store this as an integer called max_decade_usa.
# Which decade and Nobel Prize category combination had the highest proportion of female laureates?

# Store this as a dictionary called max_female_dict where the decade is the key and the category is the value. There should only be one key:value pair.
# Who was the first woman to receive a Nobel Prize, and in what category?

# Save your string answers as first_woman_name and first_woman_category.
# Which individuals or organizations have won more than one Nobel Prize throughout the years?

# Store the full names in a list named repeat_list.

--------------------------------------------------------------------------------------------------

# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Read in the Nobel Prize data
nobel = pd.read_csv('data/nobel.csv')

# Store and display the most commonly awarded gender and birth country in requested variables
top_gender = nobel['sex'].value_counts().idxmax()
top_country = nobel['birth_country'].value_counts().idxmax()

print("\n The gender with the most Nobel laureates is :", top_gender)
print(" The most common birth country of Nobel laureates is :", top_country)

# Calculate the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (nobel['year'] // 10) * 10
usa_winratio = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

# Identify the decade with the highest proportion of US-born winners
max_decade_usa = usa_winratio[usa_winratio['usa_born_winner'] == usa_winratio['usa_born_winner'].max()]['decade'].values[0]

# Plotting USA born winners
ax1 = sns.relplot(x='decade', y='usa_born_winner', data=usa_winratio, kind="line")

# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex'] == 'Female'
fem_winratio = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()

# Find the decade and category with the highest proportion of female laureates
max_fem_winratio = fem_winratio[fem_winratio['female_winner'] == fem_winratio['female_winner'].max()][['decade', 'category']]

# Create a dictionary with the decade and category pair
max_female_dict = {max_fem_winratio['decade'].values[0]: max_fem_winratio['category'].values[0]}

# Plotting female winners with % winners on the y-axis
ax2 = sns.relplot(x='decade', y='female_winner', hue='category', data=fem_winratio, kind="line")

# Finding the first woman to win a Nobel Prize
first_woman = nobel[nobel['female_winner']]
first_woman_year = first_woman[first_woman['year'] == first_woman['year'].min()]
first_woman_name = first_woman_year['full_name'].values[0]
first_woman_category = first_woman_year['category'].values[0]
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")

# Selecting the laureates that have received 2 or more prizes
repeat_list = nobel['full_name'].value_counts()[nobel['full_name'].value_counts() > 1].index.tolist()

print("\n The repeat winners are :", repeat_list)
