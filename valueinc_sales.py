# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:07:24 2022

@author: psson
"""

import pandas as pd

#reading csv file
data=pd.read_csv('transaction.csv',sep=';')

#summary of data-dataframe
data.info()

#initializing dictionary
var={'FirstName':'Pooja','LastName':'Soneja'}

#Basics of Calculations
CostPerItem=11.73
SellingPricePerItem=21.11
NumberOfItemsPurchased=6

CostPerTransaction=NumberOfItemsPurchased*CostPerItem
SalesPerTransaction=NumberOfItemsPurchased*SellingPricePerItem

#Reading columns from data-dataframe
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction1 = CostPerItem * NumberOfItemsPurchased

#Adding new column to the dataframe

data['CostPerTransaction'] = CostPerTransaction1

#SalesPerTransaction

data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

#Profit

data['ProfitPerCalculation'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']

#Round Markup

data['RoundMarkup'] = round( data['Markup'], 2)

#Know column type

print(data['Day'].dtype)

#Convert integer data type to string

day = data['Day'].astype(str)
print(day.dtype)
year=data['Year'].astype(str)

#concatenating date columns

my_date = day + '-' + data['Month'] + '-' + year

data['Date'] = my_date

#Use iloc to view specific rows/columns

data.iloc[0] #Views rows with index 0
data.iloc[0:3] #first three rows
data.iloc[-5:] #last 5 rows

data.head(5) # first five rows

data.iloc[:,2] #all the rows of the second column

data.iloc[4,3] # value in 4th row 3rd column

#split column

split_col = data['ClientKeywords'].str.split(',',expand= True)

#Appending client keyword columns in the data - dataFrame

data['ClientAge'] = split_col[0]
data['ClientBusiness'] = split_col[1]
data['ClientRoyalty'] = split_col[2]

#using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['ClientRoyalty'] = data['ClientRoyalty'].str.replace(']','')

data.iloc[0]

#using lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#importing and reading new file

seasonsFile = pd.read_csv('value_inc_seasons.csv',sep = ';')

#merging files

data = pd.merge(data, seasonsFile, on = 'Month')

#dropping columns

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Month', axis = 1)
data = data.drop('Year', axis = 1)

#export to csv file

data.to_csv('Valueinc_Cleaned.csv', index = False)