import psycopg2
import psycopg2.extras
import os

DB_URL = os.environ.get("DATABASE_URL", "dbname=astrology_app")

def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL) # opening a connection
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use the cursor to run SQL commands
    cursor.execute(query, parameters) # begin transaction
    results = cursor.fetchall()
    connection.commit() # end transaction
    connection.close() # close transaction 
    return results
