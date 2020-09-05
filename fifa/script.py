import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

print(df.head())
print(df_goals.head())

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

print(df.head())

sns.set_style('whitegrid')
sns.set_context('poster', font_scale=0.7)

f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data=df, x='Year', y="Total Goals")
ax.set_title('Total Number of Goals in FIFA cup')
plt.show()

sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')
plt.title('Goals Distribution by year')

plt.show()