# MessengerListen

What?
=======

On Ubuntu or any other Linux distribution/setup that uses glib's LibNotify notification system,
listens for notifications from '[Messenger For Desktop](http://messengerfordesktop.com/)', a NW.js interface
to Facebook's Messenger.com, and captures any messages in a simplistic sqlite database. Good for logging
chats or doing text analysis on your friends etc.

How?
======

Dependencies
------------------
* Python 2.7 and glib/dbus/sqlite3 libraries.
* Linux based OS that uses glib libnotify & dbus. (Ubuntu for example)
* [Messenger For Desktop](http://messengerfordesktop.com/)

Getting it to work
--------------------
* Log in to Messenger for Desktop and make sure notifications are enabled. Minimize it or plop it in the background
* Run python script (`python script.py`)
* Wait for notifications to come through and be logged to `db.sqlite`. ([Sqliteman](http://sqliteman.yarpen.cz/) is a good GUI viewer)

Limitations
------------------------

* Doesn't log which conversation is which. This could probably be done for group chats.
* Only does first names, not last names. - Nothing can be done about this.
