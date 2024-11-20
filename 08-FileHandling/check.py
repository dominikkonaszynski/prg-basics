import emails

# Define the email file path
email_file = 'email.txt'

# Fetch and print the sender, recipient, subject, and body of the email
print(f"Sender: {emails.email_sender(email_file)}")
print(f"Recipient: {emails.email_recipient(email_file)}")
print(f"Subject: {emails.email_subject(email_file)}")
print(f"Body: {emails.email_body(email_file)}")
