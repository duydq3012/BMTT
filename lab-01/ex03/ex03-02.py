arr = [1, 2, 3, 2, 4, 1, 5]
# Đảo ngược
arr.reverse()
print("List sau khi đảo ngược:", arr)

# Xóa trùng (cách đơn giản nhất là chuyển sang Set rồi về List)
unique_arr = list(set(arr))
print("List sau khi xóa trùng:", unique_arr)