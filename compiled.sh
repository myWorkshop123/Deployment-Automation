#!/bin/bash
main() {
    read -p "Enter the name of the repo side you want to deploy (1 for ETL, 2 For App, 3 for UI, all): " repo_side
    if [[ $repo_side == "all" ]]; then
        source ./UI.sh ./App.sh ./ETL.sh
        processUI
        processApp
        processETL
    else
        IFS=',' read -ra all_reports <<< "$repo_side"
        echo "You selected ${all_reports[@]}"
        for each in "${all_reports[@]}"; do
            if [[ $each == '1' ]]; then
                source ./ETL.sh
                processETL
            fi
            if [[ $each == '2' ]]; then
                source ./App.sh
                processApp
            fi
            if [[ $each == '3' ]]; then
                source ./UI.sh
                processUI
            fi
        done
    fi
}

cleanup(){
    rm -rf build/App build/Frontend build/ETL release/*
}