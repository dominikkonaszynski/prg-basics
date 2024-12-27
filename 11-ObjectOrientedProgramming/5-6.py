class Bank():
    def __init__(self, bank_account_no):
        self.balance = 0
        self.bank_account_no = str(bank_account_no)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account.")

    def display(self):
        formatted_account_no = self.bank_account_no[:2] + ' ' + ' '.join([self.bank_account_no[i:i+4] for i in range(2, len(self.bank_account_no), 4)])
        print(f"Bank Account No: {formatted_account_no}\n Balance: PLN {self.balance}")
    
def main():
    account1 = Bank(12345655559090111100007722)
    account1.display()
    account1.deposit(25.30)
    account1.display()
    account1.withdraw(31.70)
    account1.display()
    account1.withdraw(14)
    account1.display()

if __name__ == "__main__":
    main()