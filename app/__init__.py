from flask import Flask
from peewee import *
from dotenv import load_dotenv
import os
import datetime
import time

load_dotenv()
app = Flask(__name__)


if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

print("Using DB:", mydb)

# Retry DB connection
MAX_RETRIES = 10
for attempt in range(MAX_RETRIES):
    try:
        mydb.connect()
        print("Connected to database.")
        break
    except Exception as e:
        print(f"DB connect failed (attempt {attempt+1}): {e}")
        time.sleep(3)
else:
    raise Exception("DB connection failed after retries")


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.create_tables([TimelinePost])

from app import routes
