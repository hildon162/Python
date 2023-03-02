import pyodbc
#conn = pyodbc.connect('Driver={SQL Server Native Client 10.0};'
#                      'Server=database-2.cxohp3wvsdmn.us-east-2.rds.amazonaws.com;'
#                      'UID=admin;'
#                      'PWD=e6lqyU9JtwD1irnFDF2t;'
#                      'Database=DWTEST')
#conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
#                      'Server=mwort1\DATAWHS1;'
#                      'UID=PowerBI;'
#                      'PWD=R3p0r7s8i;'
#                      'Database=DataWarehouse')
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=epapp02;'
                      'UID=pytest;'
                      'PWD=R3p0r7s8i;'
                      'Database=E10Prod')

cursor = conn.cursor()
cursor.execute('SELECT CustNum,EMailAddress FROM Erp.Customer order by CustNum')

def find_all_indexes(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1

#row = cursor.fetchone()
#print(str(row[0]))
emails = []

for row in cursor:
    #for column in row:
    #    print(column)
    #rsize = len(row)
    email = row[1].lower()
    #s = email.count('@')
    s = find_all_indexes(email, ';')
    s += find_all_indexes(email, ',')
    s.sort()
    if s == []:
        s = [len(email)]

    start_pos = 0
    for x in s:
        pos = email.find('@',start_pos)
        emails.append(email[pos+1:x])
        start_pos = x 
    #p = email.find('@')
    #print(f"{email} : {s} : {p}")

#print(set(emails))
myset = set(emails)
emails = list(myset)
emails.sort()

f = open("domains.csv", "w")

for x in emails:
    if x != "":
        f.write(x + "\n")

f.close()

