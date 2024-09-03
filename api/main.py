import constant
from download_files import export_file, get_files
from s3.s3_utility import S3_Utility


def upload_release_files_to_s3():
    s3 = S3_Utility()
    s3.upload_directory(constant.RELEASE_DIR, constant.BUILD_FOLDER_S3_LOCATION)
    print("done")


def main():

    release_folder_id = None
    build_folders = get_files(constant.GOOGLE_DRIVE_FOLDER_ID)
    for each in build_folders:
        if each["name"] == f"{constant.GOOGLE_DRIVE_BUILD_FOLDER}-v{constant.VERSION}":
            release_folder_id = each["id"]
            break

    build_files = get_files(release_folder_id)

    for each in build_files:
        if each["name"] in constant.FILES.keys():
            export_file(
                each["id"],
                constant.FILES[each["name"]]["filename"],
                constant.RELEASE_DIR,
                constant.FILES[each["name"]]["type"],
            )


if __name__ == "__main__":
    # main()
    upload_release_files_to_s3()
