import db_connect

def save_template(json_body):
    db = db_connect.connection()
    db['dev'].insert_one(json_body)