import imaplib
import email
from email.header import decode_header


# # Account credentials
username = "ADDRESS@EMAIL.com"
password = "PASSWORD"

# # Create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.EMAIL.com") # find addresses @ https://www.systoolsgroup.com/imap/
# # Authenticate
imap.login(username, password)

# # Select the mailbox you want to delete from
imap.select("INBOX")

# # Search for specific mails by sender
status, messages = imap.search(None, 'FROM "TARGETADDRESS@EMAIL.com"')

# Search for mails by subject
# status, messages = imap.search(None, 'SUBJECT"Thanks for Subscribing to our Newsletter !"')

# # Search for mails by after a date
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')

# # Search for mails before a date
# status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')

# to grab all mail
# status, messages = imap.search(None, "ALL")

# # Connver the messages to a list of email IDs
messages = messages[0].split(b' ')

# # Iterate over targeted messages and mark them as deleted
for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")

    # Optional for loop to print emails as they are deleted, delete for faster speeds.
    for responce in msg:
        if isinstance(responce, tuple):
            msg = email.message_from_bytes(responce[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(object, bytes):
                # If it's a bytes type, decode to str
                subject = subject.decode()
            print("Deleting: ", subject)
            
    # Mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")
    
# # Finally use the expunge method that permanently removes mails that are marked as deleted
imap.expunge()

# # Close the mailbox
imap.close()

# # logout from the account
imap.logout()