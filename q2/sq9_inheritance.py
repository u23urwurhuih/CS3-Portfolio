class Publication:
    def __init__(self, title, author):
        self.t = title
        self.a = author

    def get_title(self):
        return self.t
    def get_author(self):
        return self.a
    def set_title(self, title1):
        self.t = title1
    def set_author(self, author1):
        self.a = author1
    def display_info(self):
        print(f"Title: {self.t}")
        print(f"Author: {self.a}")


class Book:
    def __init__(self, title, author, number_pages):
        self.t = title
        self.a = author
        self.p = number_pages

    def get_number_of_pages(self):
        return f"Number of pages: {self.p}"
    def set_number_of_pages(self, number_pages1):
        if number_pages1 > 0:
            self.p = number_pages1
    def display_info(self):
        print(f"Title: {self.t}")
        print(f"Author: {self.a}")

class Magazine:
    def __init__(self, title, author, issue_number):
        self.t = title
        self.a = author
        self.i = issue_number

    def get_issue_number(self):
        return f"Issue Number: {self.i}"
    def set_issue_number(self, issue_number1):
        self.i = issue_number1
    def display_info(self):
        print(f"Title: {self.t}")
        print(f"Author: {self.a}")

p = Publication("Journal of Samson Westgray", "Westgray, S.")
b = Book("How to get poor", "Keith, P. & Famon, R.", 130)
m = Magazine("The Dress", "Rezoni, S.", 303)

print("Publication Information:")
p.display_info()

print("\nBook Information:")
b.set_number_of_pages(-12)
b.display_info()
print(b.get_number_of_pages())

print("\nMagazine Information:")
m.display_info()
print(m.get_issue_number())
