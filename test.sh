#!/bin/bash

# Start date
start_date="2014-12-01"
# Number of commits per day
commits_per_day=10
# Start time (in seconds after 00:00:00)
start_time=28800 # 08:00:00 in seconds
end_time=72000   # 20:00:00 in seconds

# Convert start_date to seconds since epoch
start_date_epoch=$(date -d "$start_date" +%s)

# Get all files in the project directory
files=$(find . -type f)

# Initialize commit index
commit_index=0

# Iterate over each file
for file in $files; do
    # Check if the file is already staged
    if git ls-files --stage | grep -q "$(basename "$file")"; then
        echo "File '$file' is already staged."
    else
        # Stage the file
        git add "$file"
        echo "Staging file '$file'."
    fi

    # Calculate the commit date and time
    current_date_epoch=$((start_date_epoch + (commit_index / commits_per_day) * 86400))
    commit_date=$(date -d "@$current_date_epoch" +%Y-%m-%d)

    # Calculate time of day
    seconds_since_start_of_day=$(( (commit_index % commits_per_day) * (end_time - start_time) / (commits_per_day - 1) + start_time ))
    commit_time=$(date -d "@$seconds_since_start_of_day" +%H:%M:%S)

    # Create a commit message
    commit_message="[ADD] $(basename "$file")"

    # Commit with the calculated date and time
    GIT_AUTHOR_DATE="$commit_date $commit_time" GIT_COMMITTER_DATE="$commit_date $commit_time" git commit -m "$commit_message"

    # Increment commit index
    commit_index=$((commit_index + 1))
done

echo "Finished committing all files."
