import random
import itertools
import json
import urllib2
from twython import Twython

def GetLastNumbers():
	filename = "currentPicks.txt"
	with open(filename) as f:
		return map(int, f.readlines())

def GetWinningNumbers():
	url = urllib2.urlopen("http://data.ny.gov/resource/d6yy-54nr.json")
	winningNumbers = json.loads(url.read())
	return map(int, winningNumbers[0]["winning_numbers"].split(' '))

def GetNewNumbers():
	filename = "currentPicks.txt"
	newPicks = random.sample(range(1, 70), 5)
	newPicks.append(random.randint(1, 26))
	with open(filename, "w"):
		pass
	for pick in newPicks:
		with open(filename, "a") as currentPicks:
			currentPicks.write("{}{}".format(pick, "\n"))
	return newPicks

def GetPowerballWinnings(picks, winningNumbers):
	whitePicks = set(itertools.islice(picks, 0, 5))
	redPick = picks[5]
	whiteWinners = set(itertools.islice(winningNumbers, 0, 5))
	redWinner = winningNumbers[5]
	matches = len(whitePicks & set(whiteWinners))
	redMatch = redPick == redWinner
	winnings = "lost everything"
	if (matches == 5 and redMatch):
		winnings = "won the GRAND PRIZE"
	elif (matches == 5):
		winnings = "won $1,000,000"
	elif (matches == 4 and redMatch):
		winnings = "won $50,000"
	elif (matches == 4):
		winnings = "won $100"
	elif (matches == 3 and redMatch):
		winnings = "won $100"
	elif (matches == 3):
		winnings = "won $7"
	elif (matches == 2 and redMatch):
		winnings = "won $7"
	elif (redMatch):
		winnings = "won $4"
	return winnings

lastNumbers = GetLastNumbers()
winningNumbers = GetWinningNumbers()
winnings = GetPowerballWinnings(lastNumbers, winningNumbers)
newNumbers = GetNewNumbers()

APP_KEY='APP KEY HERE'
APP_SECRET='APP SECRET HERE'
OAUTH_KEY='OAUTH KEY HERE'
OAUTH_SECRET='OAUTH SECRET HERE'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_KEY, OAUTH_SECRET)

Status = "Last time I would have {} playing Powerball.".format(winnings)
if (winnings == "lost everything"):
	Status += " Wah Wah!"
else:	
	Status += " Hurray!"
Status += " Here are some new picks :"
Status += " {} {} {} {} {} ({}).".format(newNumbers[0], newNumbers[1], newNumbers[2], newNumbers[3], newNumbers[4], newNumbers[5])
Status += " Have a random day!"

try:
	print Status
	twitter.update_status(status = Status)
except:
	print 'Lost the lottery ticket, I will have to wait until next time.'
