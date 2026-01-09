# Multi-OS Automation Health Dashboard (WIP)
This project simulates a complex regression testing environment (Linux/Windows/VMware) 
to monitor system health during automated test cycles.

### Current Features (Phase 1 & 2):
* **Cross-Platform Agent:** Python-based monitoring using `psutil`.
* **Containerized Orchestration:** Docker-Compose simulates a multi-OS fleet.
* **Telemetry:** Real-time logging of CPU, RAM, and Disk metrics.

### Next Steps:
* [ ] Centralized Data Collector (Flask API)
* [ ] Persistent Storage (MySQL)
* [ ] Health Visualization Dashboard