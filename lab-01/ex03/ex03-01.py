numbers = [12, 5, 8, 20, 3, 15, 6, 9]
tong_chan = 0
for num in numbers:
    if num % 2 == 0:
        tong_chan += num
print("Danh sách:", numbers)
print("Tổng các số chẵn là:", tong_chan)