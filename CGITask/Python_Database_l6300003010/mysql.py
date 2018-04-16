import pymysql
import info

# Initialize database connect
db = pymysql.connect(info.host, info.user, info.passwd, info.database)
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE(
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT)"""

cursor.execute(sql)

# Data
information = [
    ('Mary', 'Smith', 19, 'F', 1800),
    ('Gary', 'Lee', 21, 'M', 2000),
    ('Becky', 'Bucked', 21, 'F', 2800),
    ('Flora', 'Aniston', 17, 'F', 2300)
]

# Insert data into database
insert = "INSERT INTO EMPLOYEE VALUES ('%s' ,'%s' ,'%s' ,'%s' ,'%s')"
for record in information:
    try:
        cursor.execute(insert % record)
        db.commit()
    except:
        db.rollback()

# Print out how many female employees in the company
sql1 = "SELECT * FROM EMPLOYEE WHERE SEX='F'"
try:
    cursor.execute(sql1)
    results = cursor.fetchall()
    print("There are %d female employees in the company." % (len(results)))
    print()  # Open a new line
except:
    db.rollback()

# Print out employees' information whose age is under 20
print("##### Age is under 20 #####")
sql2 = "SELECT * FROM EMPLOYEE WHERE AGE<=20"
try:
    cursor.execute(sql2)
    results = cursor.fetchall()
    print("FIRST_NAME\tLAST_NAME\tAGE\tSEX\tINCOME")
    for info in results:
        print("%-12s%-12s%-4s%-4s%-4s" % (info[0], info[1], info[2], info[3], info[4]))

    print()  # Open a new line
except:
    db.rollback()

# Update the income to 2000
sql3 = "UPDATE EMPLOYEE SET INCOME=2000 WHERE INCOME<2000"
try:
    cursor.execute(sql3)
    db.commit()
except:
    db.rollback()

# List out all employees whose income is greater or equal to 2000
print("##### Income is greater or equal to 2000 #####")
sql4 = "SELECT * FROM EMPLOYEE WHERE INCOME>=2000"
try:
    cursor.execute(sql4)
    results = cursor.fetchall()
    print("FIRST_NAME\tLAST_NAME\tAGE\tSEX\tINCOME")
    for info in results:
        print("%-12s%-12s%-4s%-4s%-4s" % (info[0], info[1], info[2], info[3], info[4]))

    print()  # Open a new line
except:
    db.rollback()

# Delete employees whose age is under than 18
sql5 = "DELETE FROM EMPLOYEE WHERE AGE<=18"
try:
    cursor.execute(sql5)
    db.commit()
except:
    db.rollback()

# List out all employee's information
print("##### All employee's information #####")
sql6 = "SELECT * FROM EMPLOYEE"
try:
    cursor.execute(sql6)
    results = cursor.fetchall()
    print("FIRST_NAME\tLAST_NAME\tAGE\tSEX\tINCOME")
    for info in results:
        print("%-12s%-12s%-4s%-4s%-4s" % (info[0], info[1], info[2], info[3], info[4]))

    print()  # Open a new line
except:
    db.rollback()

db.close()  # Close database connection
