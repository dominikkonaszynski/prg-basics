import re
text_file = 'data.txt'

def f(first_letter,last_letter):
    count = 0
    with open(text_file, encoding='utf-8') as file:
        text_content = file.read()
        pattern = r'\b' + re.escape(first_letter) + r'\w*' + re.escape(last_letter) + r'\b'
        matches = re.findall(pattern, text_content)
        count = (len(matches))
    return count

if __name__ == "__main__":
    print(f("w", "d"))
    print(f("a", "d"))