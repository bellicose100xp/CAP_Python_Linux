#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect("test.db")
conn.execute("DROP TABLE IF EXISTS COMPANY")


# Create Table
conn.execute(
    """CREATE TABLE COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);"""
)

# Add Records to the Database
conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )"
)
conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
)
conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
)
conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"
)

# Update Row
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")

# Delete Row
conn.execute("DELETE from COMPANY where ID = 2;")

# Must commit all changes for it to take effect
conn.commit()

conn.row_factory = sqlite3.Row
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

for row in cursor:
    print(f"{row['NAME']}: {row['SALARY']}")

print("Records created successfully")
conn.close()
