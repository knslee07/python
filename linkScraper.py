import requests
result=requests.get("http://oreilly.com/store/samplers.html")
result.status_code
c=result.content
from bs4 import BeautifulSoup
soup = BeautifulSoup(c)
samples = soup.findAll("a", "item-title")
samples[0]
"""<a class="item-title" href="http://cdn.oreilly.com/oreilly/booksamplers/9780596004927_sampler.pdf">
Programming Perl </a>"""

data = {}
for a in samples:
  title = a.string.strip()   # see how other parts are stripped from the html.
  data[title] = a.attrs['href'] # only link addresses are extracted
