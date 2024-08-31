#!/bin/bash 



# Function to print colored text
coloredEcho() {
  # eg: coloredEcho "red" "Processing UI" 

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
