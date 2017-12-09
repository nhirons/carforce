import pandas as pd
import numpy as np

def one_hot_encode(series, rank_threshold = np.inf, count_threshold = 0):

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
		other_cats = n_lowest_ranked_cats(series, cats_below_count)
	elif cats_below_rank == 0:
		other_cats = []
	else:
		other_cats = n_lowest_ranked_cats(series, cats_below_rank)

	# Convert categories
	series = convert_cats_to_other(series, other_cats)

	# Get dummies
	df_dummies = pd.get_dummies(series, prefix = series.name)

	return df_dummies

def convert_cats_to_other(series, other_categories):

	map_to_other_dict = {cat:'other' for cat in other_categories}
	series = series.replace(map_to_other_dict)
	return series

def n_lowest_ranked_cats(series, n_lowest):

	return series.value_counts()[-n_lowest:].index

def add_one_hot_encoding(df, columns, rank_threshold = np.inf, count_threshold = 0):

	to_concat = [df]
	df_dummies_list = create_dummies_list(df, columns, rank_threshold, count_threshold)
	to_concat.extend(df_dummies_list)
	df_with_ohe = pd.concat(to_concat, axis = 1)

	return df_with_ohe

def create_dummies_list(df, columns, rank_threshold, count_threshold):

	dummies_list = [one_hot_encode(df[col], rank_threshold, count_threshold) for col in columns]
	return dummies_list
