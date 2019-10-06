
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
      <td>Scotland</td>
      <td>27</td>
      <td>22</td>
      <td>Ireland</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>1</th>
      <td>England</td>
      <td>19</td>
      <td>16</td>
      <td>France</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Italy</td>
      <td>7</td>
      <td>33</td>
      <td>Wales</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>10</td>
      <td>63</td>
      <td>Ireland</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wales</td>
      <td>16</td>
      <td>21</td>
      <td>England</td>
      <td>2017</td>
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

## Countplot for scores


```python
score_data_countplot = plt.figure(figsize=(24,12))
ax = sns.distplot(All_Scores, bins=np.arange(70)-0.5, kde=False, color = 'g')
ax.set(xticks=range(0,70))
ax.set(yticks=range(0,20))
ax.grid()
```


![png](README_files/README_8_0.png)



```python
most_freq = All_Scores.value_counts()
for score, count in most_freq.head(10).iteritems():
    print("{} has occurred {} times".format(score, count))
```

    16 has occurred 17 times
    13 has occurred 16 times
    9 has occurred 15 times
    10 has occurred 14 times
    23 has occurred 13 times
    18 has occurred 12 times
    15 has occurred 11 times
    19 has occurred 10 times
    21 has occurred 10 times
    20 has occurred 9 times
    

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
mh = match_history("Wales", "England")
mh
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
      <th>4</th>
      <td>Wales</td>
      <td>16</td>
      <td>21</td>
      <td>England</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Wales</td>
      <td>21</td>
      <td>25</td>
      <td>England</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Wales</td>
      <td>16</td>
      <td>21</td>
      <td>England</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Wales</td>
      <td>18</td>
      <td>29</td>
      <td>England</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Wales</td>
      <td>30</td>
      <td>3</td>
      <td>England</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Wales</td>
      <td>19</td>
      <td>12</td>
      <td>England</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Wales</td>
      <td>28</td>
      <td>25</td>
      <td>England</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Mean scores are {} {}".format(mh['Score1'].mean(), mh['Score2'].mean()))
```

    Mean scores are 21.142857142857142 19.428571428571427
    

#### Here we will create a regression plot of the scores from a pair of teams' match history


```python
fig, ax = plt.subplots(figsize=(36,24))
p = sns.regplot(x='Year', y='Score1', data=mh, ax=ax, label=mh['Team1'])
p2 = sns.regplot(x='Year', y='Score2', data=mh, ax=ax, label=mh['Team2'], color='r')
plt.xlim(2011, 2018)
ax.grid()
ax.legend(loc="best")
```




    <matplotlib.legend.Legend at 0x1cfcb9df7f0>




![png](README_files/README_17_1.png)

