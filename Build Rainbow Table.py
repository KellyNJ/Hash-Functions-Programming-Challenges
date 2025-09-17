"""
Noah Kelly
Homework 4A
Build rainbow table
"""

import hashlib
import itertools
import string
import time

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def build_rainbow_table(charset=string.ascii_lowercase, length=4):
    table = {}
    start_time = time.time()
    for pw_tuple in itertools.product(charset, repeat=length):
        pw = ''.join(pw_tuple)
        h = hash_password(pw)
        table[h] = pw
    end_time = time.time()
    print(f"Rainbow table built for {len(table)} passwords in {end_time - start_time:.2f} seconds")
    return table

def lookup_hash(table, h):
    return table.get(h, None)

table = build_rainbow_table()
# Example lookup
test_pw = "test"
test_hash = hash_password(test_pw)
found_pw = lookup_hash(table, test_hash)
print(f"Lookup hash for '{test_pw}': Found password: {found_pw}")