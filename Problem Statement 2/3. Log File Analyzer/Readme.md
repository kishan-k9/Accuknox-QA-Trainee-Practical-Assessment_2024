This script analyzes web server logs to find the number of 404 errors, the most requested pages, and the IP addresses with the most requests.

Log File Analyzer:

Reads the web server log file line by line.
Uses regular expressions to extract IP addresses, requested pages, and status codes from the log lines.
Counts the occurrences of each pattern and generates a summary report showing the total requests, 404 errors, most requested pages, and top IP addresses.

Make sure to adjust the configuration variables such as LOG_FILE and URL to match your actual setup. For the log file analyzer, ensure the log file path is correct and for the health checker, update the URL to point to your application's health endpoint.