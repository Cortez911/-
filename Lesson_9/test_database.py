import os
import pytest
from sqlalchemy import create_engine, text, Column, Integer, String, ForeignKey, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./mydatabase9dz.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subjects'  # Исправлено: __tablename__
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Student(Base):
    __tablename__ = 'students'  # Исправлено: __tablename__
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.id'))


def create_tables_if_not_exist():
    inspector = inspect(engine)
    if not inspector.has_table('subjects'):
        Base.metadata.create_all(engine)

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    create_tables_if_not_exist()
    yield
    # Cleanup: Удаляем базу данных после завершения тестов
    try:
        os.remove(DATABASE_URL[10:-3]) # Удаляем файл mydatabase9dz.db
    except FileNotFoundError:
        pass #Файл может не существовать, если тесты упали раньше


@pytest.fixture(scope="function")
def session():
    session = Session()
    yield session
    session.close()


@pytest.mark.suppress_movedin20_warning
def test_add_student(session):
    new_subject = Subject(name="New Subject")
    session.add(new_subject)
    session.flush()
    new_student = Student(name="Test Student", subject_id=new_subject.id)
    session.add(new_student)
    session.commit()

    result = session.query(Student).filter(Student.name == "Test Student").first()
    assert result is not None


@pytest.mark.suppress_movedin20_warning
def test_update_student(session):
    new_subject = Subject(name="Another Subject")
    session.add(new_subject)
    session.flush()
    new_student = Student(name="Update Student", subject_id=new_subject.id)
    session.add(new_student)
    session.commit()
    new_student.name = "Updated Student"
    session.commit()

    result = session.query(Student).filter(Student.name == "Updated Student").first()
    assert result is not None

@pytest.mark.suppress_movedin20_warning
def test_delete_student(session):
    new_subject = Subject(name="Delete Subject")
    session.add(new_subject)
    session.flush()
    new_student = Student(name="Delete Student", subject_id=new_subject.id)
    session.add(new_student)
    session.commit()
    session.delete(new_student)
    session.commit()

    result = session.query(Student).filter(Student.name == "Delete Student").first()
    assert result is None
