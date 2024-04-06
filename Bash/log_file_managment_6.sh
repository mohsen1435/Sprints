#!/bin/bash

original_log="/var/log/vmware-vmsvc-root.1.log"
backup_log="/var/log/messages.old"
report="/var/log/report.txt"

usage() {
    echo "Usage: $0 [-o <original_log>] [-b <backup_log>] [-r <report>]"
    echo "Options:"
    echo "  -o <original_log>: Path to the original log file (default: /var/log/vmware-vmsvc-root.1.log)"
    echo "  -b <backup_log>: Path to the backup log file (default: /var/log/messages.old)"
    echo "  -r <report>: Path to the report file (default: /var/log/report.txt)"
    exit 1
}

while getopts ":o:b:r:" opt; do
    case $opt in
        o) original_log="$OPTARG" ;;
        b) backup_log="$OPTARG" ;;
        r) report="$OPTARG" ;;
        \?) echo "Invalid option: -$OPTARG" >&2; usage ;;
        :) echo "Option -$OPTARG requires an argument." >&2; usage ;;
    esac
done

cpu(){
pid=$$
top -b -p $pid -n 5 > /var/log/cpu.log

ps aux | grep "log_file_managment_2.sh" > /var/log/trace.log
}

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

find /var/log/ -type f | grep $(date -d "yesterday" "+%Y%m%d%H") | xargs rm -f

cpu
