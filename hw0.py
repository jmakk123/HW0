import pandas as pd

def read_file(filename):
	'''Input: filename (location of stock.dat)
	   Output: a list of tuples (ticker, name)
	'''

	df = pd.read_csv(filename, delimiter=' - ', names=['ticker', 'name']).itertuples(index=False, name=None)

	return df

def write_csv(parsed, outfile):
	'''Input: a list of tuples (ticker,name), output location
	   Output: None/Void, writes a file
	'''

	parse_df = pd.DataFrame(parsed, columns=['ticker', 'name']).set_index('ticker').to_csv(outfile)
	df_csv = parse_df.to_csv(outfile, index='ticker')

	return df_csv

if __name__ == "__main__": 
    write_csv(read_file('stocks.dat'), "output.csv")
