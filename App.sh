# CONSTANTS
source ./constants.sh

# UTILS
source ./utils.sh

# HELPERS 
source ./helper.sh



processApp() {
    # unzip the Frontend-archive.zip and store it in 3
    coloredEcho "green" "Processing App"
    unzip "${folder_zip[2]}" -d 2

    # update the package version
    echo "v${VERSION}"  > $APP_VERSION_HTML

    cat $APP_PREVIEW_HTML > $APP_GENERIC_HTML

    removeDependencies 'App'

    cd 2/

    zip -r ../final/App-v${VERSION}.zip * -x ${folder_zip[2]} .DS_Store

    cd ..

}

