from datetime import date


class Citizen:
    def __init__(self,name,author,price,published):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_published = published
       
    def add_citizen(self):
        print("Name: "+self.book_name)
        print("author: "+str(self.book_author))
        print("price: "+self.book_price)
        print("publlished: "+self.book_published)
        print("book Added")
        
    def year_since_published(self):
        todays_date=date.today()
        current_year=todays_date.year
        number_of_years=current_year-int(self.book_published)
        print("this book way published "+str(number_of_years)+" years ago")
       
       
book1 = Citizen("diary of a wimpy kid","jeff kinney", "700","2017")
book1.add_citizen()
book1.year_since_published()


book2 = Citizen("hary potter","jk rowling","1927","1997")
book2.add_citizen()
book2.year_since_published()