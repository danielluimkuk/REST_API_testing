
import sqlite3
# conn = sqlite3.connect("people.db")
# people = [
#     "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
#     "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
#     "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
# ]
# for person_data in people:
#     insert_cmd = f"INSERT INTO person VALUES ({person_data})"
#     conn.execute(insert_cmd)


# conn.commit()

conn = sqlite3.connect("people.db")
cur = conn.cursor()
cur.execute("SELECT * FROM person")


people = cur.fetchall()
for person in people:
    print(person)