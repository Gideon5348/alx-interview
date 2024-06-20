#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes = {}
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0

def print_stats():
    """Print the statistics collected so far"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle the interrupt signal (Ctrl + C)"""
    print_stats()
    sys.exit(0)

# Set up the signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 7:
            continue
        ip, _, date, method, path, status, size = parts
        if method != '"GET' or path != '/projects/260' or parts[5] != 'HTTP/1.1"':
            continue
        status = int(status)
        size = int(size)
        total_size += size
        if status in valid_status_codes:
            if status not in status_codes:
                status_codes[status] = 0
            status_codes[status] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except Exception as e:
        # Ignore malformed lines
        continue

# Print stats if the script ends without interruption
print_stats()
