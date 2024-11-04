def f(x,y):
    count = 0
    for i in range (x,y):
        if i < 0 and i%2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    print(f(-1,11))
