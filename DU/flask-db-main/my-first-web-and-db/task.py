import sqlite3
from task_data import *
from task_create import *

conn = sqlite3.connect("chat_app.db")

cur = conn.cursor()

cur.execute(users_create_table)
cur.execute(rooms_create_table)
cur.execute(messages_create_table)
#cur.execute(insert_users)
#cur.execute(insert_rooms)
#cur.execute(insert_messages)
conn.commit()





cur.execute("""
SELECT messages.message, users.username
FROM messages
JOIN users ON messages.user_id = users.id;
""")

#data = cur.fetchall()
#print(data)


cur.execute("""
SELECT rooms.name, messages.message
FROM rooms
JOIN messages ON rooms.id = messages.room_id
ORDER BY messages.id DESC;
""")
#data = cur.fetchall()
#print(data)

cur.execute("""
SELECT messages.message, users.username
FROM messages
JOIN users ON messages.user_id = users.id
WHERE messages.timestamp >= datetime('now', '-3 minute');
""")


data = cur.fetchall()
print(data)
print("DONE")