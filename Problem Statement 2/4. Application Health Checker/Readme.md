This script checks the uptime of an application by sending an HTTP request and checking the response status code. It determines if the application is 'up' or 'down'.

Application Health Checker:

Sends an HTTP GET request to the application's health endpoint at regular intervals.
Logs and prints the application status based on the HTTP response status code.
Considers the application 'up' if the status code is 200 and 'down' otherwise.