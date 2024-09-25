import mysql.connector as MC
Connection=MC.connect(host=“localhost”,user="root",passwd="united",database="library")
Cursor=Connection.cursor()
Continue="yes"
while Continue=="yes":
    User_ID=input("Enter the user name:")   #Log in
    PASSWD=input("Enter the password:")
    if User_ID=="Librarian" and PASSWD=="*****":
        #Displaying operations
        print("Press 1 to add record")
        print("Press 2 to get list of books given author")
        print("Press 3 to view the count of book")
        print("Press 4 to return book")       
        print("Press 5 to view not returned books (fine)")
        print("Press 6 to exit")
        choice=int(input("Enter what you want to do:"))
        if choice==1:   #To add the record
            Book_Name=input("Enter the book name:")
            Book_ID=input("Enter the book id:")
            Author=input("Enter the author name:")
            Student_Name=input("Enter the student name:")
            Date=input("Enter the return date:")      
            Cost=int(input("Enter the cost of book:"))
            Number_of_Copy=int(input("Enter the number of copy:"))
            Returned="NO"
            Record="Insert into books  values (‘{}’,’{}’,’{}’,’{}’,’{}’,{}{},’{}’)”.format(Book_Name,Book_ID,Author,Student_Name,Date,Cost, Number_of_Copy,Returned)
            Cursor.execute(Record)
            Connection.commit()
            print("Record is succesfully added")
        if choice==2:     #To get the list of books given author
            Author_Name=input("Enter the author name:")
            A="select * from books "
            Cursor.execute(A)
            Data=Cursor.fetchall()
            print("Books of ",Author_Name,"are:")
            for i in Data:
                if i[2]==Author_Name:
                    print(i[0])
        if choice==3:    #To find the number of copies of the book
            Book_Name=input("Enter the name of the book:")
            Cursor.execute("select * from books")
            List=Cursor.fetchall()
            for i in List:
                if i[0]== Book_Name:
                    print("Number of copy of ",Book_Name,"is",i[6])
        if choice==4:     #To return book
            Name=input("enter the name of the book id:")
            Return="update books set returned='{}' where book_id = '{}'".format("YES",Name)
            Cursor.execute(Return)
            Connection.commit()
            print("The Book is succesfully returned")
        if choice==5:    #Detils of the book not returned
            Cursor.execute("Select * from books")
            Data=Cursor.fetchall()
            print("Details of the books not returned:")
            for i in Data:
                if i[7]=="NO":
                    print(i)
        if choice==6:    #To exit
            print("Thank You!!!")
            break               
    else:
        if User_ID!="Librarian":
            print("Enter the correct user id")
        else:
            print("Recheck the password”)
