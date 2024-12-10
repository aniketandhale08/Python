def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The H.C.F. is", compute_hcf(num1, num2))


"""
The HCF cannot be larger than the smaller of the two numbers.
1. HCF Definition: The largest number that can divide both input numbers without leaving a remainder.
2. Find the Smaller Number: Start checking divisors only up to the smaller of the two numbers since HCF can't be larger than it.
3. Loop Through Possible Divisors: Check each number from 1 to the smaller number.
4. Update HCF: If a number divides both inputs perfectly, update it as the current HCF.
5. Return HCF: After the loop, the last updated value is the HCF.
"""