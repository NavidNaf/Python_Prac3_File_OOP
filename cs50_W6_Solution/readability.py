string = input("Text: ")

# letter count
letters = 0
for c in string:
    if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
        letters += 1
# print(letters)

# word count
wordsList = string.split()
words = len(wordsList)
# print(words)

# sentence count
sentence = string.count(".") + string.count("?") + string.count("!")
# print(sentence)

# indexing
L = (letters / words) * 100
S = (sentence / words) * 100

index = 0.0588 * L - 0.296 * S - 15.8
index = round(index)

if index > 16:
    print(f"Grade 16+")
elif index < 1:
    print(f"Before Grade 1")
else:
    print(f"Grade {index}")
