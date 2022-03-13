a = int(input())
print(1, *[k if k % 4 != 0 else str(k) + '; АХ! ' + ((str(k + 1)) if k + 1 <= a else '')
           for k in range(1, a + 1) if k % 4 != 1], sep=', ')

