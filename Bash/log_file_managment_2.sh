#!/bin/bash

original_log="/var/log/vmware-vmsvc-root.1.log"
backup_log="/var/log/messages.old"


if [ -f "$original_log" ]; then
    cp "$original_log" "$backup_log"
    > "$original_log"
    
    echo "Enter Name"
    read name
    echo "Enter Country:"
    read country
    echo "Enter the age (numeric value):"
    read age
    
    if ! [[ "$age" =~ ^[0-9]+$ ]]; then
        echo "Age must be a numeric value."
        exit 1
    fi
    
    
    echo "Name:$name" >> /var/log/messages.old
    echo "Country:$country" >> /var/log/messages.old
    echo "Age:$age" >> /var/log/messages.old
    
    
    
    echo "Done"
else
    echo "Not Done"
fi
