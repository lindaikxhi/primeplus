import psutil
import time
import os

def clear_console():
    # Clear the console for Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def display_usage():
    while True:
        clear_console()
        print("PrimePlus - Real-time Resource Usage Monitor\n")
        
        # CPU Usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        
        # Memory Usage
        memory_info = psutil.virtual_memory()
        print(f"Memory Usage: {memory_info.percent}% ({memory_info.used / (1024**3):.2f} GB used of {memory_info.total / (1024**3):.2f} GB)")
        
        # Disk Usage
        disk_info = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_info.percent}% ({disk_info.used / (1024**3):.2f} GB used of {disk_info.total / (1024**3):.2f} GB)")
        
        # Sleep for a second before updating
        time.sleep(1)

if __name__ == "__main__":
    display_usage()