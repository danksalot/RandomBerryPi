# RandomBerryPi
My [Raspberry Pi](https://www.raspberrypi.org/) likes to pick (pseudo)random things, so I've built a couple of programs that allow it to do just that.  I setup the Twitter account [@RandomBerryPi](https://twitter.com/RandomBerryPi) so that it can share everything it does with the world.  

I am using the [Twython](https://github.com/ryanmcgrath/twython) Python library to post to Twitter.

Enjoy!

# RandomTweet
RandomTweet.py is a program that is posting to Twitter as @RandomBerryPi.  It uses Python to choose a random number, perform a virtual coin flip, and choose when it will post next.

This is an example tweet: **A happy random number is 51621166 and a virtual coin landed on tails. Next update in 15 hours and 12 minutes. Have a random day!**

The range for the random number is 10,000,000 - 99,999,999.  The coin flip can be heads or tails.  The next update can be anywhere from one minute to 23 hours and 59 minutes.

The program posts these to Twitter then waits the decided amount of time before running again.

The program is run by designating the Twitter account details in the RandomTweet.py file and running it via the command line.  In order to keep the program running after the terminal window is closed, use the nohup command:

nohup python RandomTweet.py $

The $ symbol is required to be used on the end of this command so that it will continue to run in the background after the terminal window is closed.

# RandomPowerball
RandomPowerball.py is a program that is posting to Twitter as @RandomBerryPi.  It uses Python to choose random lottery numbers for the Powerball lottery.  It then checks if the last numbers it picked were winners or not and posts to Twitter.

This is an example tweet: **Last time I would have lost everything playing Powerball. Wah Wah! Here are some new picks : 12 36 48 11 33 (8). Have a random day!**

The Powerball lottery is setup to pick 5 white balls that can be numbered 1 to 69, and one red PowerBall that can be from 1 to 26. 

The Powerball numbers are picked Wednesday and Saturday nights, and the results are posted to http://data.ny.gov/resource/d6yy-54nr.json so I setup the program with cron (https://en.wikipedia.org/wiki/Cron) to run on Thursday and Sunday mornings.

