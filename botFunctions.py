import imaplib
import email
import re
from keys import *

def led_strip_on():
	print("led string is on")
def led_strip_off():
	print("led strip off")

def availableCommands(command):
	commands = ["led strip on", "led strip off"]
	functions = [led_strip_on, led_strip_off]
	try:
		index = commands.index(command)
		functions[index]()
	except ValueError:
		#send back an email(;)
		pass

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

		if(mSender == master):
			availableCommands(cleaned)
		
	except IndexError:
		pass
		print("nope")
		
		#mail.close()
		#mail.logout()
