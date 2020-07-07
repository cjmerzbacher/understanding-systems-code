import pandas as pd

#Read in gene interaction data
raw_data = pd.read_csv('PPIdatabase.csv',sep='\t')

#Split gene IDs 
data = pd.DataFrame()
data['id_A'] = raw_data['ID Interactor A'].to_list()
data['id_B'] = raw_data['ID Interactor B'].to_list()
data['id_A'] = [data['id_A'][i].split(':')[-1] for i in range(len(data.id_A))]
data['id_B'] = [data['id_B'][i].split(':')[-1] for i in range(len(data.id_B))]

data['A'] = raw_data['Gene Name Interactor A'].to_list()
data['B'] = raw_data['Gene Name Interactor B'].to_list()

data['weight'] = raw_data['Confidence Value'].to_list()
data.to_csv('cleaned_data.csv')