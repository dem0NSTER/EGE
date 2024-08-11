from itertools import product

words = []

for i in product('хацкер', repeat=5):
    word = ''.join(i)
    words.append(word)

words.sort()
words.reverse()
for word in words:
    if word.count('х') == 1 and word.count('ц') == 1:
        if len(set(word)) == 5:
            res = word
            break
words.reverse()
print(words.index(res) + 1)
