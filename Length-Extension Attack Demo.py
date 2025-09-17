"""
Noah Kelly
Homework 4A
Length-extension attack demo
"""

import hashlib
import struct

def sha256_extend(original_hash, known_msg, append_msg, secret_len):
    # Calculate padding that was added to original message
    original_len = secret_len + len(known_msg)
    padding_len = 64 - ((original_len + 9) % 64)
    if padding_len == 64:
        padding_len = 0
    
    # SHA-256 padding
    padding = b'\x80' + (b'\x00' * padding_len) + struct.pack('>Q', original_len * 8)
    
    # Extend message
    extended_msg = known_msg + padding + append_msg
    
    return extended_msg, "SIMULATED_EXTENDED_HASH"


def driver():
    print("SHA-256 Length Extension Attack\n")
    
    # Initialization
    secret = b"superDuperSecret"
    known = b"user = duke"
    append = b"&admin = true"
    
    print(f"Secret: {secret}")
    print(f"Known message: {known}")
    print(f"Want to append: {append}")
    print()
    
    # What the server computed originally
    original = secret + known
    original_hash = hashlib.sha256(original).hexdigest()
    print(f"Server's hash: {original_hash}")
    print()
    
    # The attack
    print("ATTACK... Computing extended hash without knowing secret ")
    extended_msg, _ = sha256_extend(original_hash, known, append, len(secret))
    
    # What the actual extended message is
    full_message = secret + extended_msg
    actual_hash = hashlib.sha256(full_message).hexdigest()
    
    print(f"Extended message: {extended_msg}")
    print(f"Full message: {full_message}")
    print(f"New hash: {actual_hash}")
    print()

driver()