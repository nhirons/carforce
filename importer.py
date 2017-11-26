import pandas as pd
import numpy as np


def read_dfs():

	df1 = pd.read_csv('./data/20170622_1514_SV (376k).csv')
	df2 = pd.read_csv('./data/SVC Aggregate (115k).csv')

	print('df1 has {} rows and {} columns'.format(*df1.shape))
	print('df2 has {} rows and {} columns'.format(*df2.shape))

	return df1, df2

def create_aggregate_df(df1, df2):

	df3 = pd.concat([df1,df2], join = 'outer')

	print('The concatenated dataframe has {} rows and {} columns'.format(*df3.shape))

	return df3


def keep_error_codes_only(df):

	df_errors = df.dropna(axis = 0, subset = ['CASS_STD_ERROR_CD'])

	return df_errors