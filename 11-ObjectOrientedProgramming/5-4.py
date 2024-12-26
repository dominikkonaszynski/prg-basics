class E_Book():
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author 
        self.number_of_pages = number_of_pages
        self.current_page = 1
        self.is_opened = False

    def open(self):
        self.is_opened = True

    def close(self):
        self.is_opened = False

    def next_page(self):
        if self.is_opened:
            if self.current_page < self.number_of_pages:
                self.current_page +=1
            else:
                print("You are already on last page!")
        else:
            print("Book is closed. Open it first")

    def previous_page(self):
        if self.is_opened:
            if self.current_page >= 2:
                self.current_page -= 1
            else:
                print("You are already on first page!")
        else:
            print("Book is closed. Open it first")
    def book_status(self):
        if self.is_opened:
            print(f'Book called "{self.title}", written by {self.author}. It has {self.number_of_pages} pages. You are currently on page {self.current_page}')
        else:
            print("The book is closed, status can't be shown.")

def main():
    book1 = E_Book("Wiedźmin", "Andrzej Sapkowski", 5)
    book1.open()
    book1.book_status()
    book1.next_page()
    book1.next_page()
    book1.next_page()
    book1.next_page()
    book1.book_status()
    book1.next_page()

if __name__ == "__main__":
    main()