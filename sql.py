import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("error")
    return conn

def select_all_restaurants(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurants")
    rows = cur.fetchall()
    return rows

#database = "/home/pi/Documents/TelegramBot/telegram.db"
#conn = create_connection(database)
#with conn:
#    print("1. Query task by priority:")
#    rows = select_all_restaurants(conn)
#    for r in rows:
#        print(r)

