"""
Noah Kelly
Homework 4A
Implement birthday attack simulation
"""

import hashlib
import random
import string

def reduced_hash(data, bits=24):
    # Compute SHA-256 and truncate to 'bits' bits
    full_hash = hashlib.sha256(data).digest()
    # Take first bits//8 bytes
    truncated = full_hash[:bits // 8]
    return truncated

def birthday_attack(bits=24):
    seen = {}
    attempts = 0
    while True:
        # Generate random input
        candidate = ''.join(random.choices(string.ascii_letters + string.digits, k=8)).encode()
        h = reduced_hash(candidate, bits)
        attempts += 1
        if h in seen:
            print(f"Collision found after {attempts} attempts!")
            print(f"Input 1: {seen[h].decode()}")
            print(f"Input 2: {candidate.decode()}")
            print(f"Hash (hex): {h.hex()}")
            return attempts
        else:
            seen[h] = candidate

attempts = birthday_attack()
print(f"Expected attempts ~ {2**(24/2):.0f}")