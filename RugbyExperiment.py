import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


print (tips.head())

sns.distplot(tips['total_bill'])

plt.show()

sns.pairplot(tips)
plt.show()

print("hello Testing a second time")
