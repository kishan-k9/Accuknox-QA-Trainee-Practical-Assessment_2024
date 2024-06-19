import requests
import logging
import time

# Configure logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
URL = 'http://yourapplication.com/health'
CHECK_INTERVAL = 60  # in seconds

def check_application_health(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logging.info(f'Application is UP. Status code: {response.status_code}')
            return 'up'
        else:
            logging.warning(f'Application is DOWN. Status code: {response.status_code}')
            return 'down'
    except requests.RequestException as e:
        logging.error(f'Application is DOWN. Error: {str(e)}')
        return 'down'

if __name__ == "__main__":
    while True:
        status = check_application_health(URL)
        print(f"Application status: {status}")
        time.sleep(CHECK_INTERVAL)
