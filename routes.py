from flask import jsonify
from db_config import get_database_connection

# Connect to the database
db = get_database_connection()


def get_features():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM features")
    features = cursor.fetchall()
    cursor.close()
    return features
