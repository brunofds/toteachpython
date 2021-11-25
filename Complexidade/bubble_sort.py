import csv

with open("202101_AuxilioEmergencial.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    i = 10
    for row in csv_reader:
        if i <= 0:
            break
        else:
            print(row)
            i -= 1


# Using