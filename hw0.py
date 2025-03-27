"""
Introductory programming assignment.
"""
import pandas as pd

"""
!!!TODO!!!
"""
def read_file(filename):
	'''Input: filename (location of stock.dat)
	   Output: a list of tuples (ticker, name)
	'''

	df = pd.read_csv(filename, delimiter=' - ', names=['ticker', 'name'])

	return list(df.itertuples(index=False))

"""
!!!TODO!!!
"""
def write_csv(parsed, outfile):
	'''Input: a list of tuples (ticker,name), output location
	   Output: None/Void, writes a file
	'''

	parse_df = pd.DataFrame(parsed, columns=['ticker', 'name'])
	df_csv = parse_df.to_csv(outfile, index='ticker')

	return df_csv