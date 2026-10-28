words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}
for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print(word_counts)

reapeted_words = {w: counts for w, counts in word_counts.items() if counts > 1}
print(reapeted_words)


 




