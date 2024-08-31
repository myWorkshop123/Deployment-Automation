#!/bin/bash

VERSION='30.1.1'

ROOT_DIR=$(pwd)

BUILD_DIR="${ROOT_DIR}/build"
RELEASE_DIR="${ROOT_DIR}/release"

APP_DIR="App-package.zip"
ETL_DIR="ETL-package.zip"
FRONTEND_DIR="Frontend-archive.zip"

declare -a FOLDER_ZIP_FROM=(
    [1]="${BUILD_DIR}/${APP_DIR}"
    [2]="${BUILD_DIR}/${ETL_DIR}"
    [3]="${BUILD_DIR}/${FRONTEND_DIR}"
)

declare -a FOLDER_ZIP_TO=(
    [1]="${BUILD_DIR}/App"
    [2]="${BUILD_DIR}/ETL"
    [3]="${BUILD_DIR}/Frontend"
)

VERSION_KEY="v${VERSION}"

# UI Constants
UI_PREVIEW_HTML="${FOLDER_ZIP_TO[3]}/dist_equity/preview.html"
UI_INDEX_HTML="${FOLDER_ZIP_TO[3]}/dist_equity/index.html"

# App Constants
APP_GENERIC_HTML="${FOLDER_ZIP_TO[1]}/apps/templates/pages/generic/generic_page.html"
APP_VERSION_HTML="${FOLDER_ZIP_TO[1]}/apps/templates/version.html"

# ETL Constants
ETL_VERSION_HTML="${FOLDER_ZIP_TO[2]}/etl/templates/version.html"