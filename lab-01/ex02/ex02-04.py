n = int(input("Nhập số cần tính giai thừa: "))
giaithua = 1
for i in range(1, n + 1):
    giaithua *= i
print(f"Giai thừa của {n} là: {giaithua}")