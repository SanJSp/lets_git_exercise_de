import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = './index.md'


def check_if_string_in_file(file_name, string_to_search):
	f = open(file_name, 'r')
	Lines = f.readlines() 
	regEx = string_to_search + '([A-Z]|[a-z])+'
	for line in Lines:
		if re.match(regEx, line):
			return True
	f.close()
	return False


if check_if_string_in_file(directory, '# '):
   print('Yes')
else:
   print('No')