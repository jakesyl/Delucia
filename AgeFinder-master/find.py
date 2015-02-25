'''
Jake Sylvestre 
Attempts to Guess Age
'''

import TwitterUtility
import sqlite3
from nltk.corpus import stopwords

def freq_finder(tweets):
	words = dict()
	
	stop = stopwords.words('english')

	for tweet in tweets:

		twits = tweet.split(' ')
		
		for twit in twits:
			if twit in stop:
				continue

			if twit in words:
				tel = words[twit]
				del words[twit]
				words[twit] = tel + 1 

			else:
				words[twit] = 1
			return words


