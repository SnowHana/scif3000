#!/bin/bash

# The URL of the CSV file
url="https://opennem.org.au/energy/nem/?range=7d&interval=30m&format=csv"

# Use curl to download the CSV file and save it locally
curl -o energy_data.csv "$url"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "CSV file downloaded successfully."
else
  echo "Failed to download the CSV file."
fi
