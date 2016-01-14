from mongoengine import connect

def connect_db():
    connect('avatar', 
    host='mongodb://<username>:<pw><host>:<port>/<dbname>')
