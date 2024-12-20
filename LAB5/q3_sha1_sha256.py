# Design a Python-based experiment to analyze the performance of MD5, SHA-1, and SHA-256 hashing techniques in terms of computation time and collision resistance. Generate a dataset of random strings ranging from 50 to 100 strings, compute the hash values using each hashing technique, and measure the time taken for hash computation. Implement collision detection algorithms to identify any collisions within the hashed dataset.

import hashlib
import random
import string
import time

# Function to generate a random string of length n
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Function to compute hash using different algorithms (MD5, SHA-1, SHA-256)
def compute_hashes(data, hash_type):
    if hash_type == 'md5':
        return hashlib.md5(data.encode()).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(data.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(data.encode()).hexdigest()

# Function to measure the time taken for hash computation
def measure_time(strings, hash_type):
    start_time = time.time()
    hash_values = [compute_hashes(s, hash_type) for s in strings]
    end_time = time.time()
    return hash_values, (end_time - start_time)

# Function to check for collisions
def detect_collisions(hash_values):
    seen_hashes = set()
    collisions = []
    for value in hash_values:
        if value in seen_hashes:
            collisions.append(value)
        seen_hashes.add(value)
    return collisions

# Experiment setup
def run_experiment(num_strings=100, string_length=10):
    # Generate dataset of random strings
    random_strings = [generate_random_string(string_length) for _ in range(num_strings)]

    # Measure performance and collision detection for each hash function
    results = {}
    for hash_type in ['md5', 'sha1', 'sha256']:
        print(f"\n--- Hashing with {hash_type.upper()} ---")
        
        # Measure time and compute hashes
        hash_values, computation_time = measure_time(random_strings, hash_type)
        results[hash_type] = {
            'hash_values': hash_values,
            'computation_time': computation_time
        }
        
        # Detect collisions
        collisions = detect_collisions(hash_values)
        num_collisions = len(collisions)
        
        print(f"Time taken for {hash_type.upper()}: {computation_time} seconds")
        print(f"Number of collisions detected: {num_collisions}")
    
    return results

if __name__ == "__main__":
    # Running the experiment for 100 random strings
    run_experiment(num_strings=100, string_length=10)