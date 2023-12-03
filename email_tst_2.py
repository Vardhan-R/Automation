import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = "vrdhnr@gmail.com"
password = "scfvdekkakvkyela"
# use your email provider's IMAP server, you can look for your provider's IMAP server on Google
# or check this page: https://www.systoolsgroup.com/imap/
# for office 365, it's this:
imap_server = "imap.gmail.com"

def clean(text):
	# clean text for creating a folder
	return "".join(c if c.isalnum() else "_" for c in text)

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL(imap_server)
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 1
# total number of emails
messages = int(messages[0])

for i in range(messages, messages - N, -1):
	# fetch the email message by ID
	res, msg = imap.fetch(str(i), "(RFC822)")
	for response in msg:
		if isinstance(response, tuple):
			# parse a bytes email into a message object
			msg = email.message_from_bytes(response[1])
			# decode the email subject
			subject, encoding = decode_header(msg["Subject"])[0]
			if isinstance(subject, bytes):
				# if it's bytes, decode to str
				subject = subject.decode(encoding)
			# decode email sender
			From, encoding = decode_header(msg.get("From"))[0]
			if isinstance(From, bytes):
				From = From.decode(encoding)
			print("Subject:", subject)
			print("From:", From)

			# extract content type of email
			content_type = msg.get_content_type()

			# get the email body
			body = msg.get_payload(decode=True)

			if content_type == "text/plain":
				# print only text email parts
				print("".join(body.decode("utf-8").split("\n")[2:]))

			print("=" * 100)

# close the connection and logout
imap.close()
imap.logout()