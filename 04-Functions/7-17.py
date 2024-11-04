def f(sentence):
    sentence_no_spaces = sentence.replace(" ","")
    return sentence_no_spaces

if __name__ == "__main__":
    print(f("A programming language is a system of notation for writing computer programs"))