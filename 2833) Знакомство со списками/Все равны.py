h = []
e = input()
max_word_len = 0
while e != '':
    max_word_len = max(max_word_len, len(e))
    h.append(e)
    e = input()
h.reverse()
for t in h:
    print('-' * ((max_word_len - len(t)) // 2) + t
          + '-' * ((max_word_len - len(t)) % 2) + '-' * ((max_word_len - len(t)) // 2))

