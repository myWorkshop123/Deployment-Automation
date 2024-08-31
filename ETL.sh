# CONSTANTS
source ./constants.sh

# UTILS
source ./utils.sh

# HELPERS 
source ./helper.sh


processETL() {
    # unzip the Frontend-archive.zip and store it in 3
    unzip "${folder_zip[1]}" -d 1

    # update the package version
    # echo "buildversion=\"$VERSION\""

    echo "v${VERSION}" > 1/etl/templates/version.html 

    read -p "ETL Select the dependencies folder to remove (1 for os, 2 for pip , 3 for all)" dep_folder
    
    removeDependencies 'ETL'
    
    cd 1/

    zip -r ../final/ETL-v${VERSION}.zip * -x ${folder_zip[1]} .DS_Store

}

