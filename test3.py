import random
import time

import test
import test2


def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]


def test_brute_force():
    arr = generate_random_array(100)
    start_time = time.time()
    result = test2.brute_force_min_differences(arr)
    end_time = time.time()
    print(f"Brute Force Result: {result}")
    print(f"Brute Force Runtime: {end_time - start_time:.12f} seconds")


def test_sorted_approach():
    arr = generate_random_array(100)
    start_time = time.time()
    result = test2.sirali_min_farklar(arr)
    end_time = time.time()
    print(f"Sorted Approach Result: {result}")
    print(f"Sorted Approach Runtime: {end_time - start_time:.12f} seconds")


def test_brute_force_min_difference():
    arr = generate_random_array(100)
    start_time = time.time()
    result = test.brute_force_min_difference(arr)
    end_time = time.time()
    print(f"Brute Force Result: {result}")
    print(f"Brute Force Runtime: {end_time - start_time:.12f} seconds")


def test_sorted_min_difference():
    arr = generate_random_array(100)
    start_time = time.time()
    result = test.sorted_min_difference(arr)
    end_time = time.time()
    print(f"Sorted Approach Result: {result}")
    print(f"Sorted Approach Runtime: {end_time - start_time:.12f} seconds")


test_brute_force()
test_sorted_approach()
test_sorted_min_difference()
test_brute_force_min_difference()
