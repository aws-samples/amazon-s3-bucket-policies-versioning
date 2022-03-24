from schema.aws.s3.awsapicallviacloudtrail import Marshaller
from schema.aws.s3.awsapicallviacloudtrail import AWSEvent
from schema.aws.s3.awsapicallviacloudtrail import AWSAPICallViaCloudTrail
import boto3
import os
import hashlib
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def lambda_handler(event, context):
    db_table = os.environ.get('DDB_TABLE')
    db = boto3.client('dynamodb')

    # Deserialize event into strongly typed object
    aws_event: AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    detail: AWSAPICallViaCloudTrail = aws_event.detail

    if detail.errorCode:
        logger.error(f"Invalid request for bucket {detail.requestParameters.bucketName} at {str(detail.eventTime)}")
        logger.error(f"Reason: {detail.errorMessage}")
        raise Exception(f"Invalid request: {detail.errorMessage}")

    bucket_policy = json.dumps(event['detail']['requestParameters']['bucketPolicy'])

    # Using the md5 hash code of the bucket policy to identify uniquely the bucket policy
    hash_code = hashlib.md5(bucket_policy.encode()).hexdigest()

    logger.info(f"Bucket name: {detail.requestParameters.bucketName}")
    logger.info(f"Time: {str(detail.eventTime)}")
    logger.info(bucket_policy)

    ddb = boto3.client('dynamodb')
    ddb.put_item(TableName=db_table,
                 Item={'BucketName': {'S': detail.requestParameters.bucketName},
                       'Timestamp': {'S': str(detail.eventTime)},
                       'BucketPolicy': {'S': bucket_policy},
                       'BucketPolicyHash': {'S': hash_code},
                       'UserIdentity': {'S': str(detail.userIdentity)},
                       })

    return Marshaller.marshall(aws_event)
