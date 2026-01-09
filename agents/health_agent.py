import psutil
import platform
import datetime
import socket
import time
import os
import requests

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

    if metrics["cpu_usage_pct"] > 90 or metrics["memory_usage_pct"] > 90:
        metrics["status"] = "CRITICAL"

    return metrics


if __name__ == "__main__":
    print(f"Health Agent started. Reporting to {COLLECTOR_URL}...")
    while True:
        data = collect_system_metrics()

        try:
            response = requests.post(COLLECTOR_URL, json=data, timeout=5)
            print(f"Sent report to Collector: Status {response.status_code}")
        except Exception as e:
            print(f"Failed to send report: {e}")

        print(f"Local Stats: CPU {data['cpu_usage_pct']}% | RAM {data['memory_usage_pct']}%")
        time.sleep(30)