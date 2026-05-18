import os
import csv
import time
import random
from concurrent.futures import ThreadPoolExecutor

N_VALUES = [
    1_000_000,
    10_000_000,
    100_000_000,
    1_000_000_000,
    10_000_000_000,
    100_000_000_000,
]

M_VALUES = [1, 2, 4, 8, 16, 32, 64, 128]

OUTPUT_FILE = "results/pi_monte_carlo_parallel_results.csv"


def count_inside_circle(n: int) -> int:
    rng = random.Random()
    inside = 0
    for _ in range(n):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return inside


def estimate_pi(n: int, m: int) -> tuple[float, float]:
    batch = n // m
    remainder = n % m

    batches = [batch] * m
    for i in range(remainder):
        batches[i] += 1

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=m) as executor:
        results = list(executor.map(count_inside_circle, batches))
    elapsed = time.perf_counter() - start

    pi = 4.0 * sum(results) / n
    return pi, elapsed


def main():
    os.makedirs("results", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["N", "M", "pi_estimate", "time_seconds"])

        for n in N_VALUES:
            for m in M_VALUES:
                print(f"N={n:,}  M={m} ...", end=" ", flush=True)
                pi, elapsed = estimate_pi(n, m)
                print(f"π≈{pi:.8f}  t={elapsed:.3f}s")
                writer.writerow([n, m, pi, round(elapsed, 6)])
                f.flush()

    print(f"\nРезультати збережено: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
