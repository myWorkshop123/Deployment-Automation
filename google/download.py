

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from connect import credentials
# If modifying these scopes, delete the file token.json.

files = [
  'JIRA DUMP',
  'Testcases-v23.2.1'
]
from download_files import export_xlsx
def main():
  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """

  creds = credentials()
  try:
    service = build("drive", "v3", credentials=creds)

    # Call the Drive v3 API
    results = (
        service.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])
    if not items:
      print("No files found.")
      return
    print("Files:")
    for item in items:
      if item['name'] in files:
        export_xlsx(real_file_id=item['id'], file_name=f"{item['name']}.xlsx")

      print(f"{item['name']} ({item['id']})")
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()