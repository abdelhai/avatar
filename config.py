from mongoengine import connect

def connect_db():
    connect('avatar', 
    host='mongodb://avataru:<pw><host>:<port>/<dbname>')
