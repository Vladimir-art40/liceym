r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
g = input()
a1 = r[r.rfind(g[0]) - 3]
a2 = r[r.rfind(g[len(g) // 2]) - 3]
a3 = r[r.rfind(g[-2]) - 3]
a4 = r[r.rfind(g[-1]) - 3]
print(a1, a2, a3, a4, sep='')

