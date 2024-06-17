import shutil
import subprocess
import os
from datetime import datetime

# Configuration
SOURCE_DIR = '/path/to/source/directory'
DESTINATION_DIR = '/path/to/destination/directory'
REMOTE_SERVER = 'user@example.com:/path/to/remote/directory'
LOG_FILE = 'backup_log.txt'

# Function to perform backup
def perform_backup():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_name = f'backup_{timestamp}.tar.gz'
    backup_path = os.path.join(DESTINATION_DIR, backup_name)
    
    try:
        # Create a compressed archive of the source directory
        shutil.make_archive(backup_path[:-7], 'gztar', SOURCE_DIR)
        
        # Copy the archive to a remote server using SCP
        scp_command = ['scp', backup_path, REMOTE_SERVER]
        subprocess.run(scp_command, check=True)
        
        return True, f"Backup successful: {backup_path}"
    except Exception as e:
        return False, f"Backup failed: {str(e)}"

# Function to log the backup operation
def log_backup_result(result):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.now().isoformat()} - {result}\n")

# Main function to run the backup
def main():
    print("Starting automated backup...")
    success, message = perform_backup()
    print(message)
    log_backup_result(message)

if __name__ == "__main__":
    main()
