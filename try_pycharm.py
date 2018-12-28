import datetime
import math

def printmorning():
    print("Good morning!")

today = datetime.datetime.today()
name = "Ping"
age = 45

print("Hello your name is %s" % name)
print("Hello your name is %s, my age is %d" % (name, age))
print("hi, Annie!")
print("Today is ", today)
print("Today is ", today.strftime("%A"))

printmorning()

# small story: there is a bank, giving you a APR 6% for your saving account
# if you have $1 at the bank, how much you will have after 12 years.

# (1 + apr) ** N
apr = 0.06
init = 1.0
sum = (1.0 +  apr) ** 12
print("The total will be %f" % sum)

sum1 = 1.0
for y in range(1, 13):
    sum1 *= (1.0 + apr)
print("The total will be %f" % sum1)

numberofyears = 100000
years = range(1, numberofyears + 1)
sum2 = 1.0
apr = 1.0 / numberofyears

for y in years:
    sum2 *= (1.0 + apr)
    print("After year %d, value is %f" % (y, sum2))


# Now compute constant e
print("math.e = %f" % math.e)