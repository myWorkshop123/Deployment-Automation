#!/bin/bash

VERSION='26.4.0'
declare -a folder_zip=(
    [1]="ETL-package.zip"
    [2]="App-package.zip"
    [3]="Frontend-archive.zip"
)

# App Constants
APP_PREVIEW_HTML="3/dist_equity/preview.html"
APP_GENERIC_HTML="2/apps/templates/pages/generic/generic_page.html"
APP_VERSION_HTML="2/apps/templates/version.html"
