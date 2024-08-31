# CONSTANTS
source ./constants.sh

# UTILS
source ./utils.sh

# HELPERS 
source ./helper.sh


processETL() {

    unzipFolder 2

    echo $VERSION_KEY > $ETL_VERSION_HTML

    removeDependencies 'ETL'
        
    zipFolder "${FOLDER_ZIP_TO[2]}" 'ETL'

}

