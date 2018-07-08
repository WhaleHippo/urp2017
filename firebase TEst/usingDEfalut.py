from firebase import firebase
import datetime
firebase = firebase.FirebaseApplication('https://firetest-d88ea.firebaseio.com/', None)
now = datetime.datetime.now()
print now
while True:
	firebase.post('/users', 'command')
	result = firebase.get('/command', None)
	now = datetime.datetime.now();
	print now
