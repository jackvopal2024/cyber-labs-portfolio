# log_analyzer.py
# Simple Log Analysis Tool

import csv

log_file = "examples/auth_sample.log"
output_file = "failed_logins.csv"

failed_logins = {}

with open(log_file, "r") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]  
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

print("\nFailed login attempts by IP:")
for ip, count in failed_logins.items():
    print(f"{ip}: {count}")

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Failed Attempts"])
    for ip, count in failed_logins.items():
        writer.writerow([ip, count])

print(f"\nReport saved to {output_file}")
