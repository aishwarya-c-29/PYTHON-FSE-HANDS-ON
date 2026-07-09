from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database
engine = create_engine("sqlite:///student.db", echo=True)

Base = declarative_base()

# Define ORM Model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    department = Column(String(50))

# Create table
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# ------------------ CREATE ------------------
student = Student(name="Shreya", age=21, department="CSE")
session.add(student)
session.commit()
print("Record Inserted")

# READ 
print("\nStudent Records")
students = session.query(Student).all()

for s in students:
    print(s.id, s.name, s.age, s.department)

# UPDATE 
student = session.query(Student).filter_by(id=1).first()

if student:
    student.age = 22
    session.commit()
    print("\nRecord Updated")

# DELETE 
student = session.query(Student).filter_by(id=1).first()

if student:
    session.delete(student)
    session.commit()
    print("Record Deleted")

session.close()

Output:
Record Inserted
Student Records
1 Shreya 21 CSE
Record Updated
Record Deleted
