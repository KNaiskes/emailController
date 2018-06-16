from keys import *
from readEmail import *
from time import sleep

led_strip = Reademail(username, passw, master)

while True:
	led_strip.readCommands()
	sleep(5)
