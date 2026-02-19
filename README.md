# SmartNICs and DPUs Project

Academic seminar project for the Computer Network course on the technologies, architectures, and applications of Smart Network Interface Cards (SmartNICs) and Data Processing Units (DPUs).

## Contributors
* **Sina Daneshgar** — [GitHub](https://github.com/SinaDns)
* **Mohammadmohsen Abbaszadeh** — [GitHub](https://github.com/HisEgo)

## Project Structure
The repository is organized into the following top-level sections:

- **`docs/`**: Final deliverables.
  - `report/`: Technical LaTeX report and bibliography.
  - `slides/`: Beamer presentation (`presentation.tex`) — includes SmartNIC landscape and an eBPF/XDP runtime slide plus code-reference slides.
- **`examples/`**: Hands-on demos.
  - `01-simulation/`: Python simulation for offload performance.
  - `02-p4-programmability/`: Minimal P4_16 L2 forwarding (`basic_l2.p4`).
  - `03-ebpf-xdp/`: eBPF/XDP ICMP-drop example (`03-ebpf_xdp.c`).
- **`assets/`**: Figures used in slides.
- **`scripts/`**: Utility scripts to run demos and build artifacts.


## Quick Start

### 1. Run the simulation
```bash
pip install -r examples/01-simulation/requirements.txt
python examples/01-simulation/sim.py
```
Alternatively, use the provided scripts:
- Windows: `scripts/run_demo.bat`
- Linux: `bash scripts/run_demo.sh`

### 2. Build slides or report
If you have LaTeX installed you can build only the slides or the full project using the Makefile:
```bash
# Build slides only
make slides

# Build both report and slides
make all
```

## Examples referenced in the slides
- P4 example: `examples/02-p4-programmability/basic_l2.p4` — minimal match-action L2 forwarder.
- eBPF/XDP example: `examples/03-ebpf-xdp/03-ebpf_xdp.c` — early-drop ICMP filter; attach with `ip link set dev <iface> xdp obj ...`.

## Further reading / References
- Packet Pushers — DPU-based smart interfaces: https://packetpushers.net/blog/dpu-based-smart-interfaces-and-the-future-of-network-functions-and-security-at-the-edge/
- Ubuntu — Data centre networking & SmartNICs: https://ubuntu.com/blog/data-centre-networking-smartnics
- Hot Chips — NVIDIA DPU (Idan Burstein): https://www.hc33.hotchips.org/assets/program/conference/day1/HC2021.NVIDIA.IdanBurstein.v08.norecording.pdf
- P4 Language Consortium — https://p4.org
- eBPF community — https://ebpf.io

---
*Created for the Computer Networks course, 2026.*