from twython import Twython
import random
import time

APP_KEY='APP KEY HERE'
APP_SECRET='APP SECRET HERE'
OAUTH_KEY='OAUTH KEY HERE'
OAUTH_SECRET='OAUTH SECRET HERE'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_KEY, OAUTH_SECRET)

sides=['heads','tails']

while True:
	number=random.randint(10000000, 100000000)
	delay = random.randint(60, 86399)
	delay = delay - (delay % 60)
	hours = delay / 3600
	minutes = (delay % 3600) / 60
	Status = 'A happy random number is '
	Status += `number`
	Status += ' and a virtual coin landed on '
	Status += random.choice(sides)
	Status += '. Next update in '
	if hours > 0:
		Status += `hours`
		if hours == 1:
			Status += ' hour'
		else:
			Status += ' hours'
		if minutes > 0:
			Status += ' and '
	if minutes > 0:
		Status += `minutes`
		if minutes == 1:
			Status += ' minute'
		else:
			Status += ' minutes'
	Status += '. Have a random day!'

	print Status
	try:
		twitter.update_status(status=Status)
		time.sleep(delay)
	except:
		print 'An unexpected error occurred.  Trying again...'
