squares = [x**2 for x in range(1, 11)]
print(squares)

words = ["apple","mango","kiwi","egg","cherry","bread","me"]

long_words = []

for word in words:
    if len(word) >= 5:
        long_words.append(word)

print(long_words)