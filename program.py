def read_file(input):
    a = []
    with open(input, 'r') as f:
        for line in f.readlines():
            try:
                a += list(map(int, line.split()))
            except ValueError:
                exit('Найдены непонятные символы в файле. Работа программы аварийно прекращена.')
                return ValueError
    return a


def sum_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    print("Сумма:", sum(arr))
    print()
    return sum(arr)


def mult_array(input):
    arr = read_file(input)
    mult = 1
    for i in arr:
        mult *= i
        if mult > 1000 ** 10:
            print("В файле:")
            print(*arr)
            print("Произведение привышает 1000^10. Процесс остановлен.")
            print()
            return mult
    print("В файле:")
    print(*arr)
    print("Произведение:", mult)
    print()
    return mult


def min_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    print("Минимальное: ", min(arr))
    print()
    return min(arr)


def max_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    print("Максимальное: ", max(arr))
    print()
    return max(arr)


def write_file(input, arr):
    with open(input, 'w') as f:
        for i in arr:
            f.write(str(i) + " ")


def write_file(input, arr):
    with open(input, 'w') as f:
        for i in arr:
            f.write(str(i) + " ")
