# Multi-OS Automation Health Dashboard (WIP)

... (Overview) ...

### Current Features (Phase 1 & 2):
* **Cross-Platform Agent:** Python-based monitoring using `psutil`.
* **Containerized Orchestration:** Docker-Compose simulates a multi-OS fleet.
* **Telemetry:** Real-time logging of CPU, RAM, and Disk metrics.

### Why this Architecture?
In high-performance environments, regression tests often run on "headless" distributed systems. This project mimics that by:
* **Decoupling Collection from Storage:** The agents are lightweight to avoid impacting the performance of the software being tested.
* **Multi-OS Simulation:** Using Docker to simulate different Linux distros ensures the automation framework is portable across the various OS environments required for driver and application testing.

### Next Steps:
* [ ] Centralized Data Collector (Flask API)
* [ ] Persistent Storage (MySQL)
* [ ] Health Visualization Dashboard