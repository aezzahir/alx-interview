#!/usr/bin/env python3
"""
Log parsing
"""
import sys
import re

# Initialize variables to store metrics
total_file_size = 0
status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    # Loop through stdin line by line
    for line_number, line in enumerate(sys.stdin, start=1):
        # Use regex to match the required format
        match = re.match(
            r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\]"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', line)
        if match:
            ip_address, _, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)
            
            # Update total file size
            total_file_size += file_size
            
            # Update status code counts
            if status_code in status:
                status[status_code] += 1
            
            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print(f'Total file size: {total_file_size}')
                for code, count in sorted(status.items()):
                    if count > 0:
                        print(f'{code}: {count}')
                print()
                
except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL+C)
    print(f'Total file size: {total_file_size}')
    for code, count in sorted(status.items()):
        if count > 0:
            print(f'{code}: {count}')
