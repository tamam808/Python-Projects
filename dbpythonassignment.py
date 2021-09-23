# this imports the sqlite3 module which allows us to make and modify DBs in python
import sqlite3

# this when used the first time creates a db with the name test
conn = sqlite3.connect('test.db')

# this means to do this while connected to the DB
with conn:
# this cursor method allows us to invoke SQLite statements
    cur = conn.cursor()
# here we use the conn.cursor method (which we have given assigned to variable cur) to execute a SQL statement that creates a table
##with an ID col that auto increments and a column for our txt files
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtFiles(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fileName STRING)')
# this conn.commit() method is what commits the data above into the DB
    conn.commit()
# here we end our connection to the DB in order to avoid memory leaks
conn.close()

# this time the connect method is used just to connect to the test DB since it aleady exists
conn = sqlite3.connect('test.db')

# tuple of files
files_tuple = ('information.docx', 'Hello.txt', 'myImage.png' \
               'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# this for loop will iterate through the tuple above and find all the elements that end with .txt
for i in files_tuple:
# this line of code that iterates through the touple and grabs the elements that end with .txt
    if i.endswith('.txt'):
        with conn:
            cur = conn.cursor()
# we want the value for each row to be one file out of the tuple
# so (i,) will create a one-element tuple
            cur.execute("INSERT INTO tbl_txtFiles (col_fileName) VALUES (?)", (i,))
# because this print(i) method is inside the loop it will do this everytime it finds a new file that ends with .txt through its iterations
            print(i)

conn.close()
