import csv

file_path = r'C:\Users\vkris\OneDrive\Desktop\Sample Test\Test_csvFile.csv'
users = []
status = []
with open(file_path,'r') as csv_file:
    file = csv.reader(csv_file)
    #print(list(file))
    for row in file:
        users.append(row[0])
        status.append(row[1])

print(users)
print(status)

index = users.index('HB5037294')
print(status[index])