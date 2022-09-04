# Euclidean algorithm for finding the Greatest Common Divisor of two numbers, a and b (Verbose)
a = abs(int(input("Enter value of a: ")))
b = abs(int(input("Enter value of b: ")))

_a = a
_b = b
# Swap numbers if first input is smaller the second input
if a < b:
    a, b = b, a

# Case 1: If smaller input divides the larger input
if a % b == 0:
    gcd = min([a, b])
    print(f"GCD({_a}, {_b}) = {gcd}")
else:
    # Case 2: If smaller input does not divides the larger input
    while True:
        # Find quotient and remainder when a is divided by b
        q = a // b
        r = a % b
        print(f"{a} = {b} * {q} + {r}")
        a = b
        b = r
        if r == 0:
            # If remainder is 0, print the GCD as remainder from previous step
            print(f"GCD({_a}, {_b}) = {prev}")
            gcd = prev
            break
        # Save remainder from the current step to pass to next step
        prev = r
