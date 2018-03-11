
# Look up ISBN with Worldcat

#   python isbn.py  3795110521

import sys, urllib.request
from urllib.error import URLError, HTTPError
from  ast import literal_eval
import pickle

dirty = False
try:
	isbn_cache = pickle.load(open("isbn_cache.dat", 'rb'))
	print(len(isbn_cache), "entries in database")
except:
	#raise
	isbn_cache = {}

def xisbn(ISBN):
	try:
		resp = urllib.request.urlopen("http://xisbn.worldcat.org/webservices/xid/isbn/"+str(ISBN)+"?method=getMetadata&format=python&fl=*")
	except HTTPError as err:
		print('The server couldn\'t fulfill the request.'); print('Error code: ', err.code);
	except URLError as err:
		print('Failed to reach the server.'); print('Reason: ', err.reason);

	else:
		data = resp.read()
		text = data.decode('utf-8')
		d = literal_eval(text)
		print(d)
		return d
	return None

i = sys.argv[1]
if i not in isbn_cache.keys():
	r = xisbn(i)
	if r != None and r['stat'] == 'ok':
		print("adding info...")
		dirty = True
		isbn_cache[i] = r
	elif r != None and r['stat'] == 'unknownId':
		print(80 * '*')
		print("*** unknown:", i)

if dirty:
	#shutil.move("isbn_cache.dat", "isbn_cache.dat.bak")
	print("writing...")
	pickle.dump(isbn_cache, open("isbn_cache.dat", 'wb'), 1)


