import re

def email_sender(file_name):
    with open(file_name) as file:
        email_content = file.read()
    pattern = r"From:.*<([^>]+)>"
    sender = re.search(pattern, email_content)
    return sender.group(1)

def email_recipient(file_name):
    with open(file_name) as file:
        email_content = file.read()
    pattern = r"To:.*<([^>]+)>"
    sender = re.search(pattern, email_content)
    return sender.group(1)

def email_subject(file_name):
    with open(file_name) as file:
        email_content = file.read()
    pattern = r"Subject: (.*)"
    sender = re.search(pattern, email_content)
    return sender.group(1)

def email_body(file_name):
    with open(file_name) as file:
        email_content = file.read()
    pattern = r"(\r?\n\r?\n)(.*)"
    sender = re.search(pattern, email_content, re.DOTALL)
    return sender.group(2)



email_file = 'email.txt'
#print(email_sender(email_file))
#print(email_recipient(email_file))
#print(email_subject(email_file))


