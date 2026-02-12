import pymysql
from os import getenv

DB_HOST = getenv("DB_HOST", "mysql")
DB_PORT = int(getenv("DB_PORT", "3306"))
DB_USER = getenv("DB_USER", "root")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_NAME = getenv("DB_NAME", "DB_WEEK_17")

conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER, 
        password=DB_PASSWORD,    
        database=DB_NAME)  

cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")


cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customerNumber INT PRIMARY KEY,
    customerName VARCHAR(255),
    contactLastName VARCHAR(255),
    contactFirstName VARCHAR(255),
    phone VARCHAR(255),
    addressLine1 VARCHAR(255),
    addressLine2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postalCode VARCHAR(255),
    country VARCHAR(255),
    salesRepEmployeeNumber INT,
    creditLimit VARCHAR(255)
    )''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    orderNumber INT PRIMARY KEY,
    orderDate VARCHAR(255),
    requiredDate VARCHAR(255),
    shippedDate VARCHAR(255),
    status VARCHAR(255),
    comments VARCHAR(255),
    customerNumber INT,    
    FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
    )''')

cursor.execute('''
    INSERT INTO customers (
        customerNumber, customerName, contactLastName, contactFirstName,
        phone, addressLine1, addressLine2, city, state, postalCode,
        country, salesRepEmployeeNumber, creditLimit
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')

cursor.execute('''
    INSERT INTO orders (
        orderNumber, orderDate, requiredDate, shippedDate,
        status, comments, customerNumber
    ) VALUES (%s,%s,%s,%s,%s,%s,%s)''')

conn.commit()
cursor.close()
conn.close()

