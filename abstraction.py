# libarary book,audiobook,dvdbook,catalog
# Admin

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    @abstractmethod
    def locate(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, genre, page):
        super().__init__(title, genre)
        self.page = page

    def locate(self):
        return f"{self.title} kitoblar bo'limida joylashgan"


class AudioBook(LibraryItem):
    def __init__(self, title, genre, mp3):
        super().__init__(title, genre)
        self.mp3 = mp3

    def locate(self):
        return f"{self.title} audio bo'limida joylashgan"



class DVDBook(LibraryItem):
    def __init__(self, title, genre, mp4):
        super().__init__(title, genre)
        self.mp4 = mp4

    def locate(self):
        return f"{self.title} dvd  bo'limida joylashgan"

class Catalog:
    def __init__(self):
        self.books=[]


    def add(self,item):
        self.books.append(item)


    def view_book(self):
        items=[book.title for book in self.books]
        print("Jami kitoblar idsini tanlang")
        for i,e in enumerate(items,start=1):
            print(i,e)


    def find_book(self,id):
        for i,e in enumerate(self.books,start=1):
            if id!=i:
                continue

            return e.locate()




    # def search_book(self,search):
    #     items=[book.locate() for book in self.books]
    #     print(item)

cat=Catalog()
while True:
    print("""
    1 add book
    2 audio book
    3 dvd book
    4 view 
    5 exit
    """)
    user=input('son tanlang')
    if user=='1':
        title=input('kitobni nomini yozing:')
        genre=input(f'{title}ni janrini yozing:')
        page=input(f"{title} sahifalar soni nechta:")
        item=Book(title,genre,page)
        print(item.locate())
        cat.add(item)
    elif user=='2':
        title=input('kitobni nomini yozing:')
        genre=input(f'{title}ni janrini yozing:')
        mp3=input(f"{title} time qancha:")
        item=AudioBook(title,genre,mp3)
        print(item.locate())
        cat.add(item)

    elif user == '3':
        title = input('kitobni nomini yozing:')
        genre = input(f'{title}ni janrini yozing:')
        mp4 = input(f"{title} video tiniqligi qanday:")
        item = DVDBook(title, genre, mp4)
        print(item.locate())
        cat.add(item)
    elif user=='4':
        print(cat.view_book())
        user_son=int(input('idni tanlang:'))
        print(cat.find_book(user_son))
    else:
        break



