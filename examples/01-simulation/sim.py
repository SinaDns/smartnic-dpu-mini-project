"""
simulate_offload.py
Simple educational simulation comparing CPU-only packet processing vs. DPU-offload effect.
Run: python simulate_offload.py --packets 100000
Generates a summary and writes `assets/offload_plot.png` in the repository root.
"""
import argparse
import os
import math
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np


def one_model_times(n, base_us, jitter_us):
    # return list of per-packet processing times in microseconds
    return [max(0.0, random.gauss(base_us, jitter_us)) for _ in range(n)]


def simulate(n, cpu_base=3.0, cpu_jitter=0.5, dpu_base=0.8, dpu_jitter=0.2, offload_fraction=0.65):
    # cpu-only all work done on CPU
    cpu_times = one_model_times(n, cpu_base, cpu_jitter)
    cpu_mean = statistics.mean(cpu_times)
    cpu_throughput_kpps = 1e3 / cpu_mean  # kilo-packets/sec

    # dpu model: fraction processed by DPU (fast), remainder by CPU
    dpu_times = one_model_times(n, dpu_base, dpu_jitter)
    host_times = one_model_times(n, cpu_base * (1 - offload_fraction), cpu_jitter * 0.6)
    # total per-packet perceived processing = host + (offloaded work executed on dpu)
    combined = [host_times[i] + offload_fraction * dpu_times[i] for i in range(n)]
    combined_mean = statistics.mean(combined)
    combined_throughput_kpps = 1e3 / combined_mean

    return {
        "cpu_mean_us": cpu_mean,
        "cpu_kpps": cpu_throughput_kpps,
        "dpu_mean_us": combined_mean,
        "dpu_kpps": combined_throughput_kpps,
        "cpu_samples": cpu_times,
        "combined_samples": combined,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate CPU vs DPU packet-processing")
    parser.add_argument("--packets", type=int, default=50000, help="Number of packets to simulate")
    parser.add_argument("--offload", type=float, default=0.65, help="Fraction of work offloaded to DPU (0-1)")
    parser.add_argument("--seed", type=int, default=1, help="Random seed")
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    res = simulate(args.packets, offload_fraction=args.offload)

    print("Simulation summary:")
    print(f"  CPU-only mean per-packet = {res['cpu_mean_us']:.3f} µs — {res['cpu_kpps']:.1f} kpps")
    print(f"  With DPU offload mean per-packet = {res['dpu_mean_us']:.3f} µs — {res['dpu_kpps']:.1f} kpps")
    improvement = (res['dpu_kpps'] / res['cpu_kpps'] - 1.0) * 100.0
    print(f"  Throughput improvement ≈ {improvement:.1f}%")

    # plot
    labels = ['CPU-only', 'CPU + DPU']
    kpps = [res['cpu_kpps'], res['dpu_kpps']]

    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(labels, kpps, color=['#ff7f0e', '#1f77b4'])
    ax.set_ylabel('Throughput (kpps)')
    ax.set_title('Simulated packet-processing: CPU-only vs DPU offload')
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h * 1.01, f"{h:.1f}", ha='center', va='bottom')
    plt.tight_layout()
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(base_path, "assets", "offload_plot.png")
    plt.savefig(out, dpi=150)
    print(f"Plot saved to {out}")