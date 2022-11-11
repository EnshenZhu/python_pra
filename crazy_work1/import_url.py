import urllib
from urllib.request import urlopen

url = 'www.google.com'

req = urllib.request(url)
content = urllib.urlopen(req).read()