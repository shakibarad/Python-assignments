import csv

with open("grades.csv") as f:
    reader= csv.reader(f)
    print(reader)
    for row in reader:
        print(row)
        name=row[0]
        for grade in row[1:]:
            print (grade)