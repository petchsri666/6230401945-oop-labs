with open("kku.txt", "r", encoding='utf8') as f:
    file = f.read()
with open("kku2.txt", "w", encoding='utf8') as d:
    d.write(file)
    d.write("\nMotto: วิทยา จริยา ปัญญา")
    d.write("\nMotto in English: Knowledge, Virtues, Wisdom")
    d.close()
i = open("kku2.txt", "r", encoding='utf8')
print(i.read())
