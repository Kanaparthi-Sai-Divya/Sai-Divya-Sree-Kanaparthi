def generate_odd_series(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

# Sample Input
a = int(input("Enter a number: "))
result = generate_odd_series(a)

# Output
print("Output:", ", ".join(map(str, result)))
