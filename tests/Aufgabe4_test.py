import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = './index.md'


def check_if_string_in_file(file_name, string_to_search):
	f = open(file_name, 'r')
	Lines = f.readlines()
	regEx = string_to_search + '\s?([A-Z]|[a-z]|[\u00c4-\u02AF]|[0-9])+'
	for line in Lines:
		if re.findall('>\s?([A-Z]|[a-z]|[\u00c4-\u02AF]|[0-9])+', line):
			return True
	f.close()
	return False


if check_if_string_in_file(directory, '##'):
   print('Yes')
else:
   print('No')
