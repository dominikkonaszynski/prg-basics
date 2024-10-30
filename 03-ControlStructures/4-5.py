###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    code = ord("T")
    # add one to the character's code
    added = code + 1
    # replace new character code with its
    # corresponding character (use chr())
    
    # add encrypted character to encrypted text
    ...

print(f'{plain_text}...')
print(f'{encrypted_text}...')