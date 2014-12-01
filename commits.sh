#!/bin/bash

# Set the start date
START_DATE="2014-12-01"

# Convert start date to seconds since epoch
START_DATE_EPOCH=$(date -d "$START_DATE" +%s)

# Total number of commits
TOTAL_COMMITS=$(git rev-list --count HEAD)

# Number of commits per day
COMMITS_PER_DAY=10

# Generate a list of dates to be used
DATES=()
CURRENT_DATE_EPOCH=$START_DATE_EPOCH
while [ $TOTAL_COMMITS -gt 0 ]; do
    DATE=$(date -d "@$CURRENT_DATE_EPOCH" +%Y-%m-%d)
    DATES+=($DATE)
    CURRENT_DATE_EPOCH=$(( CURRENT_DATE_EPOCH + 86400 ))  # Increment by one day (86400 seconds)
    TOTAL_COMMITS=$(( TOTAL_COMMITS - COMMITS_PER_DAY ))
done

# Reverse the list to distribute commits from start to end
DATES=($(printf "%s\n" "${DATES[@]}" | tac))

# Check if git is in the middle of an operation and clean up if necessary
if [ -d ".git/rebase-apply" ] || [ -d ".git/rebase-merge" ] || [ -f ".git/CHERRY_PICK_HEAD" ]; then
    echo "Cleaning up previous rebase or cherry-pick state."
    git rebase --abort || git cherry-pick --abort
fi

# Cleanup any existing filter branch state
cleanup_filters() {
    rm -rf .git-rewrite
}

# Amend commit dates using filter-branch
COMMIT_COUNT=0
git filter-branch --env-filter '
    export GIT_COMMITTER_DATE
    export GIT_AUTHOR_DATE

    # Increment commit count for each commit
    COMMIT_COUNT=$((COMMIT_COUNT + 1))

    # Get the correct date for this commit
    DATE_INDEX=$((COMMIT_COUNT / '"$COMMITS_PER_DAY"'))
    DATE='"${DATES[$DATE_INDEX]}"'

    # Calculate random time between 8:00 AM and 8:00 PM
    TIME_HOUR=$((8 + RANDOM % 12))
    TIME_MINUTE=$((RANDOM % 60))
    TIME=$(printf "%02d:%02d:00" $TIME_HOUR $TIME_MINUTE)

    # Apply new commit date and time
    GIT_COMMITTER_DATE="$DATE $TIME"
    GIT_AUTHOR_DATE="$DATE $TIME"
' -- --all

cleanup_filters

echo "Commit dates have been redistributed."

# Ensure to run the following command to push changes
# git push --force
