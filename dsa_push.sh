#!/bin/bash

# Navigate to the project root (optional here but good practice)
cd "$(dirname "$0")"

# Ask user for commit message
echo "Enter commit message:"
read message

# Add all changes
git add .

# Commit the changes
git commit -m "$message"

# Push to GitHub (assuming your branch is 'main')
git push origin main

