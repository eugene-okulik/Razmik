import mysql.connector as mysql
import csv
import os
import dotenv


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

cursor = db.cursor(dictionary=True)
query = '''SELECT
    name, second_name,
    "groups".title AS group_title,
    books.title AS book_title,
    subjets.title AS subject_title,
    lessons.title AS lesson_title,
    marks.value AS mark_value
FROM students
JOIN "groups" ON students.id = "groups".id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
'''
cursor.execute(query)
data = cursor.fetchall()
with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    next(file_data)
    for row in file_data:
        if row not in data:
            print(f"Данные из файла, которых нет в базе данных: {row}")

db.close()
