#!/usr/bin/env python3
"""
A simple memory information utility similar to the Unix 'free' command.
Displays information about system memory usage.
"""

import os
import sys


def get_memory_info():
    """
    Get memory information from the system.
    Returns a dictionary with memory statistics.
    """
    try:
        # Try to read from /proc/meminfo (Linux)
        with open('/proc/meminfo', 'r') as f:
            meminfo = {}
            for line in f:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip().split()[0]  # Get numeric value
                    meminfo[key] = int(value)
            return meminfo
    except FileNotFoundError:
        # If /proc/meminfo doesn't exist (non-Linux), return mock data
        print("Warning: /proc/meminfo not found. Using mock data.", file=sys.stderr)
        return {
            'MemTotal': 8000000,
            'MemFree': 2000000,
            'MemAvailable': 3000000,
            'Buffers': 500000,
            'Cached': 1500000,
            'SwapTotal': 2000000,
            'SwapFree': 1500000,
        }


def format_bytes(kb):
    """Convert kilobytes to human-readable format."""
    return f"{kb:>12}"


def display_memory_info(meminfo):
    """Display memory information in a formatted table."""
    # Calculate values (all in KB)
    total_mem = meminfo.get('MemTotal', 0)
    free_mem = meminfo.get('MemFree', 0)
    available_mem = meminfo.get('MemAvailable', free_mem)
    buffers = meminfo.get('Buffers', 0)
    cached = meminfo.get('Cached', 0)
    used_mem = total_mem - free_mem - buffers - cached
    
    swap_total = meminfo.get('SwapTotal', 0)
    swap_free = meminfo.get('SwapFree', 0)
    swap_used = swap_total - swap_free
    
    # Print header
    print(f"{'':>15} {'total':>12} {'used':>12} {'free':>12} {'shared':>12} {'buff/cache':>12} {'available':>12}")
    
    # Print memory row
    shared = meminfo.get('Shmem', 0)
    buff_cache = buffers + cached
    print(f"{'Mem:':>15} {format_bytes(total_mem)} {format_bytes(used_mem)} {format_bytes(free_mem)} "
          f"{format_bytes(shared)} {format_bytes(buff_cache)} {format_bytes(available_mem)}")
    
    # Print swap row
    print(f"{'Swap:':>15} {format_bytes(swap_total)} {format_bytes(swap_used)} {format_bytes(swap_free)}")


def main():
    """Main function to run the free command."""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("Usage: free.py")
        print("Display amount of free and used memory in the system")
        return 0
    
    meminfo = get_memory_info()
    display_memory_info(meminfo)
    return 0


if __name__ == '__main__':
    sys.exit(main())
