# Rugby Data Experiment


```python
# To make markdown from this file
# jupyter nbconvert --to markdown RugbyExperiment.ipynb --output README.md
```


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
plt.rcParams["patch.force_edgecolor"] = True

pd.options.mode.chained_assignment = None  # default='warn'
```


```python
rugby = pd.read_csv("RugbyData.csv")
rugby.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team1</th>
      <th>Score1</th>
      <th>Score2</th>
      <th>Team2</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ireland</td>
      <td>24</td>
      <td>28</td>
      <td>New Zealand</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>1</th>
      <td>England</td>
      <td>30</td>
      <td>24</td>
      <td>Fiji</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>2</th>
      <td>France</td>
      <td>28</td>
      <td>29</td>
      <td>South Africa</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Wales</td>
      <td>17</td>
      <td>29</td>
      <td>Argentina</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>4</th>
      <td>France</td>
      <td>27</td>
      <td>13</td>
      <td>New Zealand</td>
      <td>2023</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Number of ways to reach score n.
n = 40

# table[i] will store count of solutions for value i.
table = [0 for i in range(n+1)]

# Base case (If given value is 0)
table[0] = 1

# One by one consider given 3 moves and update the 
# table[] values after the index greater than or equal 
# to the value of the picked move.
for i in range(3, n+1):
    table[i] += table[i-3]
for i in range(5, n+1):
    table[i] += table[i-5]
for i in range(7, n+1):
    table[i] += table[i-7]


d={i:x for i,x in enumerate(table)}
score_possibilities = plt.figure(figsize=(16,8))
plt.bar(range(len(d)), list(d.values()), align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.show()
```


    
![png](README_files/README_4_0.png)
    


## All_Scores is a series made by appending Score1 and Score2 columns


```python
All_Scores = rugby['Score1'].append(rugby['Score2'])
```

    C:\Users\benmc\AppData\Local\Temp\ipykernel_32212\3103183966.py:1: FutureWarning: The series.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
      All_Scores = rugby['Score1'].append(rugby['Score2'])
    

## Countplot for scores


```python
# Convert the data to a DataFrame
rugby = pd.read_csv("RugbyData.csv")

df = rugby.melt(id_vars=['Year'], value_vars=['Score1', 'Score2'], value_name='Score')
df.drop(columns=['variable'], inplace=True)
df = df.sort_values(by='Year')

# Creating a custom color palette
year_palette = sns.color_palette("YlGnBu", n_colors=df["Year"].nunique())

# Creating a distplot using seaborn
plt.figure(figsize=(24, 12))
hist = sns.histplot(data=df, bins=np.arange(70)-0.5, x="Score", hue="Year", multiple="stack", palette=year_palette)

# Getting the color information from the distplot legend
legend_colors = [patch.get_facecolor() for patch in hist.legend_.legendHandles]

# Creating a custom legend
legend_labels = df["Year"].unique()
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                  markerfacecolor=color, markersize=10)
                  for label, color in zip(legend_labels, legend_colors)]

plt.legend(handles=legend_handles, title="Year")
# Adding axis ticks for each score value
plt.xticks(df["Score"].unique())
plt.title("Distribution of Scores by Year")
plt.xlabel("Score")
plt.xlim(0,50)
plt.ylabel("Count")
plt.show()


```


    
![png](README_files/README_8_0.png)
    



```python

score_data_countplot = plt.figure(figsize=(24,12))
ax = sns.distplot(All_Scores, bins=np.arange(70)-0.5, kde=False, color = 'g')
ax.set(xticks=range(0,70))
ax.set(yticks=range(0,20))
ax.grid()
```

    C:\Users\benmc\AppData\Local\Temp\ipykernel_32212\2603930824.py:2: UserWarning: 
    
    `distplot` is a deprecated function and will be removed in seaborn v0.14.0.
    
    Please adapt your code to use either `displot` (a figure-level function with
    similar flexibility) or `histplot` (an axes-level function for histograms).
    
    For a guide to updating your code to use the new functions, please see
    https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
    
      ax = sns.distplot(All_Scores, bins=np.arange(70)-0.5, kde=False, color = 'g')
    


    
![png](README_files/README_9_1.png)
    



```python
most_freq = All_Scores.value_counts()
for score, count in most_freq.head(15).iteritems():
    print("{} has occurred {} times".format(score, count))
```

    13 has occurred 29 times
    10 has occurred 27 times
    17 has occurred 25 times
    16 has occurred 21 times
    23 has occurred 21 times
    18 has occurred 20 times
    15 has occurred 19 times
    9 has occurred 19 times
    19 has occurred 19 times
    24 has occurred 18 times
    21 has occurred 17 times
    22 has occurred 17 times
    27 has occurred 17 times
    3 has occurred 15 times
    0 has occurred 15 times
    

    C:\Users\benmc\AppData\Local\Temp\ipykernel_32212\449208587.py:2: FutureWarning: iteritems is deprecated and will be removed in a future version. Use .items instead.
      for score, count in most_freq.head(15).iteritems():
    

#### Common scores seen in the ranges 9-10, 12-13, 15-23, 26-30

## Team Specifics

## Function to return match history of 2 teams


```python
def match_history(country1, country2):
    games1 = rugby[(rugby['Team1']==country1) & (rugby['Team2']==country2)]
    games2 = rugby[(rugby['Team2']==country1) & (rugby['Team1']==country2)]
    c = games2.columns
    games2[[c[0], c[3]]] = games2[[c[3], c[0]]]
    games2[[c[1], c[2]]] = games2[[c[2], c[1]]]
    games = games1.append(games2)
    games.sort_index(inplace=True)
    return games
```


```python
mh = match_history("France", "New Zealand")
mh
```

    C:\Users\benmc\AppData\Local\Temp\ipykernel_32212\246494248.py:7: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
      games = games1.append(games2)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team1</th>
      <th>Score1</th>
      <th>Score2</th>
      <th>Team2</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>France</td>
      <td>27</td>
      <td>13</td>
      <td>New Zealand</td>
      <td>2023</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Mean scores are {} {}".format(mh['Score1'].mean(), mh['Score2'].mean()))
```

    Mean scores are 27.0 13.0
    

#### Here we will create a regression plot of the scores from a pair of teams' match history


```python
fig, ax = plt.subplots(figsize=(36,24))
p = sns.regplot(x='Year', y='Score1', data=mh, ax=ax, label=mh['Team1'])
p2 = sns.regplot(x='Year', y='Score2', data=mh, ax=ax, label=mh['Team2'], color='r')
plt.xlim(2011, 2018)
ax.grid()
ax.legend(loc="best")
```




    <matplotlib.legend.Legend at 0x206789e7190>




    
![png](README_files/README_18_1.png)
    



```python

```


```python

```


```python

```
