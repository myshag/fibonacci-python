def fibonacci(n):
    """
    Генерирует первые n чисел Фибоначчи.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result


if __name__ == "__main__":
    fib_numbers = fibonacci(15)
    print('Первые 15 чисел Фибоначчи:')
    print(fib_numbers)
    print('Сумма:', sum(fib_numbers))
