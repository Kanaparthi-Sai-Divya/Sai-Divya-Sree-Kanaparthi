# Problem-4.py

def count_multiples(input_list):
    result = {}
    for i in range(1, 10):
        count = 0
        for num in input_list:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

# Sample Input
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Get Result
result = count_multiples(input_list)

# Output
print("Output:")
print(result)
