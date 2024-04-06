#!/bin/bash

original_log="/var/log/vmware-vmsvc-root.1.log"
backup_log="/var/log/messages.old"


if [ -f "$original_log" ]; then
    cp "$original_log" "$backup_log"
    > "$original_log"
    
    echo "Done"
else
    echo "Not Done"
fi

