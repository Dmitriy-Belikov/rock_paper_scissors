import random

import easygui as g
from easygui import easygui



def rock_paper_scissors():
    i = True

    while i:
        b_ot = ['Камень', 'Ножницы', 'Бумага']
        bot = random.choice(b_ot)
        choices = ['Камень', 'Ножницы', 'Бумага']
        y = g.buttonbox(msg='Игра "Камень, Ножницы, Бумага"', title='Выберите один из вариантов', choices=(choices))
        if bot == y:

            n = g.boolbox(msg='Ничья! Повторим?', title=' ', choices=('Да', 'Нет'), image=None, default_choice='Yes',
                cancel_choice='No')
            n
            if n is False or n is None:
                i = False
                break
            else:
                continue
        elif bot == 'Камень' and y == 'Ножницы' or bot == 'Ножницы' and y == 'Бумага' or bot == 'Бумага' and y == 'Камень':

            p = g.boolbox(msg='Вы проиграли, повторим?', title=' ', choices=('Да', 'Нет'), image=None, default_choice='Yes',
                cancel_choice='No')
            p
            if p is False or p is None:
                i = False
                break
            else:
                continue
            pob = g.boolbox(msg='Поздравляю! Вы победили! Повторим?', title=' ', choices=('Да', 'Нет'), image=None, default_choice='Yes',
                cancel_choice='No')
            pob
            if pob is False or pob is None:
                i = False
                break
            else:
                continue

def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = g.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()