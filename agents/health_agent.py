import psutil
import platform
import datetime
import socket
import time
import os
import requests
import math

def stress_cpu(duration=10):
    """Generates high CPU load by calculating square roots in a loop."""
    print("Simulating High CPU Usage...")
    end_time = time.time() + duration
    while time.time() < end_time:
        [math.sqrt(i) for i in range(10000)]

def stress_ram(amount_mb=500):
    """Simulates RAM usage by creating a large byte array."""
    print(f"Simulating {amount_mb}MB RAM usage...")
    # This creates a dummy list that takes up space in memory
    return bytearray(amount_mb * 1024 * 1024)

# Get the Collector URL from an environment variable
COLLECTOR_URL = os.getenv("COLLECTOR_URL", "http://localhost:5000/report")

def collect_system_metrics():
    """Collects core health metrics from the host OS."""
    metrics = {
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_release": platform.release(),
        "cpu_usage_pct": psutil.cpu_percent(interval=1),
        "memory_usage_pct": psutil.virtual_memory().percent,
        "disk_usage_pct": psutil.disk_usage('/').percent,
        "status": "HEALTHY"
    }

    if metrics["cpu_usage_pct"] > 10 or metrics["memory_usage_pct"] > 10:
        metrics["status"] = "CRITICAL"

    return metrics


if __name__ == "__main__":
    print(f"Health Agent started. Reporting to {COLLECTOR_URL}...")

    count = 0
    dummy_ram = None  # To keep RAM allocated
    while True:
        count += 1
        if count % 3 == 0:
            stress_cpu(duration=5)
            dummy_ram = stress_ram(amount_mb=256)
        else:
            dummy_ram = None

        data = collect_system_metrics()

        try:
            response = requests.post(COLLECTOR_URL, json=data, timeout=5)
            print(f"Sent report to Collector: Status {response.status_code}")
        except Exception as e:
            print(f"Failed to send report: {e}")

        print(f"Local Stats: CPU {data['cpu_usage_pct']}% | RAM {data['memory_usage_pct']}%")
        time.sleep(30)