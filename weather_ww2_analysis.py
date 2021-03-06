import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('WeatherWWII.csv')
print(dataset.describe())

dataset.plot(x='MinTemp', y='MaxTemp', style='o')
plt.title('MinTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()

# dataset.plot(x='MinTemp', y='MaxTemp', style='o')
# plt.figure(figsize=(15,10))
# plt.tight_layout()
seabornInstance.distplot(dataset['MaxTemp'])
plt.show()

# print(dataset['MinTemp'].shape)

X = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=0)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

regressor = LinearRegression()
regressor.fit(X_train,y_train) #training the algorithm

print(regressor.coef_) #Retrieve the slope
print(regressor.intercept_) #Retrieve the intercept

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual' : y_test.flatten(), 'Predicted' : y_pred.flatten()})
df1 = df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.show()

plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('X_test vs y_test/y_pred')
plt.xlabel('X_test')
plt.ylabel('y_test/y_pred')
plt.show()

print('Mean Absolute Error :',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Squared Error :',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Squared Error :',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))