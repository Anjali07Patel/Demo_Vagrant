def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # for a new line at the end

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    fibonacci(num_terms)

