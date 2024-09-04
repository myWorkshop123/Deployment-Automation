import logging
import os

import boto3
import constant
from botocore.errorfactory import ClientError


class S3_Utility:
    """
    S3 utility Class
    """

    def __init__(self):
        self.aws_access_key = constant.AWS_ACCESS_KEY_ID
        self.aws_secret_access_key = constant.AWS_SECRET_ACCESS_KEY
        self.aws_bucket_name = constant.AWS_STORAGE_BUCKET_NAME
        self.region_name = constant.AWS_DEFAULT_REGION

        self.connection_formed = False
        try:
            self.s3_connection_obj = boto3.client(
                "s3",
                region_name=self.region_name,
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_access_key,
            )

            # resource
            self.s3res = boto3.resource(
                "s3",
                region_name=self.region_name,
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_access_key,
            )

            self.connection_formed = True

        except Exception as s3_connection_error:
            logging.error(
                "Exception {err}, occurred while making connection to S3. Connection formed: {}".format(
                    err=s3_connection_error
                )
            )

    def upload_directory(self, local_directory, s3_folder):
        """
        Uploads all files from a local directory to the specified folder in the S3 bucket.

        :param local_directory: Path to the local directory to upload files from.
        :param s3_folder: The folder (prefix) in the S3 bucket where files should be uploaded.
        """
        if not self.connection_formed:
            logging.error("S3 connection not formed. Cannot upload files.")
            return

        # Iterate through the directory and upload each file
        for root, dirs, files in os.walk(local_directory):
            for filename in files:
                if filename in [".DS_Store"]:
                    continue
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, local_directory)
                s3_key = os.path.join(s3_folder, relative_path).replace(
                    "\\", "/"
                )  # Ensure S3 key uses forward slashes

                try:
                    self.s3res.Bucket(self.aws_bucket_name).upload_file(
                        local_path, s3_key
                    )
                    logging.info(
                        f"Uploaded {local_path} to s3://{self.aws_bucket_name}/{s3_key}"
                    )
                except ClientError as e:
                    logging.error(f"Failed to upload {local_path} to S3: {e}")
