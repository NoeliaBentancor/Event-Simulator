import logging
import boto3
from botocore.exceptions import ClientError
import os


class S3UPloader:

    async def upload_file(self,file_name, object_name=None):
        s3_client = boto3.client(
            os.getenv("AWS_SERVICE"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEYS"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEYS"),
        )
        if object_name is None:
            object_name = file_name
        try:
            s3_client.upload_file(file_name, os.getenv("S3_BUCKET"), object_name)
        except ClientError as e:
            logging.error(e)
