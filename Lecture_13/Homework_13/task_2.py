words = ["python", "generator", "yield", "code", "ai", "developer"]

gen = (words.upper() for words in words if len(words) > 4)

for words in gen:
    print(words)
