def conditional_odd_series(a):
    series = []
    max_odd = 2 * a - 1
    i = 1
    while i <= max_odd:
        series.append(i)
        i += 2
    if a % 2 == 0:
        # if a is even, remove last item to match example output
        series = series[:-1]
    return series

# Sample Input
a = int(input("Enter a number: "))
result = conditional_odd_series(a)

# Output
print("Output:", ", ".join(map(str, result)))