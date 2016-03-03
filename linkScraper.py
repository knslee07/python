from bs4 import BeautifulSoup
soup = BeautifulSoup(c)
samples = soup.find_all("a", "item-title")
samples[0]
"""<a class="item-title" href="http://cdn.oreilly.com/oreilly/booksamplers/9780596004927_sampler.pdf">
Programming Perl </a>"""

data = {}
for a in samples:
  title = a.string.strip()
  data[title] = a.attrs['href']
