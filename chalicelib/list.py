from . import db_connect

def template_list(userId) :
    db = db_connect.connection()
    db['dev'].find({"userId" : userId})
