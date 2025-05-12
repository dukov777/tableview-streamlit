import sqlite3

# Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
''')

# Insert some data
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
#               ("Alice", "alice@example.com"))
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
#               ("Bob", "bob@example.com"))

# Commit the changes
# conn.commit()

# Query the data
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)

# Close the connection
conn.close()