year = int(input("Nhập năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")