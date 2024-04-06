#!/bin/bash

original_log="/var/log/vmware-vmsvc-root.1.log"
backup_log="/var/log/messages.old"




spin() {
    if [ -f "$backup_log" ]; then
    
        mv "$backup_log"{,-$(date +%Y%m%d%H%M%S)}
    fi
}


spin


if [ -f "$original_log" ]; then
    cp "$original_log" "$backup_log" && > "$original_log" && echo "Done" || echo "Not Done"
else
    echo "Not Done"
fi
find /var/log/ -type f | grep $(date -d "yesterday" "+%Y%m%d%H") | xargs rm -f
