# a built-in Python library that allows you to interact with SQLite databases — 
# a lightweight, self-contained, serverless SQL database engine.
import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the students table if it doesn't exist

# Fetch a record with student_id = 101
student_id = 101
cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
record = cursor.fetchone()

# Display the result
if record:
    print("Student Record:", record)
else:
    print("No student found with ID =", student_id)

# Commit changes if any, and then close the connection
conn.commit()
conn.close()
