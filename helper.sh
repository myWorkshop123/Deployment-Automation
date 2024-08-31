

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
