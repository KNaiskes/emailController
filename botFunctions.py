import imaplib
import email
import re
from keys import *

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
			#TODO: check command if exits
			# and if exists run it


		
		print("Checked")
	except IndexError:
		pass
		print("nope")
		
		#mail.close()
		#mail.logout()
