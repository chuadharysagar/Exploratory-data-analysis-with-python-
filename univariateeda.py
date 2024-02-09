# -*- coding: utf-8 -*-
"""UnivariateEDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11BWHV2vgePgZV37NG6XREewCINTyEOCQ
"""

import pandas as pd
import seaborn as sns

df=pd.read_csv("train.csv")

df.sample(5)

"""# 1.Categorical Data

## Bar Chart
"""

# sns.countplot(df['Survived'])
df['Survived'].value_counts().plot(kind='bar')

df['Pclass'].value_counts().plot(kind='bar')

df['Sex'].value_counts().plot(kind='bar')

df['Embarked'].value_counts().plot(kind='bar')

"""## PIe chart"""

# to see the data in terms of percentage
df['Survived'].value_counts().plot(kind='pie',autopct='%.2f')

"""# 2.Numerical Data

# a.Histogram
"""

import matplotlib.pyplot as plt
plt.hist(df['Age'],bins=8)

"""# b.Distplot"""

sns.distplot(df['Age']) #kde probability density function (pdf)

"""# c.boxplot"""

sns.boxplot(df['Fare'])

df['Age'].skew() #to check the skewness of the data

