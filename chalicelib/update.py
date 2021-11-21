from . import db_connect

def update_template(templateId, json_body) : 
    db = db_connect.connection()
    db['dev'].update_one({"templateId" : templateId}, json_body)