import psutil

# Define thresholds
THRESHOLD_CPU_PERCENT = 80.0
THRESHOLD_MEM_PERCENT = 80.0
THRESHOLD_DISK_PERCENT = 80.0

# Function to check CPU usage
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > THRESHOLD_CPU_PERCENT:
        print(f"High CPU usage detected! ({cpu_percent}%)")

# Function to check memory usage
def check_memory_usage():
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    if mem_percent > THRESHOLD_MEM_PERCENT:
        print(f"High memory usage detected! ({mem_percent}%)")

# Function to check disk usage
def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    if disk_percent > THRESHOLD_DISK_PERCENT:
        print(f"High disk usage detected! ({disk_percent}%)")

# Function to check running processes
def check_running_processes():
    num_processes = len(psutil.pids())
    print(f"Number of running processes: {num_processes}")

# Main function to run checks
def main():
    print("Running system health checks...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
