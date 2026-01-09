import psutil
import platform
import datetime
import socket
import time


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
    print("Health Agent started. Monitoring system...")
    while True:
        data = collect_system_metrics()

        print(f"[{data['timestamp']}] Node: {data['hostname']} ({data['os']})")
        print(f"  Status: {data['status']}")
        print(f"  CPU: {data['cpu_usage_pct']}% | RAM: {data['memory_usage_pct']}% | Disk: {data['disk_usage_pct']}%")
        print("-" * 30)

        time.sleep(30)