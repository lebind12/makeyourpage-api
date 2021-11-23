from chalice import Chalice
from chalice.app import NotFoundError, Response
from chalicelib import db_connect, export, CRUD, cognito
from chalicelib import send_message
import json, os

app = Chalice(app_name='makeyourpage-api')


# 템플릿 CRUD
#######################################################################
# Template Save, get, list, export
@app.route('/template/{template_id}', methods=["PUT", "GET", "POST"], cors=True)
def save_update(template_id):
    method = app.current_request.method
    json_body = app.current_request.json_body
    if method == 'PUT' : 
        # 이미 존재하는 템플릿인 경우 update
        if db_connect.connection().find_one({"template_id" : json_body['template_id']}) :
            CRUD.update_template(template_id, json_body)
            return {'status': 'success'}
        # 없는 템플릿인 경우 save
        else :
            CRUD.save_template(json_body)
            return {'status': 'success'}

    elif method == 'GET' : 
        return CRUD.get_template(template_id)
    
    elif method == 'POST' : 
        request_data = app.current_request
        clientName = request_data.json_body['client']
        html_str = request_data.json_body['htmlFile']
        export.export_html(html_str, clientName, template_id)
        return {'template_id': template_id}

# Template list
@app.route('/template/list/{user_id}', methods=["GET"], cors=True)
def template_list(user_id):
    return CRUD.template_list(user_id)

#######################################################################

# 회원가입
#######################################################################
# signup
@app.route('/subscription/signup', methods=['POST'], cors=True)
def signup():
    request_data = app.current_request
    json_body = request_data.json_body
    return cognito.sign_up(json_body)

# verificode
@app.route('/subscription/verificode', methods=['POST'], cors=True)
def verification():
    request_data = app.current_request
    json_body = request_data.json_body
    return cognito.verificode(json_body)


#######################################################################
# contact 메일 보내는 함수
@app.route('/contactmail', methods=['POST'], cors=True)
def post_mail():
    request = app.current_request
    data = request.json_body

    try:
        subject = data['subject']
        address = data['address']
        content = data['content']
    except KeyError:
        raise NotFoundError()

    try:
        with open(os.path.dirname(os.path.realpath(__file__))+'/chalicelib/environment.json', 'r', encoding="UTF-8") as in_file:
            config = json.load(in_file)
            data['host_address'] = config['HOST_ADDRESS']
            data['host_password'] = config['HOST_PASSWORD']
    except KeyError:
        raise FileNotFoundError()

    send_message.send_mail(data)
    return Response(status_code=200, body={"message": "success"})
