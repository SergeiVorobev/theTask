from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, delete, Table, MetaData, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

"""
Creating the table
"""
engine = create_engine('sqlite:///grading.db', echo=True)
meta = MetaData(bind=engine)
MetaData.reflect(meta)

grading = Table(
    'grades', meta,
    Column('id', Integer, primary_key=True),
    Column('DBN', String),
    Column('School_name', String),
    Column('Category', String),
    Column('Total_enrollment', String),
    Column('Grade_K', String),
    Column('Grade_1', String),
    Column('Grade_2', String),
    Column('Grade_3', String),
    Column('Grade_4', String),
    Column('Grade_5', String),
    Column('Grade_6', String),
    Column('Grade_7', String),
    Column('Grade_8', String),
    Column('ELA_level_1', String),
    Column('ELA_level_2', String),
    Column('ELA_level_3', String),
    Column('ELA_level_4', String),
    Column('MATH_level_1', String),
    Column('MATH_level_2', String),
    Column('MATH_level_3', String),
    Column('MATH_level_4', String),

)

meta.create_all(engine)
