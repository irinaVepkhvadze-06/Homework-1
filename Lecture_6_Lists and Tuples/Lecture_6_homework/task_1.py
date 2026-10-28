scores: list[int] = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)
print(scores)
scores.remove(45)
print(scores)
print(sum(scores) / len(scores))
print(max(scores))
print(min(scores))

scores.sort()
print(scores)


passed_scores: list[int] = []
for score in scores:
    if score >= 60:
        passed_scores.append(score)
print(passed_scores)