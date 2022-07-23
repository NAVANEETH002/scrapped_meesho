import sqlite3

def connection(dbname):
    conn = sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS MEESHO_SHIRTS (TITLE TEXT,DISCOUNT TEXT,PRICE INT,RATING TEXT,FREE_DELIVERY TEXT)")

    print("Table Created")
    conn.close()

def inserttable(dbname, values):
    conn = sqlite3.connect(dbname)
    insert_sql = "INSERT INTO MEESHO_SHIRTS (TITLE, DISCOUNT, PRICE, RATING, FREE_DELIVERY) VALUES(?, ?, ?, ?, ?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()

def get_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM MEESHO_SHIRTS")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
