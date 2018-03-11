
# List all books

from isbnlib import *
from os import system
import csv, pickle

books = []
isbn_cache = pickle.load(open("isbn_cache.dat", 'rb'))
print(len(isbn_cache), "entries in database")

system('grep "" input/*.txt > books.txt')

h = open("output.html", 'w')
h.write('<html><head><meta charset="utf-8" /></head><body><table border="1">\n')
h.write('<tr><th>#</th><th>Title</th><th>Author</th><th>Year</th><th>Publisher</th><th>lang.</th><th>Place</th><th>ISBN/GTIN</th></tr>\n')
num = 1

cf = open("output.csv", 'w', newline = '')
cw = csv.writer(cf)

def getloc(x):
	a = x.split(':')[0]
	return a.split('/')[1][:-4]

def empty_aut(x):
	if x == '-':
		return ''
	else:
		return x

for l in open('books.txt', 'r').readlines():
	i = None
	if ',' not in l:
		i = get_canonical_isbn(l)
	if i == None:
		if ',' not in l:
			continue
		w = l.split(',')
		t1 = ''.join(w[0].split(':')[1:])
		a1 = empty_aut(w[2]) + ' ' + empty_aut(w[1])
		a1 = a1.strip()
		try:
			y1 = w[3]
		except:
			print(l)
			raise
		try:
			p1 = w[4]
		except:
			p1 = ''
		try:
			ii = w[5]
		except:
			ii = ''
		loc = getloc(l)
		h.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (num, t1, a1, y1, p1, '', loc, ii))
		cw.writerow([num, t1, a1, y1, p1, '', loc, ii])
		num += 1
		continue
	if is_isbn10(i) or is_isbn13(i):
		rec = isbn_cache.get(i, None)
		if rec != None:
			r = rec['list'][0]

			t1 = r.get('title', '')
			a1 = r.get('author', '')
			y1 = r.get('year', '')
			p1 = r.get('publisher', '')
			l1 = r.get('lang', '')
			loc = getloc(l)
			h.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (num, t1, a1, y1, p1, l1, loc, i))
			cw.writerow([num, t1, a1, y1, p1, l1, loc, i])
			num += 1
		else:
			print("******** NO INFO", i)
	else:
		print(i, "*** Not OK")

h.write('</body></html>\n')

