def analyze_text(text, min_length = 3, ignore_stopwords = None):
    if ignore_stopwords is None:
        ignore_stopwords = []
    words = text.split()
    count = 0 
    for w in words:
        if len(w) >= min_length and w not in ignore_stopwords:
            count += 1
    return count
print(analyze_text("I want to learn Python programming"))

        

