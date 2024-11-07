try:
    n = int(input())
    lst = []
    for i in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))
    max_sum = 0
    for i in range(2 ** n):
        operating_sum = 0
        for j in range(n):
            if (i > j) and 1:
                operating_sum += lst[j][0]
            else:
                operating_sum += lst[j][1]
                if operating_sum % 3 == 0:
                    max_sum = max(max_sum, operating_sum)
    print(max_sum)
except(ValueError):
    print('цифрами')