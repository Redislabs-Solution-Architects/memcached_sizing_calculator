# Gabs Memcached Sizing Calculator

A minimal tool to **measure dataset size and throughput (ops/sec)** of a running Memcached instance.

This is useful for:
- Estimating memory usage of your current keyspace
- Measuring read/write throughput based on real-time stats

## 🧰 What's Inside

```
.
├── memcached_sizing_calculator.py  # Main tool: measures memory and ops/sec
├── load_generator.py               # Optional helper: writes dummy data for testing
└── requirements.txt                # Python dependencies
```

## ✅ Features

- 📊 Calculates **total dataset size** in MB
- ⚡ Estimates **ops/sec** by sampling `cmd_get` and `cmd_set` over time
- 📎 Uses official `python-memcached` client (no deprecated telnetlib)

## 🚀 Getting Started

### 1. Install Dependencies

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Memcached

Locally:

```bash
memcached -p 11211 -m 512 -vv
```

Or via Docker:

```bash
docker run -d --name memcached -p 11211:11211 memcached
```

### 3. Populate Some Data (Optional)

Use the included generator to create keys/values:

```bash
python load_generator.py
```

This is useful if your Memcached instance is empty and you want to simulate usage.

### 4. Run the Calculator

```bash
python memcached_sizing_calculator.py
```

This will:
- Connect to Memcached
- Wait 60 seconds (default)
- Print dataset size and ops/sec

### ✍️ Sample Output

```
--- Memcached Metrics ---
Dataset Size: 16.42 MB
Ops/sec (get + set): 2023.40
 - cmd_get delta: 10200
 - cmd_set delta: 2000
 - Total keys: 10000
 - Memory cap: 64.00 MB
```

## ⚙️ Config

You can tweak host, port, and interval inside `memcached_sizing_calculator.py`:

```python
HOST = "127.0.0.1"
PORT = 11211
INTERVAL = 60  # in seconds
```

## 📄 License

MIT
