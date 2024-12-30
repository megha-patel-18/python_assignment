def generate_even_numbers():
    num = 2  # Start with the first even number
    count = 0
    while count < 10:
        yield num
        num += 2  # Increment to the next even number
        count += 1

# Using the generator
even_numbers = generate_even_numbers()
for even in even_numbers:
    print(even)