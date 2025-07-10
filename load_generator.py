import memcache
import time
import random
import string

mc = memcache.Client(["127.0.0.1:11211"])

def random_key_value():
    key = ''.join(random.choices(string.ascii_lowercase, k=10))
    value = ''.join(random.choices(string.ascii_letters, k=100))
    return key, value

# Write a bunch of keys
for _ in range(30000):
    k, v = random_key_value()
    mc.set(k, v)

# Read randomly to simulate traffic
for _ in range(30000):
    k, _ = random_key_value()
    mc.get(k)

print("Load test done.")