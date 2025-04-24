# Connect to a SQLite database and create a table
import sqlite3

# Step 1: Connect to (or create) a SQLite database
conn = sqlite3.connect('my_database.db')

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Write SQL to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
''')

# Step 4: Commit changes and close the connection
conn.commit()
conn.close()

print("Database connected and table created successfully.")

