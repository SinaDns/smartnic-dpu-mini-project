# SmartNICs and DPUs Project

Academic seminar project for the Computer Network course on the technologies, architectures, and applications of Smart Network Interface Cards (SmartNICs) and Data Processing Units (DPUs).

## Contributors
* **Sina Daneshgar** — [GitHub](https://github.com/SinaDns)
* **Mohammadmohsen Abbaszadeh** — [GitHub](https://github.com/HisEgo)

## Project Structure
The repository is organized into four main sections:

- **`docs/`**: Contains the final deliverables.
    - `report/`: The technical LaTeX report and bibliography.
    - `slides/`: Beamer-based presentation slides and speaker notes.
- **`examples/`**: Hands-on code demonstrations.
    - `01-simulation/`: Python script to simulate packet-processing offload performance.
    - `02-p4-programmability/`: A minimal P4_16 example for L2 forwarding.
    - `03-ebpf-xdp/`: eBPF/XDP program for high-speed packet filtering.
- **`assets/`**: Static figures, images, and precomputed simulation results.
- **`scripts/`**: Utility scripts to compile the report or run the demos quickly.

## Quick Start

### 1. View the Simulation
You can run the Python-based performance simulation using your system Python (requires `matplotlib` and `numpy`):
```bash
# Install dependencies
pip install -r examples/01-simulation/requirements.txt

# Run simulation
python examples/01-simulation/sim.py
```
Alternatively, use the provided scripts:
- Windows: `scripts/run_demo.bat`
- Linux: `bash scripts/run_demo.sh`

### 2. Build Documentation
If you have a LaTeX environment installed, you can use the top-level `Makefile`:
```bash
# Build both report and slides
make all
```

## Abstract
This project surveys the evolution of network interface cards from fixed-function devices to fully programmable DPUs. We explore offloading paradigms like P4 and eBPF/XDP, demonstrating how these technologies alleviate host CPU bottlenecks and improve cloud security/isolation.

---
*Created for the Computer Networks course, 2026.*