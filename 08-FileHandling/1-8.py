def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')

word_count = 0
for line in file_content.splitlines():
   words = line.split()
   word_count += len(words)

print('Total words:', word_count)