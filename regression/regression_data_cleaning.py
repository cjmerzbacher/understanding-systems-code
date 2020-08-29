import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits import mplot3d

#Load data
data = pd.read_csv('vegstr.csv')

#GOAL: predict tree height based on canopy diameter, etc.

#Univariate linear regression
height = np.array(data.stemheight).reshape((-1, 1))
canopydiam = np.array(data.maxcanopydiam).reshape((-1, 1))

model = LinearRegression()
model.fit(canopydiam, height)
R_sq = model.score(canopydiam, height)
pred_height = model.predict(canopydiam)

print('Slope of regression line: ', model.coef_[0])
print('R-squared coefficient: ', R_sq)

fig, ax = plt.subplots(figsize = (9, 5))
plt.plot(data.maxcanopydiam, data.stemheight, 'k.', alpha=0.5, label='Data points')
plt.plot(canopydiam, pred_height, '-', label='Regression line')
plt.legend()
plt.grid()
ax.set_xlabel('Canopy diameter, m')
ax.set_ylabel('Trunk height, m')

#Multivariate regression
data = data.dropna(subset=['dbh']).reset_index(drop=True)
X = data[['maxcanopydiam', 'dbh']]
height = data['stemheight']
model = LinearRegression()
model.fit(X, height)
R_sq = model.score(X, height)
pred_height = model.predict(X)

print('Slope of regression line: ', model.coef_[0])
print('R-squared coefficient: ', R_sq)


fig = plt.figure(figsize = (9,6))
ax = plt.axes(projection='3d')
ax.scatter3D(data.dbh, data.maxcanopydiam, data.stemheight, color='black')
ax.plot_trisurf(X.dbh, X.maxcanopydiam, pred_height, alpha=0.5)
ax.set_xlabel('Trunk diameter, cm')
ax.set_ylabel('Canopy diameter, m')
ax.set_zlabel('Trunk height, m')
plt.legend()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
ax1.plot(data.maxcanopydiam, data.stemheight, 'k.', alpha=0.5, label='Data points')
ax1.plot(X.maxcanopydiam, pred_height, '.', label='Predicted Values')
ax1.legend()
ax1.grid()
ax1.set_xlabel('Canopy diameter, m')
ax1.set_ylabel('Trunk height, m')

ax2.plot(data.dbh, data.stemheight, 'k.', alpha=0.5, label='Data points')
ax2.plot(X.dbh, pred_height, '.', label='Predicted Values')
ax2.legend()
ax2.grid()
ax2.set_xlabel('Trunk diameter, cm')
ax2.set_ylabel('Trunk height, m')