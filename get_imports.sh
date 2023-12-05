#!/bin/bash

OUTPUT_FILE="all_imports.txt"

# Function to process a file and extract unique imports
process_file() {
    local file="$1"
    echo "Processing file: $file"

    # Use Python to parse the import statements and append to the output file
    python3 <<END_PYTHON >> "$OUTPUT_FILE"
import ast

def extract_imports(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tree = ast.parse(content)

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module_name = node.module
            for alias in node.names:
                imports.add(f"{module_name}.{alias.name}")

    for imp in sorted(imports):
        print(imp)

extract_imports("$file")
END_PYTHON

    echo "-----------------------------"
}

# Function to process all files in a directory
process_directory() {
    local dir="$1"

    # Loop through all files and directories in the current directory
    for entry in "$dir"/*; do
        if [ -f "$entry" ]; then
            # If the entry is a file, process it
            if [[ "$entry" == *.py ]]; then
                process_file "$entry"
            fi
        elif [ -d "$entry" ]; then
            # If the entry is a directory, recursively process it
            process_directory "$entry"
        fi
    done
}

# Main function
main() {
    local target_directory="$1"

    # Check if the target directory exists
    if [ ! -d "$target_directory" ]; then
        echo "Error: Directory '$target_directory' not found."
        exit 1
    fi

    # Remove existing output file if it exists
    rm -f "$OUTPUT_FILE"

    # Call the function to process the target directory
    process_directory "$target_directory"

    # Sort and get unique names
    sort -u -o "$OUTPUT_FILE" "$OUTPUT_FILE"

    echo "Output saved to $OUTPUT_FILE"
}

# Check if a directory is provided as an argument
if [ "$#" -eq 1 ]; then
    main "$1"
else
    echo "Usage: $0 <directory>"
    exit 1
fi
