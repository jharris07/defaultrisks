# -*- coding: utf-8 -*-p
"""
Created on Sun Nov 11 12:12:40 2018

@author: Jon
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
PATH= "C:/Users/jon.harris/Desktop/school/final/input/"
print(os.listdir(PATH))
#files = os.listdir(("E:/School/elen239a/final/input"))
files = ['application_train.csv','application_test.csv',]
"""         
          'bureau.csv', 
         'bureau_balance.csv', 'credit_card_balance.csv',
         'installments_payments.csv', 'POS_CASH_balance.csv',
         'previous_application.csv']
"""
#PATH = "E:/School/elen239a/final/input/"

data_files=[]
data=[]
print (files)




for file in files:
    stuff = pd.read_csv(PATH+file,header=0)
    #print(stuff)
    data_files.append(file)
    data.append(stuff)

print (len(data))        
for i in range(len(data)):
    print(data_files[i])
    print(data[i].columns.values)


print("count of targets w/ histogram")
print(data[0]['TARGET'].value_counts())
print(data[0]['TARGET'].astype(int).plot.hist())


print("some fuckery")
int64cols = data[0].select_dtypes('int64').columns.values.tolist()
objectcols = data[0].select_dtypes('object').columns.values.tolist()
float64cols = data[0].select_dtypes('float64').columns.values.tolist()

int64cols.remove("SK_ID_CURR")


for keyword in int64cols:
    print(keyword)
    #print(data[0][keyword].value_counts())
    data[0][keyword].astype(int).plot(kind='hist')
    #data[0][keyword].astype(int).plot.line()
    plt.show()

print (int64cols)
print('\n')
print (objectcols)
print('\n')
print (float64cols)
print('\n')

print("MISSING DATA ANALYSIS")

def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns

missing_values = missing_values_table(data[0])
print(missing_values.head(20))

print (data[0].dtypes.value_counts())
print(data[0].select_dtypes('object').apply(pd.Series.nunique, axis = 0))
app_train = data[0]
app_test = data[1]
le = LabelEncoder()
le_count = 0
for col in app_train:
    if app_train[col].dtype == 'object':
        # If 2 or fewer unique categories
        if len(list(app_train[col].unique())) <= 2:
            # Train on the training data
            le.fit(app_train[col])
            # Transform both training and testing data
            app_train[col] = le.transform(app_train[col])
            #app_test[col] = le.transform(app_test[col])
            
            # Keep track of how many columns were label encoded
            le_count += 1
            
print('%d columns were label encoded.' % le_count)

app_train = pd.get_dummies(app_train)
app_test = pd.get_dummies(app_test)

print('Training Features shape: ', app_train.shape)
print('Testing Features shape: ', app_test.shape)
#"""
