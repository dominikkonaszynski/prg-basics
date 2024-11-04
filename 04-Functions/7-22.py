def f(password):
    if len(password) >=6 and len(password) == len(set(password)):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("A2water3"))
