# Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю
# Даны целые числ 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от деления 
# n-го числа Фибоначчи на m.

def fib_mod(n, m):
    lst = [0, 1]
    period = 1
    for i in range(2, n+1):
        next = (lst[i-2] + lst[i-1]) % m
        period = period + 1
        if lst[i-1] == 1 and next == 0:
            return lst[n % period]
        lst.append(next)
    return lst[-1]

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

# 1025 55 - 5

# 12589 369 - 89
# 1598753 25897 - 20305

# "n": "1598753", "m": 25897, "expected": 20305 