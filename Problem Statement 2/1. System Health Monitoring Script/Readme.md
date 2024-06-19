This script monitors CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds, it logs an alert to a log file.

System Health Monitoring Script:

Uses the psutil library to fetch system metrics.
Logs information and warnings to a log file based on predefined thresholds.
Runs indefinitely, checking system health every minute.