#!/bin/bash

# CONSTANTS
VERSION='26.4.0'
declare -a folder_zip=(
    [1]="ETL-package.zip"
    [2]="App-package.zip"
    [3]="Frontend-archive.zip"
)

# Function to print colored text
coloredEcho() {
  local color=$1
  local text=$2
  local reset='\033[0m'

  case $color in
    "black") color_code='\033[0;30m' ;;
    "red") color_code='\033[0;31m' ;;
    "green") color_code='\033[0;32m' ;;
    "yellow") color_code='\033[0;33m' ;;
    "blue") color_code='\033[0;34m' ;;
    "magenta") color_code='\033[0;35m' ;;
    "cyan") color_code='\033[0;36m' ;;
    "white") color_code='\033[0;37m' ;;
    *) color_code=$reset ;;  # Default to no color if an invalid color is passed
  esac

  echo -e "${color_code}${text}${reset}"
}

# Example usage

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

removeDependencies() {
    
    read -p "$1 Select the dependencies folder to remove (1 for os, 2 for pip , 3 for all)" dep_folder
    if [[ $1 == 'ETL' ]]; then
        if [[ $dep_folder == "1" ]]; then
            rm -rf 1/etl/Dependencies_os
        elif [[ $dep_folder == "2" ]]; then
            rm -rf 1/etl/Dependencies_pip
        elif [[ $dep_folder == "3" ]]; then
            rm -rf 1/etl/Dependencies_os 1/etl/Dependencies_pip
        fi
    elif [[ $1 == 'App' ]]; then
        if [[ $dep_folder == "1" ]]; then
            rm -rf 2/apps/Dependencies_os
        elif [[ $dep_folder == "2" ]]; then
            rm -rf 2/apps/Dependencies_pip
        elif [[ $dep_folder == "3" ]]; then
            rm -rf 2/apps/Dependencies_os 2/apps/Dependencies_pip
        fi
    fi 
}

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
processApp() {
    # unzip the Frontend-archive.zip and store it in 3
    unzip "${folder_zip[2]}" -d 2

    # update the package version
    echo "v${VERSION}"  > 2/apps/templates/version.html 

    cat 3/dist_equity/preview.html > 2/apps/templates/pages/generic/generic_page.html

    removeDependencies 'App'

    cd 2/

    zip -r ../final/App-v${VERSION}.zip * -x ${folder_zip[2]} .DS_Store

    cd ..

}

main() {
    read -p "Enter the name of the repo side you want to deploy (1 for ETL, 2 For App, 3 for UI, all): " repo_side
    if [[ $repo_side == "all" ]]; then
        processUI
        processApp
        processETL
    else
        IFS=',' read -ra all_reports <<< "$repo_side"
        echo "You selected ${all_reports[@]}"
        for each in "${all_reports[@]}"; do
            if [[ $each == '1' ]]; then
                processETL
            fi
            if [[ $each == '2' ]]; then
                processApp
            fi
            if [[ $each == '3' ]]; then
                processUI
            fi
        done
    fi
}

