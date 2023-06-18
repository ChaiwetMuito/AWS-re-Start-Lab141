# Lab 141 

# function for check number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# input for range number to find prime
print('input for range number to find prime')
while True:
    try:
        # Input the first number
        startNumber = int(input("Enter the first number: "))
        # Input the second number
        stopNumber = int(input("Enter the Last number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Store prime numbers in a file
with open('results.txt', 'w') as file:
    for num in range(startNumber, stopNumber + 1):
        if is_prime(num):
            print(str(num))
            file.write(str(num) + '\n')
