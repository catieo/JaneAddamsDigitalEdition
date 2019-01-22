import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost', 'port': '8889',
  'database': 'ramapoed_omek1',
  'raise_on_warnings': True,
}

connection = mysql.connector.connect(**config)
print("success 0")
cursor = connection.cursor()
print("success 1")
cursor.close()
print("success 2")
