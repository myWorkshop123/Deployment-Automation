
# CONSTANTS
source ./constants.sh

# UTILS
source ./utils.sh

# HELPERS 
source ./helper.sh

processUI() {
    coloredEcho "red" "Processing UI" 
    # unzip the Frontend-archive.zip and store it in 3
    unzip "${folder_zip[3]}" -d 3

    # new commands 
    sed  -i '' "s/buildversion=[^>]*/buildversion=\"v$VERSION\"/g" 3/dist_equity/index.html 3/dist_equity/preview.html

    cd 3/ 

    zip -r ../final/UI-v${VERSION}.zip * -x ${folder_zip[3]} .DS_Store

    cd ..

}

