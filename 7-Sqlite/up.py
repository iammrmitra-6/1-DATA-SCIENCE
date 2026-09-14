import sqlite3

# 1. Connect to a database file (or use ':memory:' for a temporary database)
conn = sqlite3.connect('example.db')

# 2. Create a cursor object to execute SQL commands
cursor = conn.cursor()

# 3. Execute SQL statements
cursor.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
cursor.execute("INSERT INTO stocks VALUES ('2026-01-05','BUY','RHAT',100,35.14)")

# 4. Commit the changes and close the connection
conn.commit()
conn.close()
