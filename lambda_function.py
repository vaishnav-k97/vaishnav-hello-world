import json
import boto3
import botocore
import logging
logging.getLogger().setLevel(logging.INFO)
    
BUCKET_NAME ='dev-days-test'
KEY ="hello.txt"
s3 =boto3.resource('s3')
def lambda_handler(event, context):
    logging.info(event)
    
    
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY,'/tmp/hello_local.txt')
        temp_file="/tmp/hello_local.txt"
        f = open(temp_file, "r")

    except botocore.exceptions.ClientError as e:
        file open
        if e.response['Error']['Code'] == '404':
            print(" The object does not exist")
        else:
            raise
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': file.read()
    }
