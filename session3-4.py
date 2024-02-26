print("hello world again!")
print("hello world again! this is a new change")
print(5/5)

a = 5
b = 5
print(a, b, id(a), id(b))
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b, id(a), id(b))
print(a is b)

a.append(4)
print(a, b, id(a), id(b))
print(a is b)
print(a == b)

# SIEVE OF ERATOSTHENES
# Create a list of the first n numbers.
n = 100
x = list(range(2, n+1))

for i in x:
    j = 2
    while (i * j <= x[-1]):
        if (i * j in x):
            x.remove(i*j)
        j += 1

print("The list of prime numbers is:", x)

print(type(2))
print(type(2.3))
print((type(False)))
print(type(None))
print(type(4*2))
print(type(4/2))
print(type(3.0*1.0))
print(type(~3))
print(type(3|2))
print(type("xx"))

print("hello")
print(5 + 2 - 9)
print(2 + 3 * 5)
print(--5)
print(4/2)
print(3.0*1.0)
print(2 ** 3 + 1)
print(2 ** (3 + 1.0))
print(2 < 3 < 1)
print(3 > 0 ** 0 * 4)
print(2 > 1 and 5)

prompt = 'What is the speed of the car?'
speed = input(prompt)
int(speed) + 17

