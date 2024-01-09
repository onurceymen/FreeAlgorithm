def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n + 1):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    return fib_sequence

# Kullanıcıdan Fibonacci serisi için istenen terim sayısını alın
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Fibonacci serisini hesapla ve ekrana yazdır
result = fibonacci(num_terms)
print(f"Fibonacci Sequence for the first {num_terms} terms: {result}")
