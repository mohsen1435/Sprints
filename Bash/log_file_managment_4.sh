#!/bin/bash

original_log="/var/log/vmware-vmsvc-root.1.log"
backup_log="/var/log/messages.old"
report="/var/log/report.txt"


spin() {
    if [ -f "$backup_log" ]; then
        mv "$backup_log"{,-$(date +%Y%m%d%H%M%S)}
    fi
}


analyze_log() {
    error_count=$(grep -c "ERROR" "$backup_log")
    warning_count=$(grep -c "WARNING" "$backup_log")
    critical_events=$(grep -E "CRITICAL|FATAL" "$backup_log")

    echo "Log Analysis Report" > "$report"
    echo "===================" >> "$report"
    echo "Total Errors: $error_count" >> "$report"
    echo "Total Warnings: $warning_count" >> "$report"
    echo "" >> "$report"
    echo "Critical Events:" >> "$report"
    echo "$critical_events" >> "$report"
}


spin


if [ -f "$original_log" ]; then
    cp "$original_log" "$backup_log" && > "$original_log" && echo "Log backup done." || echo "Failed to backup log."
else
    echo "Original log file not found."
fi

analyze_log

find /var/log/ -type f | grep grep $(date -d "yesterday" "+%Y%m%d%H") | xargs rm -f


