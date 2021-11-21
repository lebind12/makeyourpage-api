from . import db_connect

def delete_template(templateId) : 
    db = db_connect.connection()
    db['dev'].delete_one({"templateId" : templateId})