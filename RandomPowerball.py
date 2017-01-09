import random
import json
import urllib2
from twython import Twython

def GetLastPicks():
	filename = "currentPicks.txt"
	with open(filename) as f:
		return map(int, f.readlines())

def GetWinningNumbers():
	url = urllib2.urlopen("http://data.ny.gov/resource/d6yy-54nr.json")
	winningNumbers = json.loads(url.read())
	return map(int, winningNumbers[0]["winning_numbers"].split(' '))

def GetNewPicks():
	filename = "currentPicks.txt"
	newPicks = random.sample(range(1, 70), 5)
	newPicks.append(random.randint(1, 26))
	with open(filename, "w") as currentPicks:
		currentPicks.write('\n'.join(map(str, newPicks)))
	return newPicks

def GetPowerballOutcome(picks, winningNumbers):
	# score = number of white ball matches with a +10 offset if the powerball was correct
	winOptions = {
		0:"lost everything", 1:"lost everything", 2:"lost everything", 3:"won $7", 4:"won $100", 5:"won $1,000,000", 
		10:"won $4", 11:"won $4", 12:"won $7", 13:"won $100", 14:"won $50,000", 15:"won the GRAND PRIZE"
	}
	
	score = sum(1 for pick in picks[0:5] if pick in winningNumbers[0:5])
	score += (10 if picks[5] == winningNumbers[5] else 0)

	return winOptions[score]

APP_KEY='APP KEY HERE'
APP_SECRET='APP SECRET HERE'
OAUTH_KEY='OAUTH KEY HERE'
OAUTH_SECRET='OAUTH SECRET HERE'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_KEY, OAUTH_SECRET)

lastNumbers = GetLastPicks()
winningNumbers = GetWinningNumbers()
outcome = GetPowerballOutcome(lastNumbers, winningNumbers)
newNumbers = GetNewPicks()

Status = "Last time I would have {} playing Powerball.".format(outcome)
Status += " Wah Wah!" if outcome == "lost everything" else " Hurray!"
Status += " Here are some new picks :"
Status += " {} {} {} {} {} ({}).".format(newNumbers[0], newNumbers[1], newNumbers[2], newNumbers[3], newNumbers[4], newNumbers[5])
Status += " Have a random day!"

try:
	print Status
	twitter.update_status(status = Status)
except:
	print 'Lost the lottery ticket, I will have to wait until next time.'
