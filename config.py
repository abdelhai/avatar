from mongoengine import connect
import os

mongo_host = os.environ.get('MONGO_HOST')

def connect_db():
    connect('avatar', 
    host=mongo_host)
