scores = [45, 82, 67, 38, 90, 55, 72]
passing_scores = list (filter(lambda x: x >= 50, scores ))

passing_scores = list(map(lambda x: x + 5 if x + 5 <= 100 else 100, passing_scores))
print(passing_scores)

