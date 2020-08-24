import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Load data
data = pd.read_csv('forestfires.csv')
data.head()

#Univariate linear regression
area = np.array(data.area).reshape((-1, 1))
temp = np.array(data.temp).reshape((-1, 1))

model = LinearRegression()
model.fit(temp, area)
R_sq = model.score(temp, area)
pred_temp = model.predict(temp)

print('Slope of regression line: ', model.coef_[0])
print('R-squared coefficient: ', R_sq)

fig, ax = plt.subplots(figsize = (9, 5))
plt.plot(data.temp, data.area, '.', alpha=0.5)
plt.plot(pred_temp, area, '-')


