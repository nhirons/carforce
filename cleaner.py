import pandas as pd
import numpy as np

def fix_shortened_makes(make_column_series):

	makes = set(make_column_series.unique())

	# Select only single word make names
	single_word_makes = set([make for make in makes if ' ' not in make])

	# Create list of shortened make names
	short_makes = sorted([make for make in single_makes if \
                   any([make in other for other in single_makes if other != make])])

	# Create corresponding list of actual make names
	real_makes = sorted([make for make in single_makes if \
                   any([other in make for other in single_makes if other != make])])

	# Clean errors
	real_makes.remove('MERCURY')
	real_makes = ['MERCURY' if make == 'MERCEDES' else make for make in long_makes]
	real_makes = ['RAM' if make == 'RAMT' else make for make in long_makes]

	# Create dictionary of shortened names as keys, real names as values
	make_dict = dict(zip(short_makes, real_makes))

	# Replace shortened values in column / series
	fixed_makes = make_column_series.replace(to_replace = make_dict)

	return fixed_makes