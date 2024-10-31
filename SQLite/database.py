import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("DELETE FROM customers WHERE rowid = 2")

c.execute("SELECT rowid,* FROM customers")

items = c.fetchall()
# print(items)

for item in items:
    print(item)

conn.commit()
conn.close()    