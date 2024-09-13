#!/usr/bin/env python3
import subprocess
from datetime import datetime, timedelta
import os

def get_local_time():
    result = subprocess.run(['date', '+%Y-%m-%d %H:%M:%S'], capture_output=True, text=True)
    local_time_str = result.stdout.strip()
    local_time = datetime.strptime(local_time_str, '%Y-%m-%d %H:%M:%S')
    return local_time

def get_google_time():
    result = subprocess.run(['wget', '--method=HEAD', '-qSO-', '--max-redirect=0', 'google.com'], capture_output=True, t
ext=True)
    for line in result.stderr.splitlines():
        if 'Date:' in line:
            google_time_str = line.split('Date: ')[1].strip()
            google_time = datetime.strptime(google_time_str, '%a, %d %b %Y %H:%M:%S %Z')
            return google_time
    return None

def set_local_time(new_time):
    new_time_str = new_time.strftime('%Y-%m-%d %H:%M:%S')
    os.system(f'date -s "{new_time_str}"')

def main():
    local_time = get_local_time()
    google_time = get_google_time()

    if google_time is None:
        print("Failed to fetch Google's time.")
        return

    time_difference = abs((google_time - local_time).total_seconds())
    if time_difference > 120:  # 2 minutes in seconds
        print(f"Local time is more than 2 minutes out of sync. Updating local time to {google_time}.")
        set_local_time(google_time)
    else:
        print("Local time is in sync with Google's time.")

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import subprocess
from datetime import datetime, timedelta
import os

def get_local_time():
    result = subprocess.run(['date', '+%Y-%m-%d %H:%M:%S'], capture_output=True, text=True)
    local_time_str = result.stdout.strip()
    local_time = datetime.strptime(local_time_str, '%Y-%m-%d %H:%M:%S')
    return local_time

def get_google_time():
    result = subprocess.run(['wget', '--method=HEAD', '-qSO-', '--max-redirect=0', 'google.com'], capture_output=True, t
ext=True)
    for line in result.stderr.splitlines():
        if 'Date:' in line:
            google_time_str = line.split('Date: ')[1].strip()
            google_time = datetime.strptime(google_time_str, '%a, %d %b %Y %H:%M:%S %Z')
            return google_time
    return None

def set_local_time(new_time):
    new_time_str = new_time.strftime('%Y-%m-%d %H:%M:%S')
    os.system(f'date -s "{new_time_str}"')

def main():
    local_time = get_local_time()
    google_time = get_google_time()

    if google_time is None:
        print("Failed to fetch Google's time.")
        return

    time_difference = abs((google_time - local_time).total_seconds())
    if time_difference > 120:  # 2 minutes in seconds
        print(f"Local time is more than 2 minutes out of sync. Updating local time to {google_time}.")
        set_local_time(google_time)
    else:
        print("Local time is in sync with Google's time.")

if __name__ == '__main__':
    main()
