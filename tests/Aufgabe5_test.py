import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = './index.md'


def check_if_string_in_file(file_name):
	f = open(file_name, 'r')
	Lines = f.readlines()
	for line in Lines:
		if re.match('<img([\w\W][^\>]+?)\/>', line):
			return True
	f.close()
	return False

if check_if_string_in_file(directory):
   print('Yes')
else:
   print('No')
