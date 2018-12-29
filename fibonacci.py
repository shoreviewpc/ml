# preset fibonacciCache list to initial value 0
fibonacciCache = [0 for x in range(0, 2000)]

def fibonacci(n):
    # check if we already compute fibonacci(n) and store the result int the
    # fibonacci cache, if so, don't compute again, just return the value already exist to save
    # computing time
    if fibonacciCache[n] != 0:
        return fibonacciCache[n]
    if n == 1 or n == 2:
        fibonacciCache[n] = 1
    else:
        fibonacciCache[n] = fibonacci(n - 1) + fibonacci((n - 2))
    return fibonacciCache[n]

# Quick simple test to calculate fibonacci(10)
fib = 10
print("{}! = {}".format(fib, fibonacci(fib)))

# Compute gold ratio
for i in range (2, 1001):
    print("%d - fibonacci(%d) / fibonacci(%d) = %f " % (i, i - 1, i, fibonacci(i-1)/fibonacci(i)))