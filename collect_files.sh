#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <input_dir> <output_dir>"
    exit 1
fi

input_dir=$1
output_dir=$2

if [ ! -d "$input_dir" ]; then
    echo "Input directory does not exist"
    exit 1
fi

if [ ! -d "$output_dir" ]; then
    echo "Output directory does not exist"
    exit 1
fi

find "$input_dir" -type f -exec cp {} "$output_dir" \;

echo "Files copied successfully"

лпрпропро
