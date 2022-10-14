import pandas as pd
data = pd.read_csv('transaction.csv', sep=';')

data['CostPerTransaction'] = data['CostPerItem']*data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup']=round((data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction'], 2)


new_date = data ['Day'].astype(str) +'-' + data['Month']+'-'+ data['Year'].astype(str)
data['Date'] = new_date

split_col = data['ClientKeywords'].str.split(',',expand=True)
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

data['ClientAge']=data['ClientAge'].str.replace('[' , '')
data['LengthOfContract']=data['LengthOfContract'].str.replace(']' , '')
data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
data = pd.merge(data, seasons, on = 'Month')

data = data.drop(['Day', 'Year', 'Month', 'ClientKeywords'], axis = 1)

data.to_csv('ValueInc_Cleaned.csv', index=False)
