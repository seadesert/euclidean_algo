"""
Euclidean algorithm for finding the Greatest Common Divisor of two numbers, a and b,
and finding suitable x and y such that ax+by=GCD(a, b)  
(Verbose)
"""
a = abs(int(input("Enter value of a: ")))
b = abs(int(input("Enter value of b: ")))

_a = a
_b = b
stack = []
# Swap numbers if first input is smaller the second input
if a < b:
    a, b = b, a

# Case 1: If smaller input divides the larger input
if a % b == 0:
    gcd = min([a, b])
    print(f"GCD({_a}, {_b}) = {gcd}")
    print(f"{gcd} = {a} + {b} * {-(a//b - 1)}")
    print(f"x = {1}, y = {-(a//b - 1)}")
else:
    # Case 2: If smaller input does not divides the larger input
    while True:
        # Find quotient and remainder when a is divided by b
        q = a // b
        r = a % b
        print(f"{a} = {b} * {q} + {r}")
        # Push the equation to stack (For finding suitable x and y)
        stack.append([a, b, q, r])
        a = b
        b = r
        if r == 0:
            # If remainder is 0, print the GCD as remainder from previous step
            print(f"GCD({_a}, {_b}) = {prev}")
            gcd = prev

            # Finding suitable x and y
            # Pop last element from stack and initilize value of x and y
            a, b, q, r = stack.pop()
            x = b
            a, b, q, r_ = stack[-1]
            y = q
            # Step counter, i
            i = 0
            while True:
                i+=1
                a, b, q, r = stack.pop()
                # If #steps is even, x is negetive and y is possitive
                if i%2 == 0:
                    print(f"{gcd} = {a} * {-x} + {b} * {y}, {gcd == a * (-x) + b * y}")
                else:
                    # If #steps is odd, x is possitive and y is negetive
                    print(f"{gcd} = {a} * {x} + {b} * {-y}, {gcd == a * x + b * (-y)}")
                # Stop if stack is empty
                if len(stack) > 0:
                    a, b, q_, r_ = stack[-1]
                    x, y = y, (y*q_ + x)
                else:
                    if i%2 == 0:
                        print(f"x = {-x}, y = {y}")
                    else:
                        print(f"x = {x}, y = {-y}")
                    break
            break
        # Save remainder from the current step to pass to next step
        prev = r
