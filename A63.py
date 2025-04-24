# 63. Insert and read data from a SQLite database.
import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Step 2: Insert data into the 'users' table
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
               ("Alice", "alice@example.com", 25))

cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
               ("Bob", "bob@example.com", 30))

# Step 3: Commit the changes
conn.commit()

# Step 4: Read (select) data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in database:")
for row in rows:
    print(row)

# Step 5: Close the connection
conn.close()
