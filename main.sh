#!/bin/bash

# Function used to display to the user how to use this script.
# USAGE: Called without argument.
usage()
{
    echo "To see the answer of year 20XX, follow this syntax:"
    echo "Possible options are:"
    echo "    -h: get help information"
    echo "    -y <yearNumber>: Display the answer for year yearNumber. yearNumber is between 2015 and 2023 included."
}

# Check scripts arguments.
while getopts "hy:" OPT
do
    case "${OPT}" in
        h)  # The user wants to see how to use this script.
            usage
            exit 0
            ;;
        
        y)  # Check the year identifier       
            
            # Don't do anything if the year number is invalid.
            if [[ "$OPTARG" -le 2014 || "$OPTARG" -ge 2024 ]]; then
                echo "Year must be between 2015 and 2023."
                exit 1
            fi
            
            # Launch the Python code for 2015.
            if [ "$OPTARG" == "2015" ]; then
                echo "Solution for Year 2015 are done in Python. Here is the solution for my input:"
                echo 
                echo 
                cd Solution2015
                python main.py
                cd ..
            elif [ "$OPTARG" == "2016" ]; then
                echo "Solution for Year 2015 are going to be done in Java."
            else
                echo "Solution for year $OPTARG is not done yet."
            fi
            ;;
        
        *)  # User did not give any year identifier.
            echo "You did not provide a year identifier. Use -h for help."
            exit 1
            ;;
    esac
done

# If no arguments are provided, show usage.
if [ $# -eq 0 ]; then
    usage
fi
