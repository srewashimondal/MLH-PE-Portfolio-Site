from flask import Flask
from peewee import *
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
app = Flask(__name__)
from app import routes 

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
        
mydb.connect()
mydb.create_tables([TimelinePost])
