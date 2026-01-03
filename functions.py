def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    # return multiply(subtract(fahrenheit, 32), 9 / 5) # <-- Fix this in step 7
    assert fahrenheit >= -459.67, "Temperature below absolute zero!"
    return multiply(subtract(fahrenheit, 32), 5 / 9)