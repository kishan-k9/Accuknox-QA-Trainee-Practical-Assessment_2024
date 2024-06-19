import re
from collections import Counter

# Configuration
LOG_FILE = '/path/to/webserver.log'

def analyze_log(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # Regular expressions to match patterns
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    request_pattern = re.compile(r'\"(GET|POST|PUT|DELETE) (.*?) HTTP')
    status_pattern = re.compile(r'\s(\d{3})\s')

    ip_addresses = []
    requested_pages = []
    status_codes = []

    for log in logs:
        ip_match = ip_pattern.search(log)
        request_match = request_pattern.search(log)
        status_match = status_pattern.search(log)

        if ip_match:
            ip_addresses.append(ip_match.group())
        if request_match:
            requested_pages.append(request_match.group(2))
        if status_match:
            status_codes.append(status_match.group(1))

    # Count occurrences
    ip_counter = Counter(ip_addresses)
    request_counter = Counter(requested_pages)
    status_counter = Counter(status_codes)

    # Summary report
    report = {
        'total_requests': len(logs),
        '404_errors': status_counter['404'],
        'most_requested_pages': request_counter.most_common(5),
        'top_ip_addresses': ip_counter.most_common(5)
    }

    return report

if __name__ == "__main__":
    report = analyze_log(LOG_FILE)
    print("Log Analysis Report:")
    print(f"Total requests: {report['total_requests']}")
    print(f"404 errors: {report['404_errors']}")
    print("Most requested pages:")
    for page, count in report['most_requested_pages']:
        print(f"  {page}: {count} times")
    print("Top IP addresses:")
    for ip, count in report['top_ip_addresses']:
        print(f"  {ip}: {count} times")
