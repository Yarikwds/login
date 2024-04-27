# import sqlite3

# conn = sqlite3.connect("students.db")

# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS students (
#                student_name TEXT,
#                class TEXT,
#                avr_score INT,
#                parents_name TEXT
# )""")

# # cursor.execute("""INSERT INTO students VALUES (
# #                'Ланова Дарія',
# #                '7Б',
# #                10,
# #                'Ланова Раїса'
# # )  """)

# cursor.execute("""SELECT * FROM students WHERE avr_score>9""")

# stud = cursor.fetchall()

# for s in stud:
#     print(f"{s[0]}, {s[1]} клас, середня оцінка {s[2]}, мати/батько {s[3]}.")

# conn.commit()