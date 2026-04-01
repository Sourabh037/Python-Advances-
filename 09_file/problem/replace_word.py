words = ["shape", "still", "some"]

with open("problem/words.txt") as f:
    content = f.read()

for words in words:
    content = content.replace(words, "#"*len(words))

with open("problem/words.txt", "w") as f:
    f.write(content)