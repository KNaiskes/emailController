import imaplib
import email
import re
from keys import *
from mqttFunctions import *

def led_strip_available_commands(command):
	states = ["on", "off"]
	colors = ["red","orange","dark_yellow","yellow","yellow2","green","pea","cyan","light_blue","sky_blue","blue","dark_blue","purple","violet","pink","white","flash","strobe","fade","smooth"]

	change_color_command = "led strip change color:"
	change_state_command = "led strip change state:"

	if command[0:23] == change_state_command:
		for s in states:
			if s in command:
				return s
	elif command[0:23] == change_color_command[0:23]:
		for c in colors:
			if c in command:
				return c
	else:
		return None


def readEmail(username, password):
	mail = imaplib.IMAP4_SSL("imap.gmail.com")
	mail.login(username, password)
	mail.select("inbox")

	try:
		result, data = mail.search(None, "UnSeen")
		
		emailIds = data[0]
		
		emailList = emailIds.split()
		latestEmail = emailList[-1]
		
		result, data = mail.fetch(latestEmail, "(RFC822)")
		
		rawEMail = data[0][1].decode("utf-8")
		
		msg = email.message_from_string(data[0][1].decode("utf-8"))
		
		emailMessage = email.message_from_string(rawEMail)
		
		if emailMessage.is_multipart():
			for part in emailMessage.get_payload():
				body = part.get_payload()
		else:
			body = emailMessage.get_payload()
		
		mbody = cleaner = re.compile("<.*?>")
		cleaned = re.sub(mbody, "", body)
		cleaned = cleaned.strip()

		mSender = (email.utils.parseaddr(emailMessage["From"])[1])

		if(mSender == master and led_strip_available_commands(cleaned) != None):
			send_Mqtt_message("ledStrip", led_strip_available_commands(cleaned))
		
	except IndexError:
		pass
		print("nope")
		
		#mail.close()
		#mail.logout()
