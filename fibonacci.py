# Задача на программирование: небольшое число Фибоначчи
# Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи 
# (напомним, что F0 = 0, F1 = 1 и Fn = Fn−1 + Fn−2 при n ≥ 2).

def fib(n):
    lst = [1, 1]
    if n == 1 or n == 2:
        return lst[n-1]
    for i in range(2, n):
        f = lst[i-1] + lst[i-2]
        lst.append(f)
    print(lst)
    return lst[-1]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()