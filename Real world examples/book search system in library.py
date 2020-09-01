# Enter your code here. Read input from STDIN. Print output to STDOUT
class Book:
    def __init__(self,bookId,bookName,bookTechnology,bookPrice,authorname):
        self.bookId=bookId
        self.bookName=bookName
        self.bookTechnology=bookTechnology
        self.bookPrice=bookPrice
        self.authorname=authorname
    
class BookStore:
    def __init__(self,bookdb,bookStoreName):
        self.bookdb=bookdb
        self.bookStoreName=bookStoreName
    
    def searchByName(self,bookName):
        l=[]
        for book in bookdb.values():
            if bookName == book.bookName:
                l.extend([book.bookId,book.bookName,book.bookTechnology,book.bookPrice,book.authorname])
                
        if l is None:
            return None
        else:
            return l
        
    def calculatePriceByTechnology(self,bookTechnology):
        dis=10
        price=0
        for book in bookdb.values():
            if bookTechnology == book.bookTechnology:
                price+=book.bookPrice
        price=price-((price*dis)/100)
        
        if price>0:
            return price  
        else:
            price='0.0'
            return price


n=int(input())
bookdb=dict()
for i in range(1,n+1):
    idf=int(input())
    name=input()
    tech=input()
    bprice=int(input())
    aname=input()
    obj=Book(idf,name,tech,bprice,aname)
    bookdb[i]=obj

sname=input()
stech=input()
bs=BookStore(bookdb,bookStoreName="A")
first=bs.searchByName(sname)
sec=bs.calculatePriceByTechnology(stech)

if first is None:
    print("No Book Exists")
else:
    for it in first:
        print(it)
print(sec)
    
