import sqlite3

# Connect to a SQLite database (creates the file if it doesn't already exist)
connection = sqlite3.connect("students.db")

# A cursor is used to execute SQL commands
cursor = connection.cursor()

# Create a table (only if it doesn't already exist, so re-running the script is safe)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# Insert some sample data
students_data = [
    ("Vinny Mutopa", 26, "Accounting"),
    ("Rhiana Bells", 21, "Information Systems"),
    ("Auri Mutopa", 19, "Social Work"),
]

cursor.executemany(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    students_data
)

# Commit the changes so they are saved to the database file
connection.commit()

# Retrieve and display all rows from the table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Students in the database:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

# Always close the connection when done
connection.close()