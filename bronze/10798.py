table = []
for i in range(5):
    word = input()
    if len(word) < 15:
        word += " " * (15 - len(word))
    table.append(word)

for i in range(15):
    for j in range(5):
        if table[j][i] != " ":
            print(table[j][i], end="")