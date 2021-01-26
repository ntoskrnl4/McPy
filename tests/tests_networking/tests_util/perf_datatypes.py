"""Standalone performance testing script for networking datatypes."""

from networking.util.datatypes import *
from time import perf_counter_ns

import random
import sys

run_count = 2**14  # Number of loops to test with. Larger values will take longer and require more memory ( O(n) )


def main():
    sys.stdout.write(f"Testing VarInt speed with {run_count} iterations...\n")

    perf_vartypes(VarInt, "Size 1", 0,     2**7-1)
    perf_vartypes(VarInt, "Size 2", 2**7,  2**14-1)
    perf_vartypes(VarInt, "Size 3", 2**14, 2**21-1)
    perf_vartypes(VarInt, "Size 4", 2**21, 2**28-1)
    perf_vartypes(VarInt, "Size 5", 2**28, 2**31-1)
    perf_vartypes(VarInt, "Negative", -(2**31), -1)
    
    perf_vartypes(VarLong, "Size 1", 0,     2**7-1)
    perf_vartypes(VarLong, "Size 2", 2**7,  2**14-1)
    perf_vartypes(VarLong, "Size 3", 2**14, 2**21-1)
    perf_vartypes(VarLong, "Size 4", 2**21, 2**28-1)
    perf_vartypes(VarLong, "Size 5", 2**28, 2**35-1)
    perf_vartypes(VarLong, "Size 6", 2**35, 2**42-1)
    perf_vartypes(VarLong, "Size 7", 2**42, 2**49-1)
    perf_vartypes(VarLong, "Size 8", 2**49, 2**56-1)
    perf_vartypes(VarLong, "Size 9", 2**56, 2**63-1)
    perf_vartypes(VarLong, "Negative", -(2**63), -1)
    

def perf_vartypes(vartype, explanation: str, lower: int, upper: int):
    items = [random.randint(lower, upper) for _ in range(run_count)]
    sys.stdout.write(f"{explanation} {vartype.__name__}s: \n")
    start = perf_counter_ns()
    encoded = [vartype.encode(x) for x in items]
    end = perf_counter_ns()
    time = (end - start) / run_count
    sys.stdout.write(f"\tEncode: {time / 1000:.2f} us / loop\n")

    start = perf_counter_ns()
    decoded = [vartype.decode(x) for x in encoded]
    end = perf_counter_ns()
    time = (end - start) / run_count
    sys.stdout.write(f"\tDecode: {time / 1000:.2f} us / loop\n")


if __name__ == '__main__':
    main()
