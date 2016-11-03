from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class GoogleCalendar():
	
	def __init__(self):
		SCOPES = 'https://www.googleapis.com/auth/calendar'
		CLIENT_SECRET_FILE = 'client_secret.json'
		APPLICATION_NAME = 'SelToCal'

		home_dir = os.path.expanduser('~')
		credential_dir = os.path.join(home_dir, '.credentials')
		if not os.path.exists(credential_dir):
			os.makedirs(credential_dir)
		credential_path = os.path.join(credential_dir,
									   'calendar-python-quickstart.json')

		store = Storage(credential_path)
		self.credentials = store.get()
		if not self.credentials or self.credentials.invalid:
			flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
			flow.user_agent = APPLICATION_NAME
			if flags:
				self.credentials = tools.run_flow(flow, store, flags)
			else: # Needed only for compatibility with Python 2.6
				self.credentials = tools.run(flow, store)
			print('Storing credentials to ' + credential_path)
		http = self.credentials.authorize(httplib2.Http())
		self.service = discovery.build('calendar', 'v3', http=http)

	def createEvent(self, entry):
		
		createdEvent = self.service.events().quickAdd(calendarId='primary',text=entry).execute()
		if len(createdEvent['id']) > 0:
			return createdEvent
		else:
			return -1
