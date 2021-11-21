from . import db_connect

def save_template(json_body):
    db = db_connect.connection()
    db['dev'].insert_one(json_body)

def get_template(templateId) : 
    db = db_connect.connection()
    return db['dev'].find_one({"template_id" : templateId}, {"_id" : 0})

def template_list(userId) :
    db = db_connect.connection()
    document_list = list()
    return_data = dict()
    documents = db['dev'].find({"userId" : userId}, {"_id" : 0})
    for data in documents : 
        document_list.append(data)
    return_data['templates'] = document_list
    return return_data

def update_template(templateId, json_body) : 
    db = db_connect.connection()
    db['dev'].replace_one({"template_id" : templateId}, json_body)