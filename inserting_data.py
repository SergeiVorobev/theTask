"""
Read csv file and inserting into 'grades' table
"""
import csv
from create_table import *

file = open("2015-2016_Demographic_Data_-_Grades_K-8_School.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
i = 0

for line in csvreader:
    i += 1
    rows.append(line)
    insert = grading.insert().values(
        id=i,
        DBN=line[0],
        School_name=line[1],
        Category=line[2],
        Total_enrollment=line[3],
        Grade_K=line[4],
        Grade_1=line[5],
        Grade_2=line[6],
        Grade_3=line[7],
        Grade_4=line[8],
        Grade_5=line[9],
        Grade_6=line[10],
        Grade_7=line[11],
        Grade_8=line[12],
        ELA_level_1=line[49],
        ELA_level_2=line[51],
        ELA_level_3=line[53],
        ELA_level_4=line[55],
        MATH_level_1=line[60],
        MATH_level_2=line[62],
        MATH_level_3=line[64],
        MATH_level_4=line[66],

    )
    engine.execute(insert)

# Get the `books` table from the Metadata object

sql = text("SELECT * from grades")

# Fetch all the records
result = engine.execute(sql).fetchall()

# View the records
for record in result:
    print("\n", record)
