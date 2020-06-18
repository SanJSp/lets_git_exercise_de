import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = './index.md'


def check_if_string_in_file(file_name, string_to_search):
	heading = False
	f = open(file_name, 'r')
	Lines = f.readlines()
	regEx = string_to_search + '([A-Z]|[a-z]|[\u00c4-\u02AF]|[0-9])+'
	for line in Lines:
		if re.match(regEx, line):
			heading = True
			continue
		if re.match('## ([A-Z]|[a-z]|[\u00c4-\u02AF]|[0-9])+', line):
			heading = False
			continue
		if (heading == True) and re.findall('([A-Z]|[a-z]|[\u00c4-\u02AF]|[0-9])+', line):
			return True
	f.close()
	return False


if check_if_string_in_file(directory, '# '):
   print('Yes')
else:
   print('No')
