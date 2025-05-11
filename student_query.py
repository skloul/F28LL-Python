
import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the students table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Insert sample data
cursor.execute('INSERT OR IGNORE INTO students (student_id, name) VALUES (?, ?)', (101, 'Omair'))

# Fetch a record with student_id = 101
student_id = 101
cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
record = cursor.fetchone()

# Display the result
if record:
    print("Student Record:", record)
else:
    print("No student found with ID =", student_id)

# Commit changes and close the connection
conn.commit()
conn.close()
