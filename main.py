startsequence = [0, 1]
terms = 5

print(f"{startsequence[0]}\n{startsequence[-1]}")
i = 0
while terms >= i:
    startsequence.append(startsequence[-1] + startsequence[-2])
    print(startsequence[-1])
    i += 1
