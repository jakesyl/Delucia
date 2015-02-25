'''
Jake Sylvestre
Part of the learning module
Forms a lexial of words in an sqllite database
'''

import sqlite3

def create_db(ages = ['teen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'other']):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	try:
		c.execute(" SELECT * FROM db;")
	except sqlite3.OperationalError :
			c.execute(''' CREATE TABLE db(word text, frequency integer, groups text);''') 
	try:
		c.execute(" SELECT * FROM users;")
	except sqlite3.OperationalError :
			c.execute(''' CREATE TABLE users(name text, age text);''') 

def insert(phrase, group):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	empty = []#What a waste of memory
	#Break up phrase
	phrase = phrase.split(' ')
	for word in phrase:
		c.execute(''' SELECT frequency FROM db WHERE word = ? and groups = ?;''', (word, group,))
		freq = c.fetchone()
		print("frequency ")
		print(freq)
		if freq == None or freq == empty:
			#c.execute('''INSERT INTO ?  (word, frequency) VALUES ?, 1''', (group, word,))
			c.execute('''INSERT INTO db (word, frequency, groups) VALUES (?, 1, ?);''', (word, group,))

		else:
			freq = freq[0] + 1# New Frequency
			print(freq) 
			c.execute(''' UPDATE db SET frequency = ? WHERE word = ? and groups = ?;''', (freq,word, group,))
		conn.commit()
		return True
#TESTS

def insert_user(username, age):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	empty = []#What a waste of memory
	c.execute(''' SELECT * FROM users WHERE name = ? and age = ?;''', (username, age,))
	res = c.fetchall()
	if res == empty:
		#c.execute('''INSERT INTO ?  (word, frequency) VALUES ?, 1''', (group, word,))
		c.execute('''INSERT INTO users (name, age) VALUES (?, ?);''', (username, age))
		conn.commit()
	if res != empty:
		return False

	else:
		return True

'''
Get tweets
sort the words by frequency,
look for the words in groups see which one has the highest rank
for every group:
	for word in group:
		0 + (word rank highest first) + word rank in group + word frequency 
'''
