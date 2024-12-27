class Statistics():
    def __init__(self):
        self.numbers = []

    def add(self, added_number):
        self.numbers.append(added_number)
        print(f"Added {added_number}")
    
    def remove(self, removed_number):
        if removed_number in self.numbers:
            self.numbers.remove(removed_number)
            print(f"Removed {removed_number}")
        else:
            print("Number is not on the list")

    def display(self):
        print(f"The numbers are: {', '.join(map(str, self.numbers))}")

    def greatest(self):
        self.greatest_number = max(self.numbers)
        print(f"The greatest number of the list is: {self.greatest_number}")

    def smallest(self):
        self.smallest_number = min(self.numbers)
        print(f"The smallest number of the list is: {self.smallest_number}")

    def arithmetic_mean(self):
        self.arithmetic_mean = sum(self.numbers)/len(self.numbers)
        print(f"The arithmetic mean of the numbers in the list is: {self.arithmetic_mean}")

    def median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        middle_index = n // 2
        if n % 2 == 1:
            self.median_value = sorted_numbers[middle_index]
        else:
            self.median_value = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
        print(f"The median of the numbers in the list is: {self.median_value}")

    def summary(self):
        print(f"The maximum number is {self.greatest_number}.\nThe minimum number is {self.smallest_number}.\nThe arithmetic mean is {self.arithmetic_mean}.\nThe median is {self.median_value}.")

def main():
    numbers1 = Statistics()
    numbers1.add(12)
    numbers1.add(37)
    numbers1.add(6)
    numbers1.add(9)
    numbers1.add(17)
    numbers1.add(15)
    numbers1.display()
    numbers1.greatest()
    numbers1.smallest()
    numbers1.arithmetic_mean()
    numbers1.median()
    numbers1.summary()

if __name__ == "__main__":
    main()