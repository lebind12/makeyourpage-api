import boto3
import json

AWS_ACCESS_KEY = ""
AWS_SECRET_ACCESS_KEY = "",
REGION_NAME = "",

def export_html(html_str, client_name, template_id) : 
  with open('environment.json', 'r') as file : 
    json_file = file.read()
    json_file = json.loads(json_file)
    AWS_ACCESS_KEY = json_file['ACCESS_CODE']
    AWS_SECRET_ACCESS_KEY = json_file['SECRET_ACCESS_CODE']
    REGION_NAME = json_file['REGION_NAME']
  s3 = boto3.client(
    's3', 
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME
  )
  s3.put_object(Body=html_str,
    Bucket='makeyourpage-test',
    Key= client_name + '/html/' + template_id + '.html',
    ACL='public-read',
    ContentType='text/html')