print("md. shah emran hossain sabbir")
print(223902002)

# 1. Program to find the sum of odd and even numbers
numbers = [2, 5, 7, 8, 10, 13, 4, 9]

sum_even = 0
sum_odd = 0

for n in numbers:
    if n % 2 == 0:
        sum_even += n
    else:
        sum_odd += n

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

# 2. Program to find the smallest number
numbers = [22, 39, 2, 1]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest number is:", smallest)

# 3. Program to find the sum of all numbers between 50 and 100
# which are divisible by 3 and not divisible by 5
total = 0

for n in range(50, 101):
    if n % 3 == 0 and n % 5 != 0:
        total += n

print("Sum =", total)

# 4. Find the Second Highest Number
numbers = [10, 25, 30, 45, 60, 50]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_highest = unique_numbers[-2]
print("Second highest number is:", second_highest)

# 5. Factorial Using For Loop
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)

#6. Fibonacci Series
n = int(input("Enter how many terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b





