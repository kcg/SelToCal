# -*- coding: utf-8 -*-

import os
from GC import GoogleCalendar
from datetime import datetime

# Get selected text using 'xsel' (http://www.vergenet.net/~conrad/software/xsel/)
def getselection():
	selection = os.popen('xsel').read()
	return selection

# Communicate success or failure via 'notify-send' (part of libnotify-bin)
def notification(title, message):
    os.popen('notify-send -i '+os.path.dirname(os.path.abspath(__file__))+'/icon_48.png "'+title+'" "'+message+'"')
    return

#Get selection
calendarentry = getselection()

#Open google calendar and create new event
gc = GoogleCalendar()
event = gc.createEvent(entry=calendarentry)
if event == -1:
	notification("Failed!", "Could not create calendar entry.\nCheck settings.")
else:
	date = datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%SZ')
	notification("Calendar entry created", date.strftime('%a %d %b %Y, %H:%M')+"\n"+event['summary'])
