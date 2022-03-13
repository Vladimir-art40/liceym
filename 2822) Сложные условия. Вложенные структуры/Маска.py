a = input()
if (not a.__contains__(" ")) and (a.__contains__('*') or a.__contains__('?')):
    print('Возможно маска')
else:
    print('Нет, это не маска!')

