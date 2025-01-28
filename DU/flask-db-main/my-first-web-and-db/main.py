import sqlite3

conn = sqlite3.connect("chat_app.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100)
);
""")

cur.execute("""
INSERT INTO Instructors (name, specialization)
VALUES ('AdamPRO', 'trener');
""")

cur.execute("""
DELETE FROM Instructors
WHERE name='Adam';
""")


cur.execute("""
UPDATE Instructors
SET name='Eva'
WHERE name='AdamPRO';
""")
conn.commit()

cur.execute("""
SELECT * FROM Instructors;
""")

data = cur.fetchall()
print(data)
print("DONE")