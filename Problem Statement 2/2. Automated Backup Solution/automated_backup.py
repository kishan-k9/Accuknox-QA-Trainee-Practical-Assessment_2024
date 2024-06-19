import subprocess
import logging
import datetime

# Configure logging
logging.basicConfig(filename='backup_report.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
SOURCE_DIR = '/path/to/source_directory'
REMOTE_USER = 'remote_user'
REMOTE_HOST = 'remote_host'
REMOTE_DIR = '/path/to/remote_directory'

def run_backup():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        result = subprocess.run(
            ['rsync', '-avz', SOURCE_DIR, f'{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}'],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        logging.info(f'{timestamp} - Backup successful: {result.stdout.decode()}')
    except subprocess.CalledProcessError as e:
        logging.error(f'{timestamp} - Backup failed: {e.stderr.decode()}')

if __name__ == "__main__":
    run_backup()
