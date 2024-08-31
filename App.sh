# CONSTANTS
source ./constants.sh

# UTILS
source ./utils.sh

# HELPERS 
source ./helper.sh



processApp() {

    unzipFolder 1

    echo $VERSION_KEY  > $APP_VERSION_HTML

    cat $UI_PREVIEW_HTML > $APP_GENERIC_HTML

    removeDependencies 'App'

    zipFolder "${FOLDER_ZIP_TO[1]}" 'App'



}

