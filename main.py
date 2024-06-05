import pygame
import pygame_menu
from game import game
from classes import name, scores
from sql import *

pygame.init()


'''Создаем окно заставки'''
menu_image = pygame.image.load("menu.jpg")
surface = pygame.display.set_mode((400, 600))
timer = pygame.time.Clock()


def start_game_button():
    global name
    global password
    name = user_name.get_value()
    password = user_pass.get_value()
    print(f"Игра запущена с пользователем {name}")

    if reg_user(name):
        start_game_button(name, password)
    # else:
        # print(' reg_user(name, password) = False')

    if (name, password):
        game(name, scores)
    else:
        return



'''Создаем объект класса меню'''
menu = pygame_menu.Menu(
    title='Игра',
    height=300,
    width=240,
    theme=pygame_menu.themes.THEME_BLUE
)
''' Настраиваем пункты меню'''
user_name = menu.add.text_input('Имя: ', default='User', maxchar=10)
user_pass = menu.add.text_input('Пароль: ', default='123', maxchar=10)
menu.add.button('Игра', start_game_button)
menu.add.button('Выход', pygame_menu.events.EXIT)

'''Запускаем основной цикл меню'''
def mainloop(win):
    while True:
        win.blit(menu_image, (0, 0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if menu.is_enabled():
            menu.update(events)
            menu.draw(win)

        pygame.display.update()
        timer.tick(60)




if __name__ == "__main__":
    mainloop(surface)
    game(name, scores)
