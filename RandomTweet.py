from twython import Twython
import random
import time

def getDelayString():
	delay = random.randint(60, 86399)
	delay = delay - (delay % 60)
	hours = delay / 3600
	minutes = (delay % 3600) / 60
	message = ""
	if hours > 0:
		message += `hours` + ' hour'
		if hours > 1:
			message += 's'
	if hours > 0 and minutes > 0:
		message += ' and '
	if minutes > 0:
		message += `minutes` + ' minute'
		if minutes > 1:
			message += 's'
	return message

APP_KEY='APP KEY HERE'
APP_SECRET='APP SECRET HERE'
OAUTH_KEY='OAUTH KEY HERE'
OAUTH_SECRET='OAUTH SECRET HERE'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_KEY, OAUTH_SECRET)

while True:
	Status = 'A happy random number is ' + `random.randint(10000000, 100000000)`
	Status += ' and a virtual coin landed on ' + random.choice(['heads','tails'])
	Status += ". Next update in " + getDelayString()
	Status += '. Have a random day!'

	print Status
	try:
		twitter.update_status(status=Status)
		time.sleep(delay)
	except:
		print 'An unexpected error occurred.  Trying again...'
