#!/usr/bin/env python3

def print_fibonacci(length):
    
    # The logic for initializing the fsirts two Fibonacci numbers
    fib_sequence = [0, 1]

# The logic for generarting Fibonacci numbers
    while len(fib_sequence) < length:
    # Append the sum of the last two elements to the list
      fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

# Print the Fibonacci sequence up to the requested length
    print(fib_sequence[:length])

print_fibonacci(10)
