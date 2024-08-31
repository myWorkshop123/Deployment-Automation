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


#TODO 
file_from="3/dist_equity/preview.html"
file_to="2/apps/templates/pages/generic/generic_page.html"
cat $file_from > $file_to


