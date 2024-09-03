import io

from connect import credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


def get_files(folder_id):
    creds = credentials()
    query = f"'{folder_id}' in parents and trashed = false"
    try:
        service = build("drive", "v3", credentials=creds)
        results = (
            service.files()
            .list(q=query, pageSize=10, fields="nextPageToken, files(id, name)")
            .execute()
        )
        items = results.get("files", [])
        return items
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []


def export_file(real_file_id, file_name, path, file_type):
    creds = credentials()

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        request = service.files().export_media(fileId=file_id, mimeType=file_type)
        file = io.FileIO(path + "/" + file_name, mode="wb")
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}.")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None
