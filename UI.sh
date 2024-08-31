
# CONSTANTS
source ./constants.sh

# UTILS
source ./utils.sh

# HELPERS 
source ./helper.sh

processUI() {
    coloredEcho "red" "Processing UI" 
    unzipFolder 3
    sed  -i '' "s/buildversion=[^>]*/buildversion=\"v$VERSION\"/g" $UI_INDEX_HTML $UI_PREVIEW_HTML
    zipFolder "${FOLDER_ZIP_TO[3]}" 'UI'
}



