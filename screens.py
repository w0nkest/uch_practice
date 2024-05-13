from tools import load_image
import sys, time
import pygame
from button import Button
STARTGAME = False


def playfunc():
    global STARTGAME
    STARTGAME = True


def terminate():
    print("TERMINATION")
    pygame.quit()
    sys.exit()


def start_screen(screen, clock, button_objects, width, height, FPSM=60):
    global STARTGAME
    intro_text = ["Файтинг"]

    fon = pygame.transform.scale(load_image('bgmenu1.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    Button(width - int(175 * (width / 1070)), int(50 * (height / 600)), 150, 70, button_objects, 'Играть', playfunc)
    Button(width - int(205 * (width / 1070)), height - int((70 * (height / 600))), 150, 50, button_objects, 'выход',
           terminate)
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - intro_rect.width // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif STARTGAME:
                return
        for obj in button_objects:
            obj.process(screen)
        pygame.display.flip()
        clock.tick(FPSM)


def winscreen(screen, clock, width, height, name, time1, time2=0, FPSM=60):
    intro_text = [f'{name} победил!',
                  'Поздравляем!',
                  f'длительность вашего матча: {time1}:{time2}',
                  ]

    fon = pygame.transform.scale(load_image('endscreenbg.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('comicsansms', 40)
    text_coord = 50
    player_win = load_image(f'{name}_win.png', -1)
    screen.blit(player_win, (700, 80))

    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 40
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        pygame.display.flip()
        clock.tick(FPSM)


def rules_screen(screen, clock, width, height, timerules, FPSM=60):
    intro_text = ["СВОДКА ПРАВИЛ",
                  "(нажмите в любом месте окна для продолжения)", "", "",
                  'Используйте "W", "A", "S", "D" для управления движением персонажем слева, "leftALT" для его атаки.',
                  'Используйте стрелочки для управления движением персонажа справа, "rightCTRL" для его атаки.',
                  'Проигрывает игрок, у которого закончилось здоровье.', '', '', '', 'Удачи!'
                  ]
    fon = pygame.transform.scale(load_image('pixelroad_bg2.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    # head text of rules screen
    mainfont = pygame.font.SysFont('comicsansms', 40)
    font = pygame.font.SysFont('comicsansms', 20)
    string_rendered = mainfont.render(intro_text[0], True, (252, 0, 0))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 50
    intro_rect.x = width // 2 - string_rendered.get_width() // 2
    text_coord = intro_rect.height + 50
    screen.blit(string_rendered, intro_rect)
    heightmaintext = string_rendered.get_height()

    # tip to skip rules screen
    string_rendered = font.render(intro_text[1], True, (252, 40, 71))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 50 + heightmaintext
    intro_rect.x = width // 2 - string_rendered.get_width() // 2
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    # rules text
    for line in intro_text[2:]:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN or \
                    int(time.time() - timerules) >= 10:
                return
        pygame.display.flip()
        clock.tick(FPSM)


if __name__ == '__main__':
    pygame.init()
    STARTGAME = False
    FPSM = 60
    clock = pygame.time.Clock()
    width, height = 1070, 600
    screen = pygame.display.set_mode((width, height))
    button_objects = []
    start_screen(screen, clock, button_objects, width, height, FPSM)
    timerules = time.time()
    rules_screen(screen, clock, width, height, timerules, FPSM)