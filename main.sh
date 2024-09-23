#!/bin/bash

# Function to display usage instructions
usage()
{
    echo "To see the answer of year 20XX, follow this syntax:"
    echo "Possible options are:"
    echo "    -h: get help information"
    echo "    -y <yearNumber>: Display the answer for year yearNumber."
    echo "       yearNumber must be between 2015 and 2023 included."
    echo
}

# Ensure we return to the original directory after script execution
trap "cd $(pwd)" EXIT

# Check scripts arguments.
while getopts "hy:" OPT; do
    case "${OPT}" in
        h)  # The user wants help
            usage
            exit 0
            ;;
        
        y)  # Check the year identifier       
            if [[ "$OPTARG" -le 2014 || "$OPTARG" -ge 2024 ]]; then
                echo "Year must be between 2015 and 2023."
                exit 1
            fi
            
            # Handling year-specific logic
            case "$OPTARG" in
                2015)
                    echo "Solution for Year 2015 is done in Python. Here is the solution for my input:"
                    echo
                    cd Solution2015 || { echo "Error: Could not change directory to Solution2015"; exit 1; }
                    python main.py
                    ;;
                
                2016)
                    echo "Solution for Year 2016 is done in Java. Here is the solution for my input:"
                    echo
                    cd Solution2016 || { echo "Error: Could not change directory to Solution2016"; exit 1; }
                    javac -d . *.java
                    if [ $? -eq 0 ]; then
                        java Solution2016.Main
                    else
                        echo "Compilation failed."
                    fi
                    cd ..
                    ;;
                
                *)
                    echo "Solution for year $OPTARG is not done yet."
                    ;;
            esac
            ;;
        
        *)  # Invalid option
            echo "You did not provide a valid option. Use -h for help."
            exit 1
            ;;
    esac
done

# If no arguments are provided, show usage.
if [ $# -eq 0 ]; then
    usage
fi
