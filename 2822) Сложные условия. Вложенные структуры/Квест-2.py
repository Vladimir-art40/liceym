import sys
import random


def logout():
    print('Не, так не правильно, прощайте!')
    sys.exit(0)


def ok():
    print('Все верно, мне надоело это писать, прощайте!')
    sys.exit(0)


def out(data, right):
    print('\033[' + str(random.randint(31, 37)) + 'm{}'.format(data), end="\n> ")
    f = input()
    if f.lower() != right:
        logout()


def change(data):
    print('\033[' + str(random.randint(31, 37)) + 'm{}'.format('Для начала выберете наиболее интересную вас тему: '))
    a = 1
    for d in data:
        print('\033[' + str(random.randint(31, 37)) + 'm{}'.format(str(a) + ") " + d))
        a += 1
    f = input('> ')
    if f.isnumeric() and 0 < int(f) <= len(data):
        return int(f)
    else:
        logout()


themes = ['Логика', 'Правда', 'Математика']
tasks = [['Вы учитель?', 'Сколько яблок на груше?', 'А почему этот контест такой тупой?'],
         ['Вам нравится этот язык программирования?', 'Правда?', 'Занятия по олимпиадному программированию?'],
         ['3 + 3 = ?', '3 * 3 = ?', '3 ^ 3 = ?', '3 / 3 = ?']]
answers = [['да', '0', 'ничего не поделать, его гриша писал'],
           ['уже лучше', 'нет', 'хоть завтра'],
           ['6', '9', '27', '1']]
print('Здравствуйте! Я задаю вопросы, вы отвечаете. Все просто.')
alpha = change(themes)
counter = 1
for i in tasks[alpha - 1]:
    out(str(counter) + ') ' + i, answers[alpha - 1][counter - 1])
    counter += 1
ok()

