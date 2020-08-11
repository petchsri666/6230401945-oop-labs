directory = {"manee": "1234", "mana": "4567", "chujai": "6789"}
t = [(keys, value) for keys, value in directory.items()]
print(t)

v = []
for i in directory.values():
    v.append(i)
print(v)

k = []
for i in directory.keys():
    k.append(i)
print(k)

word = "antidisestablishmentarianism"
first_sorted = sorted(word)
s2 = "".join(first_sorted)
print(s2)

w = "the quick brown fox jumped over the lazy dog".split()
print(w)
