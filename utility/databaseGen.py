import sqlite3
#connect to database file
dbconnect = sqlite3.connect("telegram.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''insert into restaurant(id, title, lastVisitedUtc, vegetarian, ass, distance, cost, quality, quantity) VALUES (2,"Calavera","2020-02-05 21:45:30", 0, 3, 5, 9, 7,9);''');
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM restaurant');
#print data
for row in cursor:
    print(row['id'],row['title'],row['ass'] );
#close the connection
dbconnect.close();
