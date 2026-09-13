import psycopg

import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = psycopg.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO measurements (
        device_id,
        device_status,
        battery_status,
        motion_status,
        timestamp
    )
    VALUES (%s, %s, %s, %s, %s)
""", (
    1,
    "Connected",
    85,
    1,
    200000
))

connection.commit()

cursor.close()
connection.close()

print("Measurement inserted")