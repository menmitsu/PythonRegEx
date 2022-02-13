import re
import csv

file = open('Nov_12.csv')

print(type(file))

# print (file.read())


csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rows = []
numLines=0
for row in csvreader:
        rows.append(row)
        numLines+=1
        if(row[0]!=row[1]):
            # print("False")
            print("Classified text is "+row[0] + "   "+row[1])
            matched=re.match("[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][' ']['T'][A-Z][A-Z]?[0-9][0-9]?",row[1]);
            is_match = bool(matched)
            print("\n")
            print("Regex match is "+str(is_match))
            print("\n")



# print(rows)




file.close()
