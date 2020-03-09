import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = './index.md'


def check_if_string_in_file(file_name):
	heading = False
	count = 0
	f = open(file_name, 'r')
	Lines = f.readlines() 
	for line in Lines:
		if re.match('## ([A-Z]|[a-z])+', line):
			heading = True
			continue
		if (heading == True) and re.findall('\* ([A-Z]|[a-z])+', line):
			count = count + 1
		if (heading == True) and re.findall('\* ([A-Z]|[a-z])+', line) and (count > 2):
			return True
	f.close()
	return False


if check_if_string_in_file(directory):
   print('Yes')
else:
   print('No')