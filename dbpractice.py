# Database Practice
import sqlite3

# connection allows us to connect
# python to a SQL databse :)
connection = sqlite3.connect("./database.db")
# cursor allows us to interact with the SQL DB
cursor = connection.cursor()
query = """
SELECT SUM(Price) AS TotalPrices from Products;
"""
result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")

# BOTTOM/END OF OUR CODE
connection.commit() # this commits our changes
connection.close() # this disconnects our connection