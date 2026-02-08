import math
n = int(input("Nhập số nguyên dương: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")