import mysql.connector as mysql

db = mysql.connect(
    user='st4',
    passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name ) VALUES ('Razmik', 'Grygoryan')")
student_id = cursor.lastrowid
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('TEST1', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('TEST2', {student_id})")
cursor.execute(f"INSERT INTO `groups` VALUES ({student_id}, 'TEST', 'sep 1977', 'dec 1988')")
cursor.execute(f"UPDATE students SET group_id = {student_id} WHERE id = 328'")
cursor.execute(f"INSERT INTO subjets (title) VALUES ('TEST1')")
first_subject_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('TEST111', {first_subject_id})")
first_lesson_id = cursor.lastrowid
cursor.execute(f"INSERT INTO subjets (title) VALUES ('TEST2')")
second_subject_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('TEST222', {second_subject_id})")
second_lesson_id = cursor.lastrowid
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('7', {first_lesson_id}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('7', {second_lesson_id}, {student_id})")
cursor.execute(f"SELECT value FROM marks")
cursor.execute(f"SELECT title from books where taken_by_student_id = {student_id}")
cursor.execute(f'''SELECT
    students.id AS student_id,
    students.name AS student_name,
    students.second_name AS student_second_name,
    "groups".id AS group_id,
    "groups".title AS group_title,
    books.id AS book_id,
    books.title AS book_title,
    lessons.id AS lesson_id,
    lessons.title AS lesson_title,
    subjets.id AS subject_id,
    subjets.title AS subject_title,
    marks.id AS mark_id,
    marks.value AS mark_value
FROM students
JOIN "groups" ON students.id = "groups".id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.id = {student_id};
''')
db.commit()
db.close()
