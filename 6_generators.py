# create fib generator
def fib(limit):
    nums = []
    current, nxt = 0, 1
    while len(nums) < limit:
        current, nxt = nxt, current + nxt
        nums.append(current)

    return nums


fibs = fib(10)
print(fibs)

for n in fibs:
    if n > 20:
        break

    print(f'Processing {n}')
print('Done')


def fib_gen():  # with generator
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


for n in fib_gen():
    if n > 20:
        break

    print(f'Processing {n}')
print('Done!')


# chain it

def odds(nums):
    for n in nums:
        if n % 2 == 1:
            yield n


nums = fib_gen()
odd_nums = odds(nums)

print(type(odd_nums))

for o in odd_nums:
    print(o)
    if o > 100:
        break
