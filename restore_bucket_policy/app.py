import boto3
import os
import hashlib
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def lambda_handler(event, context):
    db_table = os.getenv('DDB_TABLE')
    if 'BucketPolicyHash' in event and event['BucketPolicyHash'] != '':
        bucket_policy_hash = event['BucketPolicyHash'].strip()
        s3 = boto3.client('s3')
        ddb = boto3.client('dynamodb')
        resp = ddb.query(
            TableName=db_table,
            ExpressionAttributeValues={
                ':BucketPolicyHash': {
                    'S': bucket_policy_hash,
                },
            },
            KeyConditionExpression='BucketPolicyHash = :BucketPolicyHash',
        )
        if len(resp['Items']) > 0:
            bucket_name = resp['Items'][0]['BucketName']['S']
            bucket_policy = resp['Items'][0]['BucketPolicy']['S']
            hash_code = hashlib.md5(bucket_policy.encode()).hexdigest()
            if hash_code != bucket_policy_hash:
                raise Exception('The BucketPolicy for the given BucketPolicyHash is corrupted.')
            timestamp = resp['Items'][0]['Timestamp']['S']
            logger.info(f"{timestamp}: Executing api PutBucketPolicy on bucket {bucket_name} :")
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            logger.info(bucket_policy)
            logger.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            try:
                s3.put_bucket_policy(
                    Bucket=bucket_name,
                    Policy=bucket_policy)
            except ClientError as e:
                raise Exception(e.response['Error'])
        else:
            raise Exception(f'Cannot find provided BucketPolicyHash code in DynamoDB table {db_table}')
        return {'message': f'Bucket policy has been restored: {bucket_policy_hash}'}
    else:
        raise Exception('Provide an event with a valid BucketPolicyHash code')

