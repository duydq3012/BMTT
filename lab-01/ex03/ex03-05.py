words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Danh sách từ:", words)
print("Số lần xuất hiện:", word_counts)