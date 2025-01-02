class C():
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        count = 0
        for x, y in self.coordinates:
            if x > 0 and y > 0:
                count += 1
        return count >= n
    
def main():
    object1 = C([[2,3],[1,8],[-6,4],[3,-7]])
    print(object1.m(2))
    print(object1.m(3))

if __name__ == "__main__":
    main()