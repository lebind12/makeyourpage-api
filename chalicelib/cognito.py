import boto3, json, os

def get_cognito_client() :
    aws_data = dict()
    with open(os.path.dirname(os.path.realpath(__file__))+'/environment.json', 'r') as file : 
        json_file = file.read()
        json_file = json.loads(json_file)
        aws_data['AWS_ACCESS_KEY'] = json_file['ACCESS_CODE']
        aws_data['AWS_SECRET_ACCESS_KEY'] = json_file['SECRET_ACCESS_CODE']
        aws_data['REGION_NAME'] = json_file['REGION_NAME']
        aws_data['APP_CLIENT_ID'] = json_file['APP_CLIENT_ID']
    
    cognito = boto3.client('cognito-idp',
        aws_access_key_id = aws_data['AWS_ACCESS_KEY'],
        aws_secret_access_key = aws_data['AWS_SECRET_ACCESS_KEY'],
        region_name = aws_data['REGION_NAME']
    )
    return cognito, aws_data

def sign_up(json_body) : 
    username = json_body['username']
    password = json_body['password']
    cognito, aws_data = get_cognito_client()

    response = cognito.sign_up(ClientId=aws_data['APP_CLIENT_ID'],
                                Username=username,
                                Password=password,
                                UserAttributes=[{
                                    'Name' : 'email',
                                    'Value' : username
                                }])
    return (response)

def verificode(json_body) : 
    usermail = json_body['usermail']
    code = json_body['code']
    cognito, aws_data = get_cognito_client()
    response = cognito.confirm_sign_up(ClientId=aws_data['APP_CLIENT_ID'],
                                    Username=usermail,
                                    ConfirmationCode=code)

    return (response)