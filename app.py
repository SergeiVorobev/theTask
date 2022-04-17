from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, delete, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///grading.db', echo=True)
meta = MetaData(bind=engine)
MetaData.reflect(meta)

grading = Table(
    'grades', meta,
    Column('DBN', String, primary_key=True),
    Column('School Name', String),
    Column('Category', String),
    Column('Total Enrollment', String),
    Column('Grade K', Integer),
    Column('Grade 1', Integer),
    Column('Grade 2', Integer),
    Column('Grade 3', Integer),
    Column('Grade 4', Integer),
    Column('Grade 5', Integer),
    Column('Grade 6', Integer),
    Column('Grade 7', Integer),
    Column('Grade 8', Integer),
    Column('ELA Level 1', Integer),
    Column('ELA Level 2', Integer),
    Column('ELA Level 3', Integer),
    Column('ELA Level 4', Integer),
    Column('MATH Level 1', Integer),
    Column('MATH Level 2', Integer),
    Column('MATH Level 3', Integer),
    Column('MATH Level 4', Integer)
)

meta.create_all(engine)
