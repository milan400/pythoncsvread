import csv
with open('D:\District.csv') as csvfile:
     readCsv = csv.reader(csvfile,delimiter=',')
     for row in readCsv:
         print(row)
         print(row[0])
         print(row[0],row[1],row[2],)
    
