def power_of_digits(n, p):
    sum_ = 0
    while n > 0:
        d = n % 10
        n = n / 10
        sum_ = sum_ + pow(d, p)
    return sum_

print sum(n for n in xrange(2, 200000) if power_of_digits(n, 5) == n)