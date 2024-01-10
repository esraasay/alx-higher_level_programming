import sys
from collections import defaultdict

def compute_metrics():
    total_file_size = 0
    status_code_counts = defaultdict(int)

    try:
        for line_number, line in enumerate(sys.stdin, 1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[-2]
                file_size = parts[-1]

                try:
                    file_size = int(file_size)
                    total_file_size += file_size
                    status_code_counts[status_code] += 1
                except ValueError:
                    print(f"Error parsing file size on line {line_number}")

            if line_number % 10 == 0:
                print_metrics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_counts)

def print_metrics(total_file_size, status_code_counts):
    print(f"Total file size: {total_file_size}")
    
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

if __name__ == "__main__":
    compute_metrics()
