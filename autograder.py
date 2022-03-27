"""
Autograder
"""
import pandas as pd
import os
import traceback
from hw0 import *

FILENAME = 'stocks.dat'
OUTFILE = 'stocks.csv'

#Are you reading the data properly
def test1():
	try:
		parsed = read_file(FILENAME)
	except:
		print('Error in read_file')
		traceback.print_exc()
		return False

	p10 = ('AAMC', 'Altisource Asset Management')
	p1016 = ('CAI', 'CAI International')
	p6042 = ('TTEC', 'TTEC Holdings')

	if (parsed[10] == p10) and \
	   (parsed[1016] == p1016) and \
	   (parsed[6042] == p6042):
		return True
	else:
		print('The output doesn\' match the tests, did you handle leading and trailing spaces')
		return False


#Are you writing the data properly
def test2():
	try:
		parsed = read_file(FILENAME)
	except:
		print('Error in read_file')
		traceback.print_exc()
		return False

	try:
		write_csv(parsed,OUTFILE)
	except:
		print('Error in write_csv')
		traceback.print_exc()
		return False

	if os.path.exists(OUTFILE):
		return True
	else:
		print('write_csv did not actually write a file')
		return False

#Is the final CSV of the right format
def test3():
	try:
		parsed = read_file(FILENAME)
	except:
		print('Error in read_file')
		traceback.print_exc()
		return False

	try:
		write_csv(parsed, OUTFILE)
	except:
		print('Error in write_csv')
		traceback.print_exc()
		return False

	df = pd.read_csv(OUTFILE)

	if list(df.columns) == ['ticker','name']:
		return True
	else:
		print('Your column headers seem to be off')
		return False


	if len(df) == 6674:
		return True
	else:
		print('Your csv file seems to be the wrong size')
		return False

print('Passed Test 1: ', test1())
print('Passed Test 2: ',test2())
print('Passed Test 3: ',test3())