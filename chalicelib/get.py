from . import db_connect

def get_template(templateId) : 
    db = db_connect.connection()
    db['dev'].find_one({"templateId" : templateId})