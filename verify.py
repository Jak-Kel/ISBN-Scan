
# Verify ISBNs and add to database

import sys
from isbnlib import *
from os import system

# only try to get info for ISBN-only lines:

for l in open(sys.argv[1], 'r').readlines():
	i = l.strip()
	if ':' in i:
		i = i.split(':')[1]
	if len(i) < 1 or ',' in l:
		continue
	if is_isbn10(i) or is_isbn13(i):
		print(i, "OK")
		if '--noweb' not in sys.argv:
			system("python3 isbn.py %s" % i)
	else:
		print(i, ">>>>>>>>>>>>>>>>>>>> Not OK <<<<<<<<<<<<<<<<<<<<<<<")



