# -*- coding: utf-8 -*-
"""Prodigy_ML_task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pNSnUWWAJg5od0gfYdknUbiJwIOLd67A
"""

# to predict the house price using Linear Regression

import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Let's load the dataframes of train.csv and test.csv
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

print(train_df.columns)

# Let's do some data preprocessing for the records in train dataframe
tr_LivArea_Median = math.floor(train_df['GrLivArea'].median())
train_df['GrLivArea'].fillna(tr_LivArea_Median, inplace=True)

tr_BsmtSF_Median = math.floor(train_df['TotalBsmtSF'].median())
train_df['TotalBsmtSF'].fillna(tr_BsmtSF_Median, inplace=True)

tr_GarageArea_Median = math.floor(train_df['GarageArea'].median())
train_df['GarageArea'].fillna(tr_GarageArea_Median, inplace=True)

tr_WoodDeck_Median = math.floor(train_df['WoodDeckSF'].median())
train_df['WoodDeckSF'].fillna(tr_WoodDeck_Median, inplace=True)

tr_OpenPorch_Median = math.floor(train_df['OpenPorchSF'].median())
train_df['OpenPorchSF'].fillna(tr_OpenPorch_Median, inplace=True)

tr_EnclosedPorch_Median = math.floor(train_df['EnclosedPorch'].median())
train_df['EnclosedPorch'].fillna(tr_EnclosedPorch_Median, inplace=True)

tr_3SsnPorch_Median = math.floor(train_df['3SsnPorch'].median())
train_df['3SsnPorch'].fillna(tr_3SsnPorch_Median, inplace=True)

tr_ScreenPorch_Median = math.floor(train_df['ScreenPorch'].median())
train_df['ScreenPorch'].fillna(tr_ScreenPorch_Median, inplace=True)

tr_PoolArea_Median = math.floor(train_df['PoolArea'].median())
train_df['PoolArea'].fillna(tr_PoolArea_Median, inplace=True)

tr_Bsmt_FB_Median = math.floor(train_df['BsmtFullBath'].median())
train_df['BsmtFullBath'].fillna(tr_Bsmt_FB_Median, inplace=True)

tr_Bsmt_HB_Median = math.floor(train_df['BsmtHalfBath'].median())
train_df['BsmtHalfBath'].fillna(tr_Bsmt_HB_Median, inplace=True)

tr_FB_Median = math.floor(train_df['FullBath'].median())
train_df['FullBath'].fillna(tr_FB_Median, inplace=True)

tr_HB_Median = math.floor(train_df['HalfBath'].median())
train_df['HalfBath'].fillna(tr_HB_Median, inplace=True)

tr_Bedroom_Median = math.floor(train_df['BedroomAbvGr'].median())
train_df['BedroomAbvGr'].fillna(tr_Bedroom_Median, inplace=True)

train_df

# Edit fields in train dataframe
train_df['TotSqFt'] = train_df['GrLivArea'] + train_df['TotalBsmtSF'] + train_df['GarageArea'] + train_df['WoodDeckSF'] + train_df['OpenPorchSF'] + train_df['EnclosedPorch'] + train_df['3SsnPorch'] + train_df['ScreenPorch'] + train_df['PoolArea']
train_df['TotBaths'] = train_df['BsmtFullBath'] + train_df['BsmtHalfBath'] + train_df['FullBath'] + train_df['HalfBath']
train_df = train_df.drop(columns=train_df.columns.difference(['Id', 'TotSqFt', 'TotBaths', 'BedroomAbvGr', 'SalePrice']))
train_df

# Edit fields in test dataframe
test_df['TotSqFt'] = test_df['GrLivArea'] + test_df['TotalBsmtSF'] + test_df['GarageArea'] + test_df['WoodDeckSF'] + test_df['OpenPorchSF'] + test_df['EnclosedPorch'] + test_df['3SsnPorch'] + test_df['ScreenPorch'] + test_df['PoolArea']
test_df['TotBaths'] = test_df['BsmtFullBath'] + test_df['BsmtHalfBath'] + test_df['FullBath'] + test_df['HalfBath']
test_df = test_df.drop(columns=test_df.columns.difference(['Id', 'TotSqFt', 'TotBaths', 'BedroomAbvGr', 'SalePrice']))
test_df

# Specify features and target variables from training dataframe
x = train_df[['TotSqFt', 'TotBaths', 'BedroomAbvGr']]
y = train_df['SalePrice']
# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# Train the linear regression model
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)

# Let's see the coefficient and intercept values of the equation y = mx + c
print(f"\nCoefficients : {lr_model.coef_}\nIntercept : {lr_model.intercept_}")

test_df.info()

missing_values = test_df.isnull().sum()
print(missing_values)

test_df = test_df.dropna()
test_df

# Let's make predictions on the test set of the split
y_pred = lr_model.predict(x_test)
# Let's evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error on Test Set: {mse}")

rmse = math.sqrt(mse)
print(f"\nDeviation : {rmse}")

test_predictions = lr_model.predict(test_df[['TotSqFt', 'TotBaths', 'BedroomAbvGr']])

# Create a dataframe for submission
predicted_df = pd.DataFrame({'Id': test_df['Id'], 'TotSqFt' : test_df['TotSqFt'], 'TotBaths' : test_df['TotBaths'] , 'BedroomAbvGr' : test_df['BedroomAbvGr'], 'SalePrice': test_predictions})
predicted_df

# Let's save the submission dataframe to a CSV file
c=predicted_df.to_csv('HousePricesPred.csv', index=False)
c

from sklearn.linear_model import LinearRegression
model = LinearRegression()

#Cross-validation to assess model performance
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
cv_scores = cross_val_score(model, x, y, cv=5)
print('Cross-Validation Scores:', cv_scores)
print('Mean CV Score:', cv_scores.mean())

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()