# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:16:39 2022

@author: psson
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to load json file

json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to load json file

with open('loan_data_json.json') as json_file2:
    data2 = json.load(json_file2)
    


#converting list to dataframe

loandata = pd.DataFrame(data)

#finding unique values for the purpose column

loandata['purpose'].unique()

#describe data

loandata.describe()

#exponential function
annoual_income = np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome'] = annoual_income

#0D array
arr = np.array(4)


#1D array
arr = np.array([1,2,3,4])

#2D array
arr = np.array([[1,2,3], [4,5,6]])

#if elif else
# 300 - 400: Very Poor
# - 401 - 600: Poor
# - 601 - 660: Fair
# - 661 - 780: Good
# - 781 - 850: Excellent

fico = 700
if fico >= 300 and fico <= 400:
    ficocat = 'Very Poor'
elif fico >= 401 and fico <= 600:
    ficocat = 'Poor'
elif fico >= 601 and fico <= 660:
    ficocat = 'Fair'
elif fico >= 661 and fico <= 780:
    ficocat = 'Good'
elif fico >= 781 and fico <= 850:
    ficocat = 'Excellent'
print(ficocat)

#for loop
fruits = ['apple', 'banana', 'cherry', 'grapes']

for x in fruits:
    print(x)
    y=x + ' fruit'
    print(y)

for x in range(0,3):
    y = fruits[x] + ' for sale'
    print(y)

#for loop in the dataset

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and fico <= 400:
        cat = 'Very Poor'
    elif category >= 401 and category <= 600:
        cat = 'Poor'
    elif category >= 601 and category <= 660:
        cat = 'Fair'
    elif category >= 661 and category <= 780:
        cat = 'Good'
    elif category >= 781 and category <= 850:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#while loop

i=1

while i<10:
    print(i)
    i = i +1

#error handling 

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = 'red'
    
    try:
        if category >= 300 and fico <= 400:
            cat = 'Very Poor'
        elif category >= 401 and category <= 600:
            cat = 'Poor'
        elif category >= 601 and category <= 660:
            cat = 'Fair'
        elif category >= 661 and category <= 780:
            cat = 'Good'
        elif category >= 781 and category <= 850:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
            
    except:
        cat = 'Error = Unknown'
    ficocat.append(cat)
    
#loc 

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']  <= 0.12, 'int.rate.type'] = 'Low'


#group by and size

catplat = loandata.groupby(['fico.category']).size()
catplat.plot.bar(color = 'red', width = 0.1)
plt.show()


catplot1 = loandata.groupby(['purpose']).size()
catplot1.plot.bar(color = 'yellow', width = 0.2)
plt.show()

#scatter plot

ypoint = loandata['AnnualIncome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'green')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)













