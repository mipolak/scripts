#!/bin/bash

LOGFILE="/var/log/analysis.log"

# Ensure log file exists
touch "$LOGFILE"

echo "===== PS Snapshot: $(date) =====" >> "$LOGFILE"

# Collect per-process usage:
# PID, USER, %CPU, %MEM, RSS, VSZ, COMMAND
ps -eo pid,user,%cpu,%mem,rss,vsz,args --sort=-%cpu --no-headers | head -n 20 >> "$LOGFILE"


echo "=== I/O Usage (iotop) ===" >> "$LOGFILE"
# Run iotop in batch mode, one snapshot (-n 1), per process (-P), show all (-a), top 10 processes
sudo iotop -P -b -n 1 | head -n 13 >> "$LOGFILE"

echo "==========" >> "$LOGFILE"
