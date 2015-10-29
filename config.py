from mongoengine import connect

def connect_db():
    connect('avatar', 
    host='mongodb://avataru:q1w2e3r4@ds039484.mongolab.com:39484/avatar')
