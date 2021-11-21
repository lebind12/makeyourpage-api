from chalice import Chalice
from chalice.app import NotFoundError, Response
from chalicelib import db_connect, export, CRUD, cognito
from chalicelib import send_message
import json

app = Chalice(app_name='makeyourpage-api')


# 템플릿 CRUD
#######################################################################
# Temaplate Export
@app.route('/template/export', methods=["POST"], cors=True)
def template_export():
    request_data = app.current_request
    clientName = request_data.json_body['client']
    html_str = request_data.json_body['htmlFile']
    template_id = request_data.json_body['template_id']

    export.export_html(html_str, clientName, template_id)
    return {'template_id': template_id}

# Template Save
@app.route('/template/save', methods=["PUT"], cors=True)
def template_save():
    request_data = app.current_request
    json_body = request_data.json_body
    CRUD.save_template(json_body)
    return {'status': 'success'}

# Template list
@app.route('/template/list/{user_id}', methods=["GET"], cors=True)
def template_list(user_id):
    return CRUD.template_list(user_id)

# Template get data
@app.route('/template/get/{template_id}', methods=['GET'], cors=True)
def template_get(template_id):
    return CRUD.get_template(template_id)

# Template Update
@app.route('/template/update/{template_id}', methods=['PUT'], cors=True)
def template_update(template_id):
    request_data = app.current_request
    json_body = request_data.json_body
    CRUD.update_template(template_id, json_body)
    return {'status': 'success'}
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
        with open('config.json', 'r', encoding="UTF-8") as in_file:
            config = json.load(in_file)
            data['host_address'] = config['HOST_ADDRESS']
            data['host_password'] = config['HOST_PASSWORD']
    except KeyError:
        raise FileNotFoundError()

    send_message.sendMail(data)
    return Response(status_code=200, body={"message": "success"})
