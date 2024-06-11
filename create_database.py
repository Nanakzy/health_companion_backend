import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

# Create database if it doesn't exist
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS healthcompanion")
db.commit()
cursor.close()
db.close()

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="healthcompanion"
)

# Create tables if they don't exist
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS features (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
""")
db.commit()
cursor.close()
db.close()
