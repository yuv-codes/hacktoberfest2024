# %% [markdown]
# Olympics Medals and Data Analysis 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# %% [markdown]
# ## Importing Data

# %%
dict=pd.read_csv('dictionary.csv')

# %%
summ=pd.read_csv('summer.csv')

# %%
win=pd.read_csv('winter.csv')

# %%
dict.head()

# %%
summ.head()

# %%
win.head()

# %% [markdown]
# ## Checking Null Values and Data Types

# %%
dict.info()

# %%
summ.info()

# %%
win.info()

# %%
temp=dict[dict['GDP per Capita'].isna()&dict['Population'].isna()]
display(temp)

# %%
temp1 = summ[summ['Country'].isna() ]
display(temp1)

# %% [markdown]
# ## Summary Statistics

# %%
dict.describe()

# %%
win.describe()

# %%
summ.describe()

# %% [markdown]
# ## Distribution of Numerical Values

# %%
sns.histplot(dict['GDP per Capita'],bins=20,kde=True)
plt.xticks([20000, 40000, 60000, 80000, 100000])
plt.title("Distribution of GDP per Capita")
plt.xlabel("GDP per Capita")
plt.ylabel("Frequency")

# %%
sns.boxplot(x= dict['Population'])
plt.title("Distribution of Population")
plt.xlabel("Population")

# %% [markdown]
# ## Distribution of Categorical Values

# %%
summ['Country'].value_counts()

# %%
win['Country'].value_counts()

# %%
summ['Gender'].value_counts()

# %%
win['Gender'].value_counts()

# %%
summ['Sport'].value_counts()

# %%
win['Sport'].value_counts()

# %%
summ['Athlete'].value_counts()

# %%
win['Athlete'].value_counts()

# %% [markdown]
# ## Correlation Matrix

# %%
numeric_df = dict.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True)

# %% [markdown]
# ## Analysing the Relationships

# %%
plt.scatter(dict['Population'],dict['GDP per Capita'], alpha=0.5)
plt.title('GDP per Capita vs. Population')
plt.xlabel('Population')
plt.ylabel('GDP per Capita')
plt.grid(True)
plt.xlim(left=1e7)
plt.show()


# %% [markdown]
# ## Merging Summer and Winter df

# %%
final_df = pd.concat([summ, win], axis=0, keys=["Summer", "Winter"], names=["Season", "Edition"]).reset_index(level="Season")

# %%
display(final_df)

# %%
final_df = final_df.reset_index()

# %%
final_df = final_df.drop(columns=["Edition"])
display(final_df)

# %% [markdown]
# ## Merging Countries with Final Dataframe

# %%
olympics = final_df.merge(dict.iloc[:, :2], how= "left", right_on = "Code", left_on = "Country")

# %%
display(olympics)

# %%
olympics= olympics.drop(columns= "Code")


# %%
display(olympics)

# %%
olympics = olympics.rename(columns= {"Country_x": "Code", "Country_y": "Country"})
display(olympics)

# %% [markdown]
# ## Data Cleaning

# %%
olympics.isnull().sum()

# %%
missing_index = olympics.loc[olympics["Country"].isnull(), "Code"]
missing_index

# %%
olympics.loc[olympics["Country"].isnull(), "Code"].value_counts()

# %%
missing_countries = olympics.loc[olympics["Country"].isnull(), "Code"].dropna().unique()

# %%
display(missing_countries)

# %% [markdown]
# #### Mapping Missing Countries with their Codes

# %%
mapping_data = pd.Series(index = missing_countries, name = "Country", data = ["Mixed team", "Bohemia", "Australasia", "Russian Empire", "Czechoslovakia", "Yugoslavia","Romania", "Soviet Union", "United Team of Germany", "British West Indies","East Germany", "West Germany", "Unified Team", "Independent Olympic Participants","Serbia", "Trinidad and Tobago", "Montenegro", "Singapore"])

# %%
display(mapping_data)

# %%
data = {"Code": mapping_data.index,"Country": mapping_data.values}
df = pd.DataFrame(data)

# %%
df

# %%
merged_olympics = olympics.merge(df, how='left', on='Code')
merged_olympics

# %%
merged_olympics['Country'] = merged_olympics['Country_x'].fillna(merged_olympics['Country_y'])
merged_olympics.drop(columns=["Country_x", "Country_y"], inplace=True)

# %%
merged_olympics.isnull().sum()

# %%
merged_olympics[merged_olympics['Code'].isnull()]

# %%
merged_olympics = merged_olympics.dropna()

# %%
merged_olympics.reset_index(inplace = True)

# %% [markdown]
# ## Data Visualization

# %% [markdown]
# ### Frequency of Categorical Values

# %%
categorical_variables = ['Sport', 'Discipline', 'Country']
for var in categorical_variables:
    category_counts = merged_olympics[var].value_counts()
    plt.figure(figsize=(10, 20)) 
    category_counts.plot(kind='barh', color='skyblue')
    plt.title(f'Frequency of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)  
    plt.show()

# %% [markdown]
# ### Frequency of Top and Bottom 5 Categorical Values

# %%
categorical_variables = ['Sport', 'Discipline', 'Country']
for var in categorical_variables:
    category_counts = merged_olympics[var].value_counts()
    sorted_values = category_counts.sort_values()
    top_5 = sorted_values[-5:]
    bottom_5 = sorted_values[:5]
    plt.figure(figsize=(12, 6))  
    plt.subplot(1, 2,1)  
    top_5.plot(kind='barh', color='skyblue')
    plt.title(f'Top 5 {var}')
    plt.xlabel('Frequency')
    plt.ylabel(var)
    plt.subplot(1, 2,2)  
    bottom_5.plot(kind='barh', color='salmon')
    plt.title(f'Bottom 5 {var}')
    plt.xlabel('Frequency')
    plt.ylabel(var)
    plt.tight_layout()  
    plt.show()

# %% [markdown]
# ### Frequency of Gender and Season

# %%
categorical_values = ['Gender', 'Season']
plt.figure(figsize=(16, 6))
for i, var in enumerate(categorical_values, 1):
    plt.subplot(1, 2, i)  
    merged_olympics[var].value_counts().plot(kind='barh', color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel(var)
    plt.title(f'Frequency of {var}')
plt.tight_layout()  
plt.show()

# %% [markdown]
# ### Number of Events by Year

# %%
events_per_year = merged_olympics.groupby('Year')['Event'].count()
plt.figure(figsize=(10, 6))
events_per_year.plot(kind='line', marker='o', color='skyblue')
plt.title('Number of Events Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.grid(True)  
plt.show()

# %% [markdown]
# ### Medal Count by Year

# %%
medal_count_by_year = merged_olympics.groupby('Year')['Medal'].count().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=medal_count_by_year, x='Year', y='Medal', marker='o', color='skyblue')
plt.title('Total Medal Count by Year')
plt.xlabel('Year')
plt.ylabel('Total Medal Count')
plt.xticks(rotation=45)  
plt.grid(True)  
plt.show()

# %% [markdown]
# ### Distribution of Gender and Gender Wise Count of Medals

# %%
categorical_variables = ['Medal', 'Gender']
plt.figure(figsize=(10, 4))
for i, var in enumerate(categorical_variables, 1):
    plt.subplot(1, 3, i)
    sns.countplot(data=merged_olympics, x=var, hue='Gender', palette='pastel')
    plt.title(f'Stacked Bar Plot of {var} by Gender')
    plt.xlabel(var)
    plt.ylabel('Count')
    plt.xticks(rotation=45)  
    plt.legend(title='Gender')
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Number of Medals by Sports for both Genders

# %%
sport_gender_counts = merged_olympics.groupby(['Sport', 'Gender']).size().unstack(fill_value=0)
sport_gender_counts.plot(kind='bar', stacked=False, color=['skyblue', 'salmon'])
plt.title('Count of Medals by Sport for Each Gender')
plt.xlabel('Sport')
plt.ylabel('Count of Medals')
plt.xticks(rotation=90, ha='right')
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Number of Medals by Discipline for both Genders

# %%
sport_gender_counts = merged_olympics.groupby(['Discipline', 'Gender']).size().unstack(fill_value=0)
plt.figure(figsize=(20, 10))
ax = plt.gca()
sport_gender_counts.plot(kind='bar', stacked=False, color=['skyblue', 'salmon'], ax=ax)
plt.title('Count of Medals by Discipline for Each Gender', fontsize = 20)
plt.xlabel('Discipline', fontsize = 18)
plt.ylabel('Count of Medals', fontsize = 18)
plt.xticks(rotation=90, ha='right', fontsize = 16)
plt.legend(title='Gender', fontsize = 20)
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Top 10 Countries

# %%
top_10_countries = merged_olympics['Country'].value_counts().head(10)
top_10_countries.plot(kind='barh', color = 'skyblue')
plt.xticks(rotation=45)
plt.xlabel('Count of Medals')
plt.ylabel('Countries')
plt.title('Top 10 Countries')
plt.show()

# %%
sns.countplot(data= merged_olympics, x= 'Country', hue='Season', order = top_10_countries.index)
plt.xticks(rotation=45)
plt.xlabel('Count of Medals')
plt.ylabel('Countries')
plt.title('Top 10 Countries')
plt.show()

# %%
sns.countplot(data= merged_olympics, x= 'Country', hue='Medal', order = top_10_countries.index)
plt.xticks(rotation=45)
plt.xlabel('Count of Medals')
plt.ylabel('Countries')
plt.title('Top 10 Countries')
plt.show()

# %% [markdown]
# ### Top 10 Sports

# %%
top_10_countries = merged_olympics['Sport'].value_counts().head(10)
top_10_countries.plot(kind='barh', color = 'skyblue')
plt.xticks(rotation=45)
plt.xlabel('Count of Medals')
plt.ylabel('Sport')
plt.title('Top 10 Sports')
plt.show()

# %%
sns.countplot(data= merged_olympics, x= 'Sport', hue='Season', order = top_10_countries.index)
plt.xticks(rotation=90)
plt.xlabel('Count of Medals')
plt.ylabel('Sports')
plt.title('Top 10 Sports')
plt.show()

# %%
sns.countplot(data= merged_olympics, x= 'Sport', hue='Medal', order = top_10_countries.index)
plt.xticks(rotation=45)
plt.xlabel('Count of Medals')
plt.ylabel('Sports')
plt.title('Top 10 Sports')
plt.show()

# %% [markdown]
# ### Year Wise Number of Medals

# %%
medals_count = olympics.groupby(['Year', 'Medal']).size().unstack(fill_value=0)
medals_count.columns = ['Bronze', 'Gold', 'Silver']
print(medals_count)

# %%
medals_count['Total'] = medals_count['Gold'] + medals_count['Silver'] + medals_count['Bronze']
top_10_years = medals_count.sort_values(by='Total', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_years.index, top_10_years['Gold'], color='gold', label='Gold')
plt.bar(top_10_years.index, top_10_years['Silver'], bottom=top_10_years['Gold'], color='silver', label='Silver')
plt.bar(top_10_years.index, top_10_years['Bronze'], bottom=top_10_years['Gold'] + top_10_years['Silver'], color='peru', label='Bronze')
plt.title('Top 10 Years with Most Medals')
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()



