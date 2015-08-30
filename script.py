import glib
import dbus
import sqlite3
from dbus.mainloop.glib import DBusGMainLoop

conn = None

def log_message(name, body):

    #If group chat, get just peron's name
    if " to " in name:
        name = name.split(" to ")[0]

    #Don't log 'sent a photo'
    if body == name + " sent a photo.":
        return

    c = conn.cursor()
    c.execute('insert into messages(name, message) VALUES (?, ?)', (name, body))
    print "Logged message from " + name + ': ' + body

def get_notifications(bus, message):
  keys = ["app_name", "replaces_id", "app_icon", "summary",
          "body", "actions", "hints", "expire_timeout"]
  args = message.get_args_list()
  if len(args) == 8:
    notification = dict([(keys[i], args[i]) for i in range(8)])

    if(notification["app_name"] == "Messenger"):
      log_message(str(notification["summary"]), str(notification["body"]))

def init_database():
    global conn

    #Connect to DB
    conn = sqlite3.connect('db.sqlite', isolation_level=None)
    c = conn.cursor()
    c.execute('create table if not exists messages(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name text, message text, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL )')
    c.close()

loop = DBusGMainLoop(set_as_default=True)
session_bus = dbus.SessionBus()
session_bus.add_match_string("type='method_call',interface='org.freedesktop.Notifications',member='Notify',eavesdrop=true")
session_bus.add_message_filter(get_notifications)

print 'Connecting to DB'
init_database()

print 'Listening for messages...'
glib.MainLoop().run()
