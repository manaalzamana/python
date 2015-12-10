# pythonimport urllib.request
import json
url = "https://restcountries.eu/rest/v1/alpha/co"
pgf=urllib.request.urlopen(url)
content=pgf.read()
pg_str=content.decode('utf-8')
js = json.loads(pg_str)
country = input("Enter the country code:")
found = 0
for k,v in js.items():
	if ( country == v ):
		print(js['nativeName'],js['capital'])
		found = 1
		break
if( found==0 ):
	print("Country not found ")
	print("nativeName: ", js['nativeName'],js['capital'])
