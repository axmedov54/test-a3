import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                  password="xudashukur10",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="carshop")
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE cars
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         IN); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



import psycopg2
from psycopg2 import Error

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        user="postgres",
        password="xudashukur10",
        host="127.0.0.1",
        port="5432",
        database="carshop"
    )
    cursor = connection.cursor()
    yaratish = "INSERT INTO cars (id,model,price)VALUES (%s,%s,%s) "
    qoshish = ("DOGE CHARGER",55000)
    cursor.execute(yaratish,qoshish)
    connection.commit()
    print("malumot qoshildi")
    
    
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
        print("PostgreSQL connection is closed")   













































