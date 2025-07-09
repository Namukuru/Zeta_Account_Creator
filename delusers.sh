#!/bin/bash

target_gid=150

# Loop through all users in /etc/passwd
while IFS=: read -r username _ uid gid _ _ _; do
    if [ "$gid" -eq "$target_gid" ]; then
        echo "Deleting user: $username"
        sudo userdel -r "$username"
    fi
done < /etc/passwd

