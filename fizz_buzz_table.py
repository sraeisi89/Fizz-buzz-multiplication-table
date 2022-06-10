# first solution
def fizz_buzz_table(n):
    arr = []
    counter = 1
    for i in range(n):
        col = []
        for j in range(1, n+1):
            col.append(j * counter)
        arr.append(col)
        counter += 1

    for items in arr:
        for i in range(n):
            if items[i] % 3 == 0 and items[i] % 5 == 0:
                items[i] = "FizzBuzz"
            elif items[i] % 3 == 0:
                items[i] = "Fizz"
            elif items[i] % 5 == 0:
                items[i] = "Buzz"
    print(arr)
fizz_buzz_table(3)

# second solution
def fizz(n):
    matrix = []
    for r in range(1, n+1):
        matrix.append([c*r for c in range(1, n+1)])

    for items in matrix:
        for i in range(n):
            if items[i] % 3 == 0 and items[i] % 5 == 0:
                items[i] = "FizzBuzz"
            elif items[i] % 3 == 0:
                items[i] = "Fizz"
            elif items[i] % 5 == 0:
                items[i] = "Buzz"
    print(matrix)
fizz(3)





