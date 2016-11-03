# ![logo][logo] SelToCal 
Small linux program to turn any selected text directly into a Google Calendar Event
[logo]: https://github.com/kcg/SelToCal/blob/master/icon_48.png "Logo"

###Example:
Someone writes you an email or some other message including *"Hey, let's meet next Friday at 2pm in Cafe Bellevue"*.

You can directly select the bit *next Friday at 2pm in Cafe Bellevu*, hit the key-short-cut for SelToCal and the event will be saved into your Google calendar

###Dependencies:
- Google Calendar (SelToCal uses the Google API and the QuickAdd function)
- Python 2.7 (probably other versions are fine)
- xsel (for the selection)
- notify-send (for desktop notifications)
