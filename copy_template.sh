#!/bin/bash

# Get the current year
current_year=$(date +%Y)

# Prompt for the year
read -p "Enter the year (default: $current_year): " year
year=${year:-$current_year}

# Prompt for the number
read -p "Enter the day: " day

# Create the year directory if it doesn't exist
if [ ! -d "$year" ]; then
  mkdir "$year"
fi

# Create the numbered directory
mkdir "$year/$day"

# Copy the files from the template directory
cp -r _template/* "$year/$day"

echo "Files copied to $year/$day"