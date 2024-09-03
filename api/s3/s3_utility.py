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

    def upload_file_to_s3(self, file_name_with_key_in_s3, local_file_path):
        """
        This function is to upload the file from local path to s3 path
        """
        try:
            session = self.create_session()
            s3_client = session.resource("s3")
            s3_client.Object(
                self.aws_bucket_name, file_name_with_key_in_s3
            ).upload_file(local_file_path)

        except:
            print("Error in uploading file to s3")

    def upload_files_to_s3(self, s3_file_key_path, local_file_path):
        """
        Upload Files to S3.
        This method upload files from local directory to a specified location in
        given S3 bucket.
        Arguments:
            key {string} -- s3 key of the folder where the files needs to stored.
            filepath {string} -- local path of file on the system/lambda.
        Usage:
            upload_files_to_s3(
                file_body=b'bytes'|file,
                key='s3-file-key',
            )
        Raises:
            s3_error: An error occurred while interacting with S3 boto APIs.
        """
        try:
            self.s3_connection_obj.upload_file(
                local_file_path, self.aws_bucket_name, s3_file_key_path
            )
            logging.info(
                "Copying file {} at {}".format(local_file_path, s3_file_key_path)
            )
        except Exception as s3_error:
            logging.error(
                "Exception {} occurred while writing file to S3! - filepath in server {}".format(
                    s3_error, local_file_path
                )
            )
            raise s3_error

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

    def check_if_file_exists_on_s3(self, file_name):
        """Function to check if file exists on the server
        INPUT:
            bucket_name - bucket_name
            file_name - file_name to search
        Returns True if file exists
        """
        try:
            logging.info(
                f"Checking in the bucket ->{self.aws_bucket_name},for the key->{file_name}"
            )
            result = self.s3_connection_obj.list_objects_v2(
                Bucket=self.aws_bucket_name, Prefix=file_name
            )
            if "Contents" in result:
                return True
            else:
                return False
        except ClientError as e:
            logging.error(f"Error -> {e} occurred")
            return False

    def read_contents_from_file(self, file_path_key_in_s3):
        """function to read the contents from the file stored in s3 path"""

        try:
            # check if the file exists
            res = self.check_if_file_exists_on_s3(file_path_key_in_s3)
            if res is not False:
                fileobj = self.s3_connection_obj.get_object(
                    Bucket=self.aws_bucket_name, Key=file_path_key_in_s3
                )
                return fileobj["Body"].read()
            else:
                logging.error("File not found in S3!")

            return ""

        except Exception as s3_error:
            logging.error(
                "Exception {} occurred reading the file from S3!".format(s3_error)
            )

            raise s3_error

    def download_files_from_s3(self, s3_file_key_path, local_file_path):
        """
        Download Files from S3.
        This method is used to download files from as specified location in S3 bucket
        and store it locally.
        Arguments:
            key {string} -- s3 key of the folder where the files needs to stored.
            local_filepath {string} -- local path of file on the system/lambda.
        Usage:
            download_files_from_s3(
                key='s3-file-key',
                local_filepath='/User/localuser/work_folder/file_name.extension'
            )
        Raises:
            s3_error: An error occurred while interacting with S3 boto APIs.
        """
        try:
            self.s3_connection_obj.download_file(
                self.aws_bucket_name, s3_file_key_path, local_file_path
            )
        except Exception as s3_error:
            logging.error(
                "Exception {}, occurred while downloading the file {}".format(
                    s3_error, s3_file_key_path
                )
            )
            raise s3_error
