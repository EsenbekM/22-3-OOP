def pair_sum(a, b):  # O(1)
    return a + b


def pair_sum_sequence(n):  # O(n)
    result = 0
    for i in range(n):
        result += i
    return result


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = ['g', 'f', 'e', 'd', 'c', 'b', 'a']


def ex_1():  # O(N+N) = N + N = 2N = N    O(N)
    for a in arr1:
        print(a)
    for b in arr2:
        print(b)


def ex_2():  # O(N*N) = N * N = N**2 = O(N**2)
    for i in arr1:
        for j in arr2:
            print(i, j)

# ex_1()
# ex_2()
