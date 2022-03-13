a = input()
a1 = a.__contains__('лилипут') or a.__contains__('Лилипут') or a.__contains__('ЛИЛИПУТ')
a2 = a.__contains__('великан') or a.__contains__('Великан') or a.__contains__('ВЕЛИКАН')
if (a1 and a2) or (not a1 and not a2):
    print('Я совсем запутался.')
elif a1:
    print('В Лилипутии.')
else:
    print('В Великании.')

