import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
#Load data
fires = pd.read_csv('FTM_fires.csv')
fires.head()

trees = pd.read_csv('FTM_trees.csv')
trees.head()

#Merge trees and fire data so each row is a tree with its associated fire
data = pd.merge(trees, fires, on='YrFireName', how='inner')

#Clean data
data = data.drop(columns=['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18' ,'Unnamed: 19'])
data = data.dropna(subset=['CLS_percent', 'yr0status']) #Remove trees whose status was not assessed directly after fire

#Univariate linear regression
species = np.array(data.Species).reshape((-1, 1))
clspercent = np.array(data.CLS_percent).reshape((-1, 1))
burned = np.array(data.yr0status).reshape((-1, 1))

cls_train, cls_test, burn_train, burn_test = train_test_split(clspercent, burned, test_size=0.2, random_state=42)


model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(cls_train, burn_train)

prob_burned = model.predict_proba(burn_test)
pred_burned = model.predict(burn_test)


#Plot data points and linreg line
fig, ax = plt.subplots(figsize = (9, 5))
plt.plot(cls_train, cls_test, '.', alpha=0.5)

#plt.plot(pred_burned, clspercent, '-')

#R_sq = model.score(burned, clspercent)
#pred_burned = model.predict(burned)
print('Slope of regression line: ', model.coef_[0])
print('R-squared coefficient: ', R_sq
