import pandas as pd
import numpy as np

def one_hot_encode(df, col, rank_threshold, count_threshold = 0):

	series = df[col]

	# Returns one hot encoded dataframe.
	# Categories with counts below count_threshold
	# or a rank below rank_threshold become 'other'

	cats_below_count = (series.value_counts() < count_threshold).sum()

	if rank_threshold > len(series.value_counts()):
		cats_below_rank = 0
	else:
		cats_below_rank = len(series.value_counts()) - rank_threshold

	# Select the highest number of categories below either threshold
	if cats_below_count > cats_below_rank:
		other_cats = series.value_counts()[-cats_below_count:].index
	elif cats_below_rank == 0:
		other_cats = []
	else:
		other_cats = series.value_counts()[-cats_below_rank:].index
	

	# Convert categories
	cat_changes = {cat:'other' for cat in other_cats}
	series = series.replace(cat_changes)

	# Get dummies
	df_dummies = pd.get_dummies(series, prefix = col)

	return df_dummies

def add_one_hot_encoding(df, columns, rank_threshold, count_threshold = 0):

	to_concat = [df]

	df_dummies_list = [one_hot_encode(df, col, rank_threshold, count_threshold) for col in columns]

	to_concat.extend(df_dummies_list)

	df_with_ohe = pd.concat(to_concat, axis = 1)

	return df_with_ohe