import pandas as pd 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

k = 15
#Import clustered data and separate labels
raw_data = pd.read_csv('result_data.csv')
data = raw_data.loc[1:, 't:0':'t:160']
label = raw_data.closest[1:]

#Perform LDA
lda = LinearDiscriminantAnalysis(n_components=15)
transformed_data = lda.fit(data, label).transform(data)

plt.figure()
for i in range(k+1):
 plt.scatter(transformed_data[label == i, 0], transformed_data[label == i, 1], alpha=.8,
 label=i)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA')
plt.show()