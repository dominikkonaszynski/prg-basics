def f(sentence):
    count = 0
    letter = 'e'
    for char in sentence:
        if char in letter:
            count += 1
    return count

if __name__ == "__main__":
    print(f("You never get a second chance to make a first impression"))