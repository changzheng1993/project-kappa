# These functions refer to the lecture of Day 13

import numpy as np
import matplotlib.pyplot as plt

def scale_design_mtx(X):
	"""utility to scale the design matrix for display
	his scales the columns to their own range so we can see the variations
	across the column for all the columns, regardless of the scaling of the
	olumn.
	"""
	mi, ma = X.min(axis=0), X.max(axis=0)
	# Vector that is True for columns where values are not
	# all almost equal to each other
	col_neq = (ma - mi) > 1.e-8
	Xs = np.ones_like(X)
	# Leave columns with same value throughout with 1s
	# Scale other columns to min, max in column
	mi = mi[col_neq]
	ma = ma[col_neq]
	Xs[:,col_neq] = (X[:,col_neq] - mi)/(ma - mi)
	return Xs


def show_design(X, design_title = None):
	""" Show the design matrix nicely """
	plt.imshow(scale_design_mtx(X), interpolation='nearest',cmap='gray', aspect = 0.075) 
	
	if design_title != None:
		plt.title(design_title)