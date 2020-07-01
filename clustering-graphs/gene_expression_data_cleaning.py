import pandas as pd

#Read in gene interaction data
raw_data = pd.read_csv('yeast_gene_interactions.csv',sep='\t')

#Remove 90, 100 minute time point as outliers
raw_data = raw_data.drop(['t:90', 't:100'], axis=1)

#Remove ORFs with low average 
raw_data['row_mean'] = raw_data.loc[: , "t:0":"t:160"].mean(axis=1)
cutoff = raw_data.row_mean.mean() - raw_data.row_mean.std()*2
cleaned_data = raw_data.loc[raw_data.row_mean > cutoff]

#remove ORFs with low variability
cleaned_data['row_std'] = cleaned_data.loc[: , "t:0":"t:160"].std(axis=1)
cutoff = cleaned_data.row_std.mean() - cleaned_data.row_std.std()*2
cleaned_data = cleaned_data.loc[cleaned_data.row_std > cutoff]

#Normalize gene vectors 
normalized_data = cleaned_data
for i in range(len(cleaned_data)):
    gene_vector = cleaned_data.iloc[i]['t:0':'t:160']
    new_vector = (gene_vector - gene_vector.mean() ) / gene_vector.std()
    normalized_data.iloc[i] = new_vector
normalized_data['NAME'] = cleaned_data.NAME
normalized_data['YORF'] = cleaned_data.YORF
normalized_data['GWEIGHT'] = cleaned_data.GWEIGHT

normalized_data.to_csv('cleaned_data.csv')