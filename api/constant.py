import os

from dotenv import load_dotenv

load_dotenv()


class CONSTANT:
    def __init__(self, value, description):
        self.value = value
        self.description = description


VERSION = CONSTANT(os.getenv("VERSION", False), "Version of the build").value
ROOT_DIR = CONSTANT(os.getenv("ROOT_DIR", False), "Location of the root dir").value
BUILD_DIR = CONSTANT(os.getenv("BUILD_DIR", False), "Location of the build dir").value
RELEASE_DIR = CONSTANT(
    os.getenv("RELEASE_DIR", False), "Location of the release dir"
).value

GOOGLE_DRIVE_FOLDER_ID = CONSTANT(
    "1yZEDI6jqwHw7Q1qxWPvYA3jqIPlgwxwe", "Google Drive Folder ID"
).value

GOOGLE_DRIVE_BUILD_FOLDER = CONSTANT(
    "BUILD_RELEASES", "Google Drive release folder name"
).value


JIRA_DUMP = CONSTANT("JIRA DUMP", "Name of the JIRA_DUMP file without extension").value
TESTCASES = CONSTANT("Testcases", "Name of the Testcases file without extension").value
DEPLOYMENT_DOC = CONSTANT(
    "DeploymentInstructions", "Name of the Testcases file without extension"
).value


# Google Drive API Constants
class EXPORT_FILE_TYPE(object):
    EXCEL = "xlsx"
    DOCX = "docx"


G_API_SCOPES = [
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive",
]


G_API_FILE_TYPE = {
    EXPORT_FILE_TYPE.EXCEL: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    EXPORT_FILE_TYPE.DOCX: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


FILES = {
    f"{JIRA_DUMP}-v{VERSION}": {
        "filename": f"{JIRA_DUMP}-v{VERSION}.{EXPORT_FILE_TYPE.EXCEL}",
        "type": G_API_FILE_TYPE[EXPORT_FILE_TYPE.EXCEL],
    },
    f"{TESTCASES}-v{VERSION}": {
        "filename": f"{TESTCASES}-v{VERSION}.{EXPORT_FILE_TYPE.EXCEL}",
        "type": G_API_FILE_TYPE[EXPORT_FILE_TYPE.EXCEL],
    },
    f"{DEPLOYMENT_DOC}-v{VERSION}": {
        "filename": f"{DEPLOYMENT_DOC}-v{VERSION}.{EXPORT_FILE_TYPE.DOCX}",
        "type": G_API_FILE_TYPE[EXPORT_FILE_TYPE.DOCX],
    },
}

# AWS S3 Constants
AWS_ACCESS_KEY_ID = CONSTANT(os.getenv("AWS_ACCESS_KEY_ID", ""), "AWS Access Key").value
AWS_SECRET_ACCESS_KEY = CONSTANT(
    os.getenv("AWS_SECRET_ACCESS_KEY", ""), "AWS Secret Access Key"
).value
AWS_STORAGE_BUCKET_NAME = CONSTANT(
    os.getenv("AWS_STORAGE_BUCKET_NAME", ""), "AWS Storage Bucket Name"
).value
AWS_DEFAULT_REGION = CONSTANT(
    os.getenv("AWS_DEFAULT_REGION", ""), "AWS Default Region"
).value

AWS_S3_ENDPOINT_URL = CONSTANT(
    os.getenv("AWS_S3_ENDPOINT_URL", ""), "AWS S3 Endpoint URL"
).value

AWS_DEFAULT_ACL = CONSTANT(
    os.getenv("AWS_DEFAULT_ACL", ""), "AWS S3 Endpoint URL"
).value


BUILD_FOLDER_S3_LOCATION = CONSTANT(
    "test-folder/", "Location of the build folder in S3"
).value


# Outlook Email Constants
class OUTLOOK(object):
    SMTP_SERVER = "smtp.office365.com"
    SMTP_PORT = 587
    SENDER_EMAIL = os.getenv("OUTLOOK_SENDER_EMAIL", "")
    SENDER_PASSWORD = os.getenv("OUTLOOK_SENDER_PASSWORD", "")
    RECEIEVER_EMAIL = ["kartik.kumar@galepartners.com"]
    CC_EMAIL = ["fushionblade888@gmail.com"]
