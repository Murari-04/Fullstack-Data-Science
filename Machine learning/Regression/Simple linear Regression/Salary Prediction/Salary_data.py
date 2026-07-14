import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\Lenovo\Downloads\Salary_Data.csv")

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split

x_train , x_test, y_train, y_test = train_test_split(x,y,train_size = 0.8, test_size = 0.2, random_state=0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_train,regressor.predict(x_train), color= 'blue')
plt.title('salary vs exp')
plt.xlabel('years of exp')
plt.ylabel('Salary')
plt.show()

m_coef = regressor.coef_
print(m_coef)

c_inter = regressor.intercept_
print(c_inter)

y_12  =  m_coef * 12 + c_inter

print(y_12)

bias_training = regressor.score(x_train, y_train)
print(bias_training) 

variance_testing = regressor.score(x_test,y_test)
print(variance_testing)

dataset.mean() 
dataset['Salary'].mean()
dataset['YearsExperience'].mean()

dataset.median() 
dataset['Salary'].median()
dataset['YearsExperience'].median()

dataset.var()
dataset['Salary'].var()
dataset['YearsExperience'].var()

dataset.std()
dataset['Salary'].std()
dataset['YearsExperience'].std()

from scipy.stats import variation
variation(dataset.values)
variation(dataset['Salary'])
variation(dataset['YearsExperience'])

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])
dataset['Salary'].corr(dataset['Salary'])

dataset.skew()

dataset.sem()


import scipy.stats as stats
dataset.apply(stats.zscore)

stats.zscore(dataset['Salary']) 
stats.zscore(dataset['YearsExperience']) 


# ANOVA

y_mean=np.mean(y) 
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

y=y[0:6]
SSE=np.sum((y-y_pred)**2)
print(SSE)

mean_total = np.mean(dataset.values)
# here df.to_numpy()will convert pandas Dataframe to Nump
SST=np.sum((dataset.values-mean_total)**2)
print(SST)

r_square = 1 - (SSR / SST)
r_square

print(r_square)
print(bias_training)
print(variance_testing)
