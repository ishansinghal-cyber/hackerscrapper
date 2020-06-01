import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(res, 'html.parser')

storylink = soup.select(".storylink")
subtext 	= soup.select(".subtext")


hn = {}

for idx,story in enumerate(storylink):
	title	   = storylink[idx].text
	story_link = storylink[idx].get("href")
	votes      = int(subtext[idx].select(".score")[0].text.replace(" points",""))
	if(votes > 100):
		hn.update({"Title":title,"storylink":story_link,"votes":votes})
		pprint(hn)
	else:
		continue