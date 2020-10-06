import speech_recognition as sr 
from time import ctime
import time
import os
from gTTs import gTTs
import requests
import json



def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('I Am Listening...')
		audio = r.listen(source)
	data = ''
	try:
		data = r.recognize_google(audio)
		print('You said: ' + data)
	except sr.UnknownValueError:
		print('Sorry, I Could Not Understand You')
	except sr.RequestError as e:
		print('Request Failed; {0}'.format(e))
	return data

def respond(audiostring):
	print(audiostring)
	tts = gTTs(text=audiostring, lang='en')
	tts.save('speech.mp3')
	os.system('mp321 speech.mp3')

def digital_assistant(data):
	if 'how are you' in data:
		listening = True
		respond('I Am Well')

	if 'what time is it' in data:
		listening = True
		respond(ctime())

	if 'stop listening' in data:
		listening = False
		print('listening stopped')
		return listening
	return listening

time.sleep(2)
respond('Hi Oisin, what Can I Do For You')
listening = True
while listening == True:
	data = listen()
	listening = digital_assistant(data)

