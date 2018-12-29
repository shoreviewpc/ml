# compute factorial using the for loop (non-recursive version)
def calcfactorial(n):
    product = 1
    for x in range(1, num + 1):
        product *= x
    return product

num = 10
print("{}! = {}".format(num, calcfactorial(num)))

# recursion problem
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print("{}! = {}".format(num, recursive_factorial(num)))


