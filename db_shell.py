from app import db, Student

# john = Student(firstname='john', lastname='doe', email='jd@example.com', age=23, bio='Biology student')
# print(john)
# db.session.add(john)
# db.session.commit()

# sammy = Student(firstname='Sammy', lastname='Shark', email='sammyshark@example.com', age=20, bio='Marine biology student')

# carl = Student(firstname='Carl', lastname='White', email='carlwhite@example.com', age=22, bio='Marine geology student')

# db.session.add(sammy)
# db.session.add(carl)
# db.session.commit()

students = Student.query.all()
print(students)

stud = Student.query.filter_by(firstname='Sammy').all()
print(stud)