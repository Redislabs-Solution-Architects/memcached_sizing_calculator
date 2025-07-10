import time
import memcache

HOST = "127.0.0.1"
PORT = 11211
INTERVAL = 60  # seconds

def get_stats(client):
    raw_stats = client.get_stats()[0][1]  # First server tuple, stats dict
    stats = {}
    for k, v in raw_stats.items():
        try:
            stats[k] = int(v)
        except ValueError:
            continue
    return stats

def main():
    mc = memcache.Client([(f"{HOST}:{PORT}")])

    print(f"Collecting Memcached stats... (interval = {INTERVAL}s)")
    stats_before = get_stats(mc)
    time.sleep(INTERVAL)
    stats_after = get_stats(mc)

    delta_get = stats_after['cmd_get'] - stats_before['cmd_get']
    delta_set = stats_after['cmd_set'] - stats_before['cmd_set']
    total_ops = delta_get + delta_set
    ops_per_sec = total_ops / INTERVAL

    memory_used_bytes = stats_after.get('bytes', 0)
    memory_used_mb = memory_used_bytes / 1024 / 1024

    print(f"\n--- Memcached Metrics ---")
    print(f"Dataset Size: {memory_used_mb:.2f} MB")
    print(f"Ops/sec (get + set): {ops_per_sec:.2f}")
    print(f" - cmd_get delta: {delta_get}")
    print(f" - cmd_set delta: {delta_set}")
    print(f" - Total keys: {stats_after.get('curr_items', 0)}")
    print(f" - Memory cap: {stats_after.get('limit_maxbytes', 0) / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    main()