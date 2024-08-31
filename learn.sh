#!/bin/bash
# load constants
source ./constants.sh



function foo ()
{
    echo "Arguments work just like script arguments: $*"
    echo "And: $1 $2..."
    echo "This is a function"
    returnValue=0    # Variable values can be returned
    return $returnValue
}



FILE=`zenity --multiple --file-selection --title="Select a File"`

case $? in
         0)
                echo "\"$FILE\" selected.";;
         1)
                echo "No file selected.";;
        -1)
                echo "An unexpected error has occurred.";;
esac




