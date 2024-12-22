# forward recursion
def print_num(n, t):
    if n > t:
        return
    print(n)
    print_num(n + 1, t)


# backtracking or backward recursion
def print_num(n, t):
    if n < 1:
        return
    print_num(n - 1, t)
    print(n)


# functional recursion
def sum_(n):
    if n == 0:
        return 0
    return n + sum(n - 1)


# parameterized recursion
def sum_(n, s):
    if n<1:
        return s
    return sum(n-1, s+n)


if __name__ == "__main__":
    print_num(1, 10)
