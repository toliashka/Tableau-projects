import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#trANSFORM TO DATAFRAME
loandata = pd.DataFrame(data)

#finding link values for the purpose column
loandata['purpose'].unique()

#describing the data
loandata.describe()

#describe the data for specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income
  

#applying for loops for loan data

length=len(loandata)
cat=[]
for x in range(0,length):
    fico = loandata['fico'][x]
    try:
        
        if fico>=300 and fico<400:
            ficocat='Very Poor'
        elif fico>=400 and fico<600:
                ficocat = 'Poor'
        elif fico >=601 and fico<660:
                ficocat='Fair'
        elif fico >=660 and fico<700:
                ficocat='Good'
        elif fico>=700:
                ficocat='Excellent'
        else:
                ficocat='Unknown'
    except:
        cat = 'Unknown'
    cat.append(ficocat)

cat = pd.Series(cat)
loandata['fico.category']=cat

#df.loc as conditional statements
# df.loc[df[column_name] condition, new_column_name]='value if the condition is met'
#for interest rate, a nwe column is wanted if the rate>0.12 then high else low
loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'high' 
loandata.loc[loandata['int.rate'] <=0.12, 'int.rate.type'] = 'low' 

#number of loans by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='red', width= 0.5)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='blue', width = 0.3)
plt.show()

#scatter plots
ypoint=loandata['annual income']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)

























