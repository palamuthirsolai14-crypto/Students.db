import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    sid TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

conn.commit()
print("Database created successfully.")
conn.close()
