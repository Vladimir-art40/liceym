import sys
import random


def logout():
    print('Не, так не правильно, прощайте!')
    sys.exit(0)


def out(data, right):
    print('\033[' + str(random.randint(31, 37)) + 'm{}' .format(data), end="\n> ")
    f = input()
    if f.lower() != right:
        logout()


print('Здравствуйте! Я задаю вопросы, вы отвечаете. Все просто.')
out('1) Вы учитель?', 'да')
out('2) Вам нравится этот язык программирования?', 'нет')
out('3) 2 + 2 = ?', '4')
out('4) Курсы по олимпиадному программированию будут?', 'да')
out('5) Точно будут?', 'да')
print('Вы успешно прошли тест!')



