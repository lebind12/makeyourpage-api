import boto3, json

AWS_ACCESS_KEY = ""
AWS_SECRET_ACCESS_KEY = "",
REGION_NAME = "",

# with open('environment.json', 'r') as file : 
file = open('environment.json', 'r')
json_file = file.read()
json_file = json.loads(json_file)
AWS_ACCESS_KEY = json_file['ACCESS_CODE']
AWS_SECRET_ACCESS_KEY = json_file['SECRET_ACCESS_CODE']
REGION_NAME = json_file['REGION_NAME']
  

cognito = boto3.client('cognito-idp',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME
)

response = cognito.sign_up(
    ClientId = '1ktf35gclndhu0t3ulsfbpdgq3',
    Username = 'lebind12@naver.com',
    Password = 'Adizkahwm12!',
    ValidationData = [
        {
            'Name' : 'custom:textvalue',
            'Value' : '1234'
        }
    ]
)

print(response)