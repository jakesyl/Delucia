'''
Jake Sylvestre
Learning Script CLI
'''

import TwitterUtility
import lexstore

def prompt():# I hate CLIS too
	lexstore.create_db()
	print("Enter Twitter Names of similiar ages delimeted by a comma:")
	names = input()
	print ("Enter Age:")
	age = input()
	sort_tweets(names, age)


def sort_tweets(names, age):
	names = names.split(',')
	ages = ['teen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty']#Hopefully garbage collection works fast
	
	age = str(age)
	age = ages[(int(age[0]))-1]#only first number of age, only ints are used for getting from list
	for name in names:
		tweets = TwitterUtility.get_tweets(name)
		for tweet in tweets:
			lexstore.insert(tweet, age)
