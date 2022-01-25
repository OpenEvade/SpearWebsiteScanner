import requests
from googlesearch import search
url = "http://" + input("[!] Domain:")
server = requests.get(url).headers['server']
urls = search("site:exploit-db.com " + server + " CVE -(ghdb)", num_results=5)
print(server)
print(urls[0])
