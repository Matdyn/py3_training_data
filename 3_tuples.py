# create a tuple
m = .4,  # the coma matter
print(type(m), m)

m = (.4, .9, 4, 18.9)
print(type(m), m)

# unpack a tuple
x, y, _, _ = m
print(x, y)

x, y = y, x
print(x, y)


# These numbers looks familiar...

n = [1, 1, 2, 3, 5, 8, 13, 21]

for f in n:
    print(f, end=', ')
print()
print()

for idx, f in enumerate(n):
    print(f'{idx + 1}. {f} ')


# Show the ith fibonacci number

# example: fibonacci generator with simple(est?) algorithm
def fib(limit):
    nums = []
    current = 0
    nxt = 1
    while len(nums) < limit:
        #nums.append(current)
        #current, nxt = nxt, current + nxt
        temp = current
        current = nxt
        nxt = temp + current
        nums.append(current)
    return nums

print(fib(7))


def fib_2(limit):
     nums = []
     current, nxt = 0, 1
     while len(nums) < limit:
         current, nxt = nxt, current + nxt
         nums.append(current)
     return nums

print(fib_2(7))