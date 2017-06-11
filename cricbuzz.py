import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) == 2:
	url = str(sys.argv[1])
else:
	print ("Only url is expected")
	sys.exit()

	
try:
	page =  requests.get(url)
except (requests.exceptions.MissingSchema) as e:
	print ("Missing Schema")
	print (e)
	sys.exit()
else:
	pass
	
strip = "http://www.cricbuzz.com/live-cricket-scorecard/1"

if strip not in url:
	print ("Try URL beginning with: {}".format(strip))
	print ("Press Ctrl+C and try again")
	sys.exit()	

soup = BeautifulSoup(page.text, 'html.parser')

text = soup.find_all('div', attrs = {'class': 'cb-col cb-col-100 cb-scrd-itms'})
#print (len(text))

team = soup.find_all('span', class_ = None)
#print ((team))
#n = len(team)

playing = []

for i in team:
	if "Innings" in str(i):
		playing.append(i.get_text())

score = []
 
for i in text:
	if "Total" in str(i):
		score.append(i.get_text())
for i in range(len(playing)):
	if len(playing[i]) > 0:
		print ("{} \n{}".format(playing[i], score[i]))
	
