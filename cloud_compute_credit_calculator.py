#!/usr/bin/env python3
"""Awesome Cloud GPU & VPS Free Credits Directory Calculator 2026."""
import argparse

PROVIDERS = {
    "vultr": {"name": "Vultr Cloud", "credit": 250, "gpu_support": True, "min_deposit": 10},
    "runpod": {"name": "RunPod", "credit": 50, "gpu_support": True, "min_deposit": 25},
    "vastai": {"name": "Vast.ai", "credit": 25, "gpu_support": True, "min_deposit": 10},
    "digitalocean": {"name": "DigitalOcean", "credit": 200, "gpu_support": False, "min_deposit": 5}
}

def calculate():
    print("=" * 70)
    print("Awesome Cloud GPU & VPS Free Credit Directory 2026")
    print("=" * 70)
    print(f"{'Provider':<15} {'Free Credit':<15} {'GPU Accelerated':<18} {'Min Deposit'}")
    print("-" * 70)
    total_credits = 0
    for key, data in PROVIDERS.items():
        total_credits += data["credit"]
        print(f"{data['name']:<15} ${data['credit']:.2f}{'':<9} {'Yes (A100/H100)' if data['gpu_support'] else 'CPU Only':<18} ${data['min_deposit']:.2f}")
    print("-" * 70)
    print(f"{'Total Accessible Trial Capital':<30} ${total_credits:.2f} in free cloud credits")
    print("=" * 70)

if __name__ == "__main__":
    calculate()
