#!/bin/bash

source ./utils.sh


main() {
    read -p "Enter the name of the repo side you want to deploy (1 for ETL, 2 For App, 3 for UI, all): " repo_side
    if [[ $repo_side == "all" ]]; then
        source ./UI.sh ./App.sh ./ETL.sh
        processUI
        processApp
        processETL
    else
        IFS=',' read -ra all_reports <<< "$repo_side"
        coloredEcho "red" "You selected ${all_reports[@]}"
        for each in "${all_reports[@]}"; do
            if [[ $each == '1' ]]; then
                source ./ETL.sh
                processETL
            fi
            if [[ $each == '2' ]]; then
                source ./App.sh
                source ./UI.sh
                processUI
                processApp
                rm -rf "$RELEASE_DIR"/"UI"-v${VERSION}.zip
            fi
            if [[ $each == '3' ]]; then
                source ./UI.sh
                processUI
            fi
        done
    fi
}

initiate_build() { 
    main 
    cd api || exit
    python main.py
}

cleanup(){
    rm -rf build/App build/Frontend build/ETL release/*
}
