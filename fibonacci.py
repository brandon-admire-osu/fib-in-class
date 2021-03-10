def fib(n):
    output = []
    count = 0
    n1, n2 = 0, 1
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise ValueError
    elif n == 1:
        return [0]
    else:
        while count < n:
            output.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return output


def fact(n):
    count = n
    total = 1
    if not isinstance(n, int):
        raise ValueError
    if n < 1:
        raise ZeroDivisionError
    while count > 1:
        total = count * total
        count -= 1
    return total


print(fact(5))
