from tabulate import tabulate
from datetime import date
import mysql.connector
con = mysql.connector.connect(host = 'localhost',password = 'khushi1205',user = 'root',database = 'elib')
curs = con.cursor()

def main():
         print('  WELCOME TO OUR E-LIBRARY =)')
         print('        ---------------')
         print('            M E N U    ')
         print('        ---------------')
         print('        1. User Login')
         print('        2. User Signin')
         print('        3. Admin Login')
         print(" ")
         choice = int(input("Enter your choice: "))
         if choice == 1:
                  user_login()
         elif choice == 2:
                  user_signin()
         elif choice == 3:
                  admin_login()
         else:
                  print(" ")
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  print(" ")
                  main()
         con.close()
         
def down_books():
         data = []
         Name = ur_name
         Email = ur_mail 
         curs.execute('select * from user_books where (Name,Email)=(%s,%s)',(Name,Email))
         data = curs.fetchall()
         con.commit()
         if data:
                  print("------------------------------------")
                  print(Name,"your Downloaded Books are:")
                  curs.execute('select Downloaded_books from user_books where (Name,Email)=(%s,%s)',(Name,Email))
                  ab = curs.fetchall()
                  tab = ['Your Downloaded books']
                  print(tabulate(ab, headers = tab, tablefmt = 'grid'))
                  
         else:
                  print("    ---------------------------")
                  print("        NO DOWNLOADED BOOKS")
                  print("    ---------------------------")

def todown_fb():
        data = []
        print("    --------BOOKS AVAILABLE ARE--------") 
        curs.execute('select Bname,Bauthor from fiction_books')
        data = curs.fetchall()
        tab = ['Book Name','Book Author']
        print(tabulate(data, headers = tab, tablefmt = 'grid'))
        Bname = input("Enter name of book you want to download: ")
        Bauthor = input("Enter book's author: ") 
        curs.execute('select * from fiction_books where (Bname,Bauthor) = (%s,%s)',(Bname,Bauthor))
        ch = curs.fetchall()
        con.commit()
        if ch:
                  print(" ")
                  print("**Copy the URL given below and paste it in search engine")
                  print("URL for",Bname,"is:")
                  curs.execute('select download_link from fiction_books where (Bname,Bauthor)=(%s,%s)',(Bname,Bauthor))
                  data = curs.fetchall()
                  tab = ['URL for your desired book']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  print(" ")
                  Name = ur_name
                  Email = ur_mail
                  Genre = 'Fiction'
                  curs.execute('INSERT INTO user_books (Name,Email,Downloaded_books,Genre)values(%s,%s,%s,%s)',(Name,Email,Bname,Genre))
                  con.commit()
                  ag = input("Do you want to download another fiction book(yes or no)? ")
                  if ag == 'yes':
                           todown_fb() 
        else:
                  print("    ----INVALID CREDENTIALS----")
                  print("            TRY AGAIN")
                  print("    ---------------------------")
                  print(" ")
                  todown_fb()
                          
def todown_abb():
        print("    --------BOOKS AVAILABLE ARE--------")
        curs.execute('select Bname,Bauthor from autob_bio')
        data = curs.fetchall()
        tab = ['Book Name','Book Author']
        print(tabulate(data, headers = tab, tablefmt = 'grid'))
        Bname = input("Enter name of book you want to download: ")
        Bauthor = input("Enter book's author: ")
        curs.execute('select * from autob_bio where (Bname,Bauthor) = (%s,%s)',(Bname,Bauthor))
        ch = curs.fetchall()
        con.commit()
        if ch:
                  print(" ")
                  print("**Copy the URL given below and paste it in search engine")
                  print("URL for",Bname,"is:")
                  curs.execute('select download_link from autob_bio where (Bname,Bauthor)=(%s,%s)',(Bname,Bauthor))
                  data = curs.fetchall()
                  tab = ['URL for your desired book']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  print(" ")
                  Name = ur_name
                  Email = ur_mail
                  Genre = 'Autobiography/Biography'
                  curs.execute('INSERT INTO user_books (Name,Email,Downloaded_books,Genre)values(%s,%s,%s,%s)',(Name,Email,Bname,Genre))
                  con.commit()
                  ag = input("Do you want to download another autobiography/biography book(yes or no)? ")
                  if ag == 'yes':
                           todown_abb() 
        else:
                  print("    ----INVALID CREDENTIALS----")
                  print("            TRY AGAIN")
                  print("    ---------------------------")
                  print(" ")
                  todown_abb() 
                          
def todown_ct():
        print("    --------BOOKS AVAILABLE ARE--------")
        curs.execute('select Bname,Bauthor from crime_thrillers')
        data = curs.fetchall()
        tab = ['Book Name','Book Author']
        print(tabulate(data, headers = tab, tablefmt = 'grid'))
        Bname = input("Enter name of book you want to download: ")
        Bauthor = input("Enter book's author: ") 
        curs.execute('select * from crime_thrillers where (Bname,Bauthor) = (%s,%s)',(Bname,Bauthor))
        ch = curs.fetchall()
        con.commit()
        if ch:
                  print(" ")
                  print("**Copy the URL given below and paste it in search engine")
                  print("URL for",Bname,"is:")
                  curs.execute('select download_link from crime_thrillers where (Bname,Bauthor)=(%s,%s)',(Bname,Bauthor))
                  data = curs.fetchall()
                  tab = ['URL for your desired book']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  print(" ")
                  Name = ur_name
                  Email = ur_mail
                  Genre = 'Crime Thrillers'
                  curs.execute('INSERT INTO user_books (Name,Email,Downloaded_books,Genre)values(%s,%s,%s,%s)',(Name,Email,Bname,Genre))
                  con.commit()
                  ag = input("Do you want to download another crime thriller book(yes or no)? ")
                  if ag == 'yes':
                           todown_ct()
        else:
                  print("    ----INVALID CREDENTIALS----")
                  print("            TRY AGAIN")
                  print("    ---------------------------")
                  print(" ")
                  todown_ct() 
                          
def todown_hb():
        print("    --------BOOKS AVAILABLE ARE--------")
        curs.execute('select Bname,Bauthor from historical_books')
        data = curs.fetchall()
        tab = ['Book Name','Book Author']
        print(tabulate(data, headers = tab, tablefmt = 'grid'))
        Bname = input("Enter name of book you want to download: ")
        Bauthor = input("Enter book's author: ")
        curs.execute('select * from historical_books where (Bname,Bauthor) = (%s,%s)',(Bname,Bauthor))
        ch = curs.fetchall()
        con.commit()
        if ch:
                  print(" ")
                  print("**Copy the URL given below and paste it in search engine")
                  print("URL for",Bname,"is:") 
                  curs.execute('select download_link from historical_books where (Bname,Bauthor)=(%s,%s)',(Bname,Bauthor))
                  data = curs.fetchall()
                  tab = ['URL for your desired book']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  print(" ")
                  Name = ur_name
                  Email = ur_mail
                  Genre = 'History'
                  curs.execute('INSERT INTO user_books (Name,Email,Downloaded_books,Genre)values(%s,%s,%s,%s)',(Name,Email,Bname,Genre))
                  con.commit()
                  ag = input("Do you want to download another historical book(yes or no)? ")
                  if ag == 'yes':
                           todown_hb()
        else:
                  print("    ----INVALID CREDENTIALS----")
                  print("            TRY AGAIN")
                  print("    ---------------------------")
                  print(" ")
                  todown_hb()  
                          
def todown_shb():
        print("    --------BOOKS AVAILABLE ARE--------")
        curs.execute('select Bname,Bauthor from self_help')
        data = curs.fetchall()
        tab = ['Book Name','Book Author']
        print(tabulate(data, headers = tab, tablefmt = 'grid'))
        Bname = input("Enter name of book you want to download: ")
        Bauthor = input("Enter book's author: ")
        curs.execute('select * from self_help where (Bname,Bauthor) = (%s,%s)',(Bname,Bauthor))
        ch = curs.fetchall()
        con.commit()
        if ch:
                  print(" ")
                  print("**Copy the URL given below and paste it in search engine")
                  print("URL for",Bname,"is:")
                  curs.execute('select download_link from self_help where (Bname,Bauthor)=(%s,%s)',(Bname,Bauthor))
                  data = curs.fetchall()
                  tab = ['URL for your desired book']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  print(" ")
                  Name = ur_name
                  Email = ur_mail
                  Genre = 'Self Help'
                  curs.execute('INSERT INTO user_books (Name,Email,Downloaded_books,Genre)values(%s,%s,%s,%s)',(Name,Email,Bname,Genre))
                  con.commit()
                  ag = input("Do you want to download another self-help book(yes or no)? ")
                  if ag == 'yes':
                           todown_shb() 
        else:
                  print("    ----INVALID CREDENTIALS----")
                  print("            TRY AGAIN")
                  print("    ---------------------------")
                  print(" ")
                  todown_shb()

def review():
         Bname = input("Enter the name of the book: ")
         Email = ur_mail
         Review = input("Enter you review: ")
         Rating = float(input("Rate the book (out of 5): "))
         curs.execute('INSERT into reviews (Bname,Email,Review,Ratings)values(%s,%s,%s,%s)',(Bname,Email,Review,Rating))
         con.commit()
         print("    ============================")
         print("    THANK YOU FOR YOUR REVIEW!!!")
         print("    ============================")
         ad = input("Do you want to share your review for another book(yes or no)? ")
         if ad == 'yes':
                  print(" ")
                  review()

def todown_books():
         print('1. Fiction books')
         print('2. Autobiography/Biography')
         print('3. Crime Thrillers')
         print('4. Historical books')
         print('5. Self-help books')
         print(" ")
         gen = int(input("Enter the no. of respective genre whose book you want to download: "))
         confirm = input("Do you want to continue with chosen genre(yes or no) or want to choose another genre?: ")
         if confirm == 'yes':
                  if gen == 1:
                           todown_fb()
                  elif gen == 2:
                           todown_abb()
                  elif gen == 3:
                           todown_ct()
                  elif gen == 4:
                           todown_hb()
                  else:
                           todown_shb()
                  print(" ") 
                  an = input("Do you want to download book from another genre(yes or no)? ")
                  if an == 'yes':
                           todown_books()
                  print(" ")
                  rev = input("Would you like to share a review for your any previously read book(yes or no)? ")
                  if rev == 'yes':
                           print(" ")
                           review()
         else:
                  todown_books()

def update_user():
         print("   1. Name")
         print("   2. Age")
         print("   3. Gender")
         print("   4. Country")
         print("   5. Contact")
         print("   6. Email")
         print("   7. Password")
         print(" ")
         edit = int(input("Enter the no. of respective detail you want to edit: "))
         if edit == 1:
                  Name = input("Enter new Name: ")
                  Password = ur_pass
                  curs.execute("UPDATE users SET Name = %s WHERE Password = %s",(Name,Password))
                  con.commit()
                  print("   ---------------------------")
                  print("   NAME SUCCESSFULLY CHANGED!!")
                  print("   ---------------------------")
         elif edit == 2:
                  Age = int(input("Enter new Age: "))
                  Password = ur_pass 
                  curs.execute( "UPDATE users SET Age = %s WHERE Password = %s",(Age,Password))
                  con.commit()
                  print("   --------------------------")
                  print("   AGE SUCCESSFULLY CHANGED!!")
                  print("   --------------------------")
         elif edit == 3:
                  Gender = input("Enter new Gender: ")
                  Password = input("Enter your registered password: ")
                  curs.execute("UPDATE users SET Gender = %s WHERE Password = %s",(Gender,Password))
                  con.commit()
                  print("   -----------------------------")
                  print("   GENDER SUCCESSFULLY CHANGED!!")
                  print("   -----------------------------")
         elif edit == 4:
                  Country = input("Enter new Country: ")
                  Password = ur_pass 
                  curs.execute("UPDATE users SET Country = %s WHERE Password = %s",(Country,Password))
                  con.commit()
                  print("   ------------------------------")
                  print("   COUNTRY SUCCESSFULLY CHANGED!!")
                  print("   ------------------------------")
         elif edit == 5:
                  Contact = int(input("Enter new Contact: "))
                  Password = ur_pass
                  curs.execute("UPDATE users SET Contact = %s WHERE Password = %s",(Contact,Password))
                  con.commit()
                  print("   ------------------------------")
                  print("   CONTACT SUCCESSFULLY CHANGED!!")
                  print("   ------------------------------")
         elif edit == 6:
                  Email = input("Enter new Email: ")
                  Password = ur_pass
                  curs.execute("UPDATE users SET Email = %s WHERE Password = %s",(Email,Password))
                  con.commit()
                  print("   ----------------------------")
                  print("   EMAIL SUCCESSFULLY CHANGED!!")
                  print("   ----------------------------")
         elif edit == 7:
                  Password = input("Enter new Password: ")
                  Email = ur_mail
                  curs.execute("UPDATE users SET Password = %s WHERE Email = %s",(Password,Email))
                  con.commit()
                  print("   -------------------------------")
                  print("   PASSWORD SUCCESSFULLY CHANGED!!")
                  print("   -------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  update_user()
         inp = input("Do you want to edit another data(yes or no)? ")
         if inp == 'yes':
                  update_user()

def new_arr():
         print('1. Fiction books')
         print('2. Autobiography/Biography')
         print('3. Crime Thrillers')
         print('4. Historical books')
         print('5. Self-help books')
         print(" ")
         gen = int(input("Enter the no. of respective genre whose new arrivals you wanna see: "))
         if gen == 1:
                  curs.execute("select Bname from fiction_books where Date > '2022-02-06'")
                  data = curs.fetchall()
                  tab = ['New Arrivals in Fiction']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
         elif gen == 2:
                  curs.execute("select Bname from autob_bio where Date > '2022-02-06'")
                  data = curs.fetchall()
                  tab = ['New Arrivals in Autobiograhy/Biography']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
         elif gen == 3:
                  curs.execute("select Bname from crime_thrillers where Date > '2022-02-06'")
                  data = curs.fetchall()
                  tab = ['New Arrivals in Crime Thrillers']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
         elif gen == 4:
                  curs.execute("select Bname from historical_books where Date > '2022-02-06'")
                  data = curs.fetchall()
                  tab = ['New Arrivals in History']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
         elif gen == 5:
                  curs.execute("select Bname from self_help where Date > '2022-02-06'")
                  data = curs.fetchall()
                  tab = ['New Arrivals in Self Help']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
         else:
                  print("    ---INVALID CHOICE---")
                  print("         TRY AGAIN")
                  print("    --------------------")
         print(" ")
         bk = input("Do you want to check new arrivals of another genre(yes or no)? ")
         if bk == 'yes':
                  new_arr()

def rem_user():
         confo = input("Are you sure you want to delete your account(yes or no): ")
         if confo == 'yes':
                  Name = ur_name
                  Email = ur_mail
                  curs.execute('DELETE from users where (Name,Email)=(%s,%s)',(Name,Email))
                  con.commit()
                  print("    --------ACCOUNT DELETED!!--------")
         else:
                  user_menu()
         
def logout():
         exit

def user_menu():
         print(" ")
         print("        W E L C O M E")
         print("        -------------")
         print("           M E N U")
         print("        --------------")
         print("        1. My books")
         print("        2. Download new book")
         print("        3. Edit my profile")
         print("        4. New arrivals")
         print("        5. Delete account")
         print("        6. Logout")
         print(" ")
         choice = int(input("Enter you choice: "))
         if choice == 1:
                  down_books()
         elif choice == 2:
                  todown_books()
         elif choice == 3:
                  update_user()
         elif choice == 4:
                  new_arr()
         elif choice == 5:
                  rem_user()
         elif choice == 6:
                  logout()
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  user_menu()
         print(" ")
         bc = input("Do you want to go back to main menu(yes or no)? ")
         if bc == 'yes':
                  user_menu()

def user_login():
         ab = []
         Email = input("Enter your registered mail id: ")
         Password = input("Enter your password: ")
         curs.execute('select * from users where (Email,Password)=(%s,%s)',(Email,Password))
         ab = curs.fetchall()
         con.commit() 
         if ab:
                  global ur_name
                  ur_name = ab[0][0]
                  global ur_mail
                  ur_mail = ab[0][5]
                  global ur_pass
                  ur_pass = ab[0][6]
                  user_menu()
         else:
                  print("    Oops!!Wrong credentials")
                  print("          Try again")
                  print("---------------------------------")
                  print("Redirecting back to login page...")
                  print("---------------------------------")
                  user_login()
                  
def user_signin():
         Name = input("Enter your full name: ")
         Age = int(input("Enter you age in numericals: "))
         Gender = input("Enter your gender: ")
         Country = input("Enter the country you are from: ")
         Contact = int(input("Enter your contact number: "))
         Email = input("Enter you Email id: ")
         Password = input("Set a password: ")
         values = (Name,Age,Gender,Country,Contact,Email,Password) 
         curs.execute('INSERT INTO users(Name,Age,Gender,Country,Contact,Email,Password)VALUES(%s,%s,%s,%s,%s,%s,%s)',values)
         con.commit()
         print(" ")
         print(" CONGRATULATIONS!!SUCCESSFULLY REGISTERED :)")
         print("      ----------------------------")
         print("      Redirecting to login page...")
         print("      ----------------------------")
         user_login()

def add_fiction():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of book: ")
                  Bauthor = input("Enter book's author: ")
                  ISBN = int(input("Enter ISBN number of book: "))
                  download_link = input("Enter the URL for PDF of book: ")
                  Date = date.today()
                  values = (Bname,Bauthor,ISBN,download_link,Date)
                  curs.execute('INSERT INTO fiction_books(Bname,Bauthor,ISBN,download_link,Date)VALUES(%s,%s,%s,%s,%s)',values)
                  con.commit()
                  print(" ")
                  ch = input("Do you want to add more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------NEW BOOK(s) ADDED!!--------")
                  
def add_autob_bio():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of book: ")
                  Bauthor = input("Enter book's author: ")
                  ISBN = int(input("Enter ISBN number of book: "))
                  download_link = input("Enter the URL for PDF of book: ")
                  Date = date.today()
                  values = (Bname,Bauthor,ISBN,download_link,Date)
                  curs.execute('INSERT INTO autob_bio(Bname,Bauthor,ISBN,download_link,Date)VALUES(%s,%s,%s,%s,%s)',values)
                  con.commit()
                  print(" ")
                  ch = input("Do you want to add more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------NEW BOOK(s) ADDED!!--------")
                  
def add_ct():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of book: ")
                  Bauthor = input("Enter book's author: ")
                  ISBN = int(input("Enter ISBN number of book: "))
                  download_link = input("Enter the URL for PDF of book: ")
                  Date = date.today()
                  values = (Bname,Bauthor,ISBN,download_link,Date)
                  curs.execute('INSERT crime_thrillers(Bname,Bauthor,ISBN,download_link,Date)VALUES(%s,%s,%s,%s,%s)',values)
                  con.commit()
                  print(" ")
                  ch = input("Do you want to add more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------NEW BOOK(s) ADDED!!--------")
                  
def add_historical():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of book: ")
                  Bauthor = input("Enter book's author: ")
                  ISBN = int(input("Enter ISBN number of book: "))
                  download_link = input("Enter the URL for PDF of book: ")
                  Date = date.today()
                  values = (Bname,Bauthor,ISBN,download_link,Date)
                  curs.execute('INSERT INTO historical_books(Bname,Bauthor,ISBN,download_link,Date)VALUES(%s,%s,%s,%s,%s)',values)
                  con.commit()
                  print(" ")
                  ch = input("Do you want to add more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------NEW BOOK(s) ADDED!!--------")
                  
def add_selfh():
         ch = 'yes'
         while ch == 'yes' and 'y':
                  Bname = input("Enter name of book: ")
                  Bauthor = input("Enter book's author: ")
                  ISBN = int(input("Enter ISBN number of book: "))
                  download_link = input("Enter the URL for PDF of book: ")
                  Date = date.today()
                  values = (Bname,Bauthor,ISBN,download_link,Date)
                  curs.execute('INSERT INTO self_help(Bname,Bauthor,ISBN,download_link,Date)VALUES(%s,%s,%s,%s,%s)',values)
                  con.commit()
                  print(" ")
                  ch = input("Do you want to add more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------NEW BOOK(s) ADDED!!--------")

def add_books():
         print('1. Fiction book')
         print('2. Autobiography/Biography')
         print('3. Crime Thrillers')
         print('4. Historical')
         print('5. Self-help')
         print(" ")
         choice = int(input("Enter the number of respective genre whose book you want to add: "))
         if choice == 1:
                  add_fiction()
         elif choice == 2:
                  add_autob_bio()
         elif choice == 3:
                  add_ct()
         elif choice == 4:
                  add_historical()
         elif choice == 5:
                  add_selfh()
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  add_books()
         an = input("Do you want to add book of another genre(yes or no)? ")
         if an == 'yes':
                  add_books()

def rem_fiction():
         curs.execute('select Bname,Bauthor from fiction_books')
         data = curs.fetchall()
         tab = ['Bname','Bauthor','ISBN','Download Link']
         print(tabulate(data, headers = tab, tablefmt = 'grid'))
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of the book you want to remove: ")
                  Author = input("Enter book's Author: ") 
                  curs.execute('DELETE from fiction_books where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  con.commit()
                  print(" ")
                  ch = input("Do you want to remove more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------BOOK(s) DELETED!!--------")
         
def rem_autob_bio():
         curs.execute('select Bname,Bauthor from autob_bio')
         data = curs.fetchall()
         tab = ['Bname','Bauthor','ISBN','Download Link']
         print(tabulate(data, headers = tab, tablefmt = 'grid'))
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of the book you want to remove: ")
                  Author = input("Enter book's Author: ")
                  curs.execute('DELETE from autob_bio where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  con.commit()
                  print(" ")
                  ch = input("Do you want to remove more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------BOOK(s) DELETED!!--------")
         
def rem_ct():
         curs.execute('select Bname,Bauthor from crime_thrillers')
         data = curs.fetchall()
         tab = ['Bname','Bauthor','ISBN','Download Link']
         print(tabulate(data, headers = tab, tablefmt = 'grid'))
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of the book you want to remove: ")
                  Author = input("Enter book's Author: ")
                  curs.execute('DELETE from crime_thrillers where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  con.commit()
                  print(" ")
                  ch = input("Do you want to remove more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------BOOK(s) DELETED!!--------")
         
def rem_historical():
         curs.execute('select Bname,Bauthor from historical_books')
         data = curs.fetchall()
         tab = ['Bname','Bauthor','ISBN','Download Link']
         print(tabulate(data, headers = tab, tablefmt = 'grid'))
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of the book you want to remove: ")
                  Author = input("Enter book's Author: ")
                  curs.execute('DELETE from historical_books where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  con.commit()
                  print(" ")
                  ch = input("Do you want to remove more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------BOOK(s) DELETED!!--------")
         
def rem_selfh():
         curs.execute('select Bname,Bauthor from self_help')
         data = curs.fetchall()
         tab = ['Bname','Bauthor','ISBN','Download Link']
         print(tabulate(data, headers = tab, tablefmt = 'grid'))
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of the book you want to remove: ")
                  Author = input("Enter book's Author: ")
                  curs.execute('DELETE from self_help where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  con.commit()
                  print(" ")
                  ch = input("Do you want to remove more books from this genre? (yes or no)? ")
                  print(" ")
         print("    --------BOOK(s) DELETED!!--------")

def rem_books():
         print('1. Fiction book')
         print('2. Autobiography/Biography')
         print('3. Crime Thrillers')
         print('4. Historical')
         print('5. Self-help')
         print(" ")
         choice = int(input("Enter the number of respective genre whose book you want to remove: "))
         if choice == 1:
                  rem_fiction()
         elif choice == 2:
                  rem_autob_bio()
         elif choice == 3:
                  rem_ct()
         elif choice == 4:
                  rem_historical()
         elif choice == 5:
                  rem_selfh()
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  rem_books()
         an = input("Do you want to remove book from another genre(yes or no)? ")
         if an == 'yes':
                  rem_books()

def admin_signin():
         ch = 'yes'
         while ch == 'yes':
                  Name = input("Enter admin's name: ")
                  Designation = input("Enter admin's designation: ")
                  Age = int(input("Enter admin's age: "))
                  Gender = input("Enter admin's gender: ")
                  Address = input("Enter admin's address: ")
                  Contact = int(input("Enter admin's contact no.: "))
                  Email = input("Enter admin's mail id: ")
                  Password = input("Enter admin's password: ")
                  values = (Name,Designation,Age,Gender,Address,Contact,Email,Password)
                  curs.execute('INSERT INTO Admin(Name,Designation,Age,Gender,Address,Contact,Email,Password)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',values)
                  con.commit()
                  ch = input("Do you want to add another admin(yes or no)? ")
         print("    -----NEW ADMIN(s) ADDED SUCCESSFULLY!!-----")

def rem_admin():
         ch = 'yes'
         while ch == 'yes':
                  confo = input("Are you sure you want to remove the admin(yes or no)? ")
                  if confo == 'yes':
                           Name = input("Enter name of the admin you want to remove: ")
                           Designation = input("Enter admin's designation: ")
                           curs.execute('DELETE from admin where (Name,Designation)=(%s,%s)',(Name,Designation))
                           con.commit()
                           ch = input("Do you want to remove another admin? (yes or no)? ")
                  else:
                           admin_menu()
         print("    --------ADMIN(s) REMOVED!!--------")

def ret_fb():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of desired book: ")
                  Author = input("Enter book's author: ")
                  curs.execute('SELECT * from fiction_books where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  data = curs.fetchall()
                  tab = ['Book Name','Book Author','ISBN','Download Link']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  ch = input("Do you want details of another book of this genre? (yes or no)? ")
def ret_abb():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of desired book: ")
                  Author = input("Enter book's author: ")
                  curs.execute('SELECT * from autob_bio where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  data = curs.fetchall()
                  tab = ['Book Name','Book Author','ISBN','Download Link']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  ch = input("Do you want details of another book of this genre? (yes or no)? ")
def ret_ct():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of desired book: ")
                  Author = input("Enter book's author: ")
                  curs.execute('SELECT * from crime_thrillers where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  data = curs.fetchall()
                  tab = ['Book Name','Book Author','ISBN','Download Link']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  ch = input("Do you want details of another book of this genre? (yes or no)? ")
def ret_hb():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of desired book: ")
                  Author = input("Enter book's author: ")
                  curs.execute('SELECT * from historical_books where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  data = curs.fetchall()
                  tab = ['Book Name','Book Author','ISBN','Download Link']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  ch = input("Do you want details of another book of this genre? (yes or no)? ")
def ret_shb():
         ch = 'yes'
         while ch == 'yes':
                  Bname = input("Enter name of desired book: ")
                  Author = input("Enter book's author: ")
                  curs.execute('SELECT * from self_help where (Bname,Bauthor)=(%s,%s)',(Bname,Author))
                  data = curs.fetchall()
                  tab = ['Book Name','Book Author','ISBN','Download Link']
                  print(tabulate(data, headers = tab, tablefmt = 'grid'))
                  ch = input("Do you want details of another book of this genre? (yes or no)? ")

def ret_books():
         print('1. Fiction book')
         print('2. Autobiography/Biography')
         print('3. Crime Thrillers')
         print('4. Historical')
         print('5. Self-help')
         print(" ")
         choice = int(input("Enter the number of respective genre whose book details are desired: "))
         if choice == 1:
                  ret_fb()
         elif choice == 2:
                  ret_abb()
         elif choice == 3:
                  ret_ct()
         elif choice == 4:
                  ret_hb()
         elif choice == 5:
                  ret_shb()
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  ret_books()
         an = input("Do you want details of another book from another genre(yes or no)? ")
         if an == 'yes':
                  ret_books()

def upd_fb():
         print('1. Book Name')
         print("2. Book's Author")
         print('3. ISBN number')
         print('4. Download link')
         print(" ")
         choice = int(input("Enter the no. of respective detail you want to edit: "))
         if choice == 1:
                  Bname = input("Enter new name: ")
                  Bauthor = input("Enter name of author: ")
                  curs.excute('UPDATE fiction_books SET Bname = %s WHERE Bauthor = %s',(Bname,Bauthor))
                  con.commit()
                  print("   --------------------------------")
                  print("   BOOK NAME CHANGED SUCCESSFULLY!!")
                  print("   --------------------------------")
         elif choice == 2:
                  Bauthor = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE fiction_books SET Bauthor = %s WHERE Bname = %s',(Bauthor,Bname))
                  con.commit()
                  print("   ----------------------------------")
                  print("   AUTHOR NAME CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------------")
         elif choice == 3:
                  ISBN = int(input("Enter new ISBN: "))
                  Bname = input("Enter name of book: ") 
                  curs.excute('UPDATE fiction_books SET ISBN = %s WHERE Bname = %s',(ISBN,Bname))
                  con.commit()
                  print("   ---------------------------")
                  print("   ISBN CHANGED SUCCESSFULLY!!")
                  print("   ---------------------------")
         elif choice == 4:
                  download_link = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE fiction_books SET download_link = %s WHERE Bname = %s',(download_link,Bname))
                  con.commit()
                  print("   ------------------------------------")
                  print("   DOWNLOAD LINK CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  upd_fb()
         rep = input("Do you want to edit detail of book from this genre(yes or no)? ")
         if rep == 'yes':
                  print(" ")
                  upd_fb()
                  
def upd_abb():
         print('1. Book Name')
         print("2. Book's Author")
         print('3. ISBN number')
         print('4. Download link')
         print(" ")
         choice = int(input("Enter the no. of respective detail you want to edit: "))
         if choice == 1:
                  Bname = input("Enter new name: ")
                  Bauthor = input("Enter name of author: ")
                  curs.excute('UPDATE autob_bio SET Bname = %s WHERE Bauthor = %s',(Bname,Bauthor))
                  con.commit()
                  print("   --------------------------------")
                  print("   BOOK NAME CHANGED SUCCESSFULLY!!")
                  print("   --------------------------------")
         elif choice == 2:
                  Bauthor = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE autob_bio SET Bauthor = %s WHERE Bname = %s',(Bauthor,Bname))
                  con.commit()
                  print("   ----------------------------------")
                  print("   AUTHOR NAME CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------------")
         elif choice == 3:
                  ISBN = int(input("Enter new ISBN: "))
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE autob_bio SET ISBN = %s WHERE Bname = %s',(ISBN,Bname))
                  con.commit()
                  print("   ---------------------------")
                  print("   ISBN CHANGED SUCCESSFULLY!!")
                  print("   ---------------------------")
         elif choice == 4:
                  download_link = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE autob_bio SET download_link = %s WHERE Bname = %s',(download_link,Bname))
                  con.commit()
                  print("   ------------------------------------")
                  print("   DOWNLOAD LINK CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  upd_abb()
         rep = input("Do you want to edit detail of book from this genre(yes or no)? ")
         if rep == 'yes':
                  print(" ")
                  upd_abb()

def upd_ct():
         print('1. Book Name')
         print("2. Book's Author")
         print('3. ISBN number')
         print('4. Download link')
         print(" ")
         choice = int(input("Enter the no. of respective detail you want to edit: "))
         if choice == 1:
                  Bname = input("Enter new name: ")
                  Bauthor = input("Enter name of author: ")
                  curs.excute('UPDATE crime_thrillers SET Bname = %s WHERE Bauthor = %s',(Bname,Bauthor))
                  con.commit()
                  print("   --------------------------------")
                  print("   BOOK NAME CHANGED SUCCESSFULLY!!")
                  print("   --------------------------------")
         elif choice == 2:
                  Bauthor = input("Enter new name: ")
                  Bname = input("Enter name of book: ") 
                  curs.excute('UPDATE crime_thrillers SET Bauthor = %s WHERE Bname = %s',(Bauthor,Bname))
                  con.commit()
                  print("   ----------------------------------")
                  print("   AUTHOR NAME CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------------")
         elif choice == 3:
                  ISBN = int(input("Enter new ISBN: "))
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE crime_thrillers SET ISBN = %s WHERE Bname = %s',(ISBN,Bname))
                  con.commit()
                  print("   ---------------------------")
                  print("   ISBN CHANGED SUCCESSFULLY!!")
                  print("   ---------------------------")
         elif choice == 4:
                  download_link = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE crime_thrillers SET download_link = %s WHERE Bname = %s',(download_link,Bname))
                  con.commit()
                  print("   ------------------------------------")
                  print("   DOWNLOAD LINK CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  upd_ct()
         rep = input("Do you want to edit detail of book from this genre(yes or no)? ")
         if rep == 'yes':
                  print(" ")
                  upd_ct()
                  
def upd_hb():
         print('1. Book Name')
         print("2. Book's Author")
         print('3. ISBN number')
         print('4. Download link')
         print(" ")
         choice = int(input("Enter the no. of respective detail you want to edit: "))
         if choice == 1:
                  Bname = input("Enter new name: ")
                  Bauthor = input("Enter name of author: ")
                  curs.excute('UPDATE historical_books SET Bname = %s WHERE Bauthor = %s',(Bname,Bauthor))
                  con.commit()
                  print("   --------------------------------")
                  print("   BOOK NAME CHANGED SUCCESSFULLY!!")
                  print("   --------------------------------")
         elif choice == 2:
                  Bauthor = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE historical_books SET Bauthor = %s WHERE Bname = %s',(Bauthor,Bname))
                  con.commit()
                  print("   ----------------------------------")
                  print("   AUTHOR NAME CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------------")
         elif choice == 3:
                  ISBN = int(input("Enter new ISBN: "))
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE historical_books SET ISBN = %s WHERE Bname = %s',(ISBN,Bname))
                  con.commit()
                  print("   ---------------------------")
                  print("   ISBN CHANGED SUCCESSFULLY!!")
                  print("   ---------------------------")
         elif choice == 4:
                  download_link = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE historical_books SET download_link = %s WHERE Bname = %s',(download_link,Bname))
                  con.commit()
                  print("   ------------------------------------")
                  print("   DOWNLOAD LINK CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  upd_hb()
         rep = input("Do you want to edit detail of book from this genre(yes or no)? ")
         if rep == 'yes':
                  print(" ")
                  upd_hb()
                  
def upd_shb():
         print('1. Book Name')
         print("2. Book's Author")
         print('3. ISBN number')
         print('4. Download link')
         print(" ")
         choice = int(input("Enter the no. of respective detail you want to edit: "))
         if choice == 1:
                  Bname = input("Enter new name: ")
                  Bauthor = input("Enter name of author: ")
                  curs.excute('UPDATE self_help SET Bname = %s WHERE Bauthor = %s',(Bname,Bauthor))
                  con.commit()
                  print("   --------------------------------")
                  print("   BOOK NAME CHANGED SUCCESSFULLY!!")
                  print("   --------------------------------")
         elif choice == 2:
                  Bauthor = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE self_help SET Bauthor = %s WHERE Bname = %s',(Bauthor,Bname))
                  con.commit()
                  print("   ----------------------------------")
                  print("   AUTHOR NAME CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------------")
         elif choice == 3:
                  ISBN = int(input("Enter new ISBN: "))
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE self_help SET ISBN = %s WHERE Bname = %s',(ISBN,Bname))
                  con.commit()
                  print("   ---------------------------")
                  print("   ISBN CHANGED SUCCESSFULLY!!")
                  print("   ---------------------------")
         elif choice == 4:
                  download_link = input("Enter new name: ")
                  Bname = input("Enter name of book: ")
                  curs.excute('UPDATE self_help SET download_link = %s WHERE Bname = %s',(download_link,Bname))
                  con.commit()
                  print("   ------------------------------------")
                  print("   DOWNLOAD LINK CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  upd_shb()
         rep = input("Do you want to edit detail of book from this genre(yes or no)? ")
         if rep == 'yes':
                  print(" ")
                  upd_shb()
         
def update_books():
         print('1. Fiction Book')
         print('2. Autobiography/Biography')
         print('3. Crime Thrillers')
         print('4. Historical Book')
         print('5. Self Help Book')
         choice = int(input("Enter the no. of respective genre you whose book details you want to update: "))
         if choice == 1:
                  upd_fb()
         elif choice == 2:
                  upd_abb()
         elif choice == 3:
                  upd_ct()
         elif choice == 4:
                  upd_hb()
         elif choice == 5:
                  upd_shb()
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  update_books()
         an = input("Do you want to edit details of book from another genre(yes or no)? ")
         if an == 'yes':
                  print(" ")
                  update_books()

def update_admin():
         print('1. Name')
         print('2. Designation')
         print('3. Age')
         print('4. Gender')
         print('5. Address')
         print('6. Contact')
         print('7. Email')
         print('8. Password')
         print(" ")
         ed = int(input("Enter the no. of respective detail you want to edit: "))
         if ed == 1:
                  Name = input("Enter new name: ")
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Name = %s WHERE Password = %s',(Designation,Password))
                  con.commit()
                  print("   ---------------------------")
                  print("   NAME CHANGED SUCCESSFULLY!!")
                  print("   ---------------------------")
         elif ed == 2:
                  Designation = input("Enter new designation: ")
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Designation = %s WHERE Password = %s',(Name,Password))
                  con.commit()
                  print("   ----------------------------------")
                  print("   DESIGNATION CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------------")
         elif ed == 3:
                  Age = int(input("Enter new age: "))
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Age = %s WHERE Password = %s',(Age,Password))
                  con.commit()
                  print("   --------------------------")
                  print("   AGE CHANGED SUCCESSFULLY!!")
                  print("   --------------------------")
         elif ed == 4:
                  Gender = input("Enter new gender: ")
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Gender = %s WHERE Password = %s',(Gender,Password))
                  con.commit()
                  print("   -----------------------------")
                  print("   GENDER CHANGED SUCCESSFULLY!!")
                  print("   -----------------------------")
         elif ed == 5:
                  Address = input("Enter new address: ")
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Address = %s WHERE Password = %s',(Address,Password))
                  con.commit()
                  print("   ------------------------------")
                  print("   ADDRESS CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------")
         elif ed == 6:
                  Contact = int(input("Enter new contact: "))
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Contact = %s WHERE Password = %s',(Contact,Password))
                  con.commit()
                  print("   ------------------------------")
                  print("   CONTACT CHANGED SUCCESSFULLY!!")
                  print("   ------------------------------")
         elif ed == 7:
                  Email = input("Enter new email: ")
                  Password = ad_pass
                  curs.execute('UPDATE admin SET Email = %s WHERE Password = %s',(Name,Password))
                  con.commit()
                  print("   ----------------------------")
                  print("   EMAIL CHANGED SUCCESSFULLY!!")
                  print("   ----------------------------")
         elif ed == 8:
                  Password = input("Enter new password: ")
                  Email = ad_mail
                  curs.execute('UPDATE admin SET Password = %s WHERE Email = %s',(Password,Email))
                  con.commit()
                  print("   -------------------------------")
                  print("   PASSWORD CHANGED SUCCESSFULLY!!")
                  print("   -------------------------------")
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
         pq = input("Do you want to change another detail(yes or no)? ")
         if pq == 'yes':
                  update_admin()

def admin_menu():
         print(" ")
         print("        W E L C O M E    A D M I N")
         print("        --------------------------")
         print("                 M E N U")
         print("        --------------------------")
         print('        1. Add books')
         print('        2. Remove book')
         print('        3. Add new admin')
         print('        4. Remove an admin')
         print('        5. Retrieve book details')
         print('        6. Retrieve admin details')
         print('        7. Retrieve user details')
         print('        8. Update admin details')
         print('        9. Update book details')
         print('        10. Logout')
         print(" ")
         choice = int(input("Enter your choice: "))
         if choice == 1:
                  add_books()
         elif choice == 2:
                  rem_books()
         elif choice == 3:
                  admin_signin()
         elif choice == 4:
                  rem_admin()
         elif choice == 5:
                  ret_books()
         elif choice == 6:
                  ch = 'yes'
                  while ch == 'yes':
                           Name = input("Enter desired admin's name: ")
                           Designation = input("Enter admin's designation: ")
                           curs.execute('SELECT * from admin where (Name,Designation)=(%s,%s)',(Name,Designation))
                           data = curs.fetchall()
                           tab = ['Name','Designation','Age','Gender','Address','Contact','Email','Password']
                           print(tabulate(data, headers = tab, tablefmt = 'grid'))
                           ch = input("Do you want details of another admin? (yes or no)? ")
         elif choice == 7:
                  ch = 'yes'
                  while ch == 'yes':
                           Name = input("Enter name of desired user: ")
                           Email = input("Enter email of desired user: ")
                           curs.execute('SELECT * from users where (Name,Email)=(%s,%s)',(Name,Email))
                           data = curs.fetchall()
                           tab = ['Name','Age','Gender','Country','Contact','Email','Password']
                           print(tabulate(data, headers = tab, tablefmt = 'grid'))
                           ch = input("Do you want details of another user? (yes or no)? ")
         elif choice == 8:
                  update_admin()
         elif choice == 9:
                  update_books()
         elif choice == 10:
                  logout()
         else:
                  print("  ---INVALID CHOICE---")
                  print("       TRY AGAIN")
                  print("  --------------------")
                  admin_menu()
         print(" ")
         bc = input("Do you want to go back to main menu(yes or no)? ")
         if bc == 'yes':
                  admin_menu()
                  
def admin_login():
         ab = []
         Email = input("Enter your mail id: ")
         Password = input("Enter your password: ")
         curs.execute('select * from admin where (Email,Password)=(%s,%s)',(Email,Password))
         a = curs.fetchall()
         con.commit()
         if a:
                  global ad_mail
                  ad_mail = a[0][6]
                  global ad_pass
                  ad_pass = a[0][7]
                  admin_menu()
         else:
                  print("     Oops!!Wrong Credentials")
                  print("           Try Again")
                  print("---------------------------------")
                  print("Redirecting back to login page...")
                  print("---------------------------------")
                  admin_login()

main()
