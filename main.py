import pygame
from screens import start_screen, rules_screen, winscreen
import time
import sys
from player import Playerstay, Playersit, Playerjump, Playerattack, Playerdeath, Playerrun
from hud import HPbar
from tools import load_image


if __name__ == '__main__':
    pygame.init()
    FPSM = 60
    clock = pygame.time.Clock()
    width, height = 1070, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('the game')
    button_objects = []
    start_screen(screen, clock, button_objects, width, height, FPSM)
    timerules = time.time()
    rules_screen(screen, clock, width, height, timerules, FPSM)

    size = width, height = 1360, 640    # 1700, 800
    GRAVITY = 10
    screen_rect = (0, 0, width, height)
    screen = pygame.display.set_mode(size)

    all_sprites_stay1 = pygame.sprite.Group()
    all_sprites_run1 = pygame.sprite.Group()
    all_sprites_jump1 = pygame.sprite.Group()
    all_sprites_sit1 = pygame.sprite.Group()
    all_sprites_attack1 = pygame.sprite.Group()

    all_sprites_stay2 = pygame.sprite.Group()
    all_sprites_run2 = pygame.sprite.Group()
    all_sprites_jump2 = pygame.sprite.Group()
    all_sprites_sit2 = pygame.sprite.Group()
    all_sprites_attack2 = pygame.sprite.Group()

    all_sprites_cody_death = pygame.sprite.Group()
    all_sprites_akira_death = pygame.sprite.Group()

    image = pygame.transform.scale(load_image('fon.jpg'), (1360, 640))  # (1700, 800)

    pl1_HPbar = HPbar(12, 12, False)    # 12, 12
    pl2_HPbar = HPbar(800, 12)          # 1000, 15

    pl1_pos = [80, 240]     # [100, 300]

    pl_stay1 = load_image('player1_stay.png', -1, size=0.8)
    pl_run1 = load_image('player1_run.png', -1, size=0.8)
    pl_at1 = load_image('player1_attack.png', -1, size=0.8)
    pl_sit1 = load_image('player1_sit.png', -1, size=0.8)
    pl_jump1 = load_image('player1_jump.png', -1, size=0.8)
    pl_de1 = load_image('cody_death.png', -1, size=0.8)

    player_de1 = Playerdeath(pl_de1, 6, 1, pl1_pos[0], pl1_pos[1], all_sprites_cody_death, False)
    player_ju1 = Playerjump(pl_jump1, 6, 1, pl1_pos[0], pl1_pos[1], all_sprites_jump1, False)
    player_sit1 = Playersit(pl_sit1, 5, 1, pl1_pos[0], pl1_pos[1], all_sprites_sit1, False)
    player_at1 = Playerattack(pl_at1, 5, 1, pl1_pos[0], pl1_pos[1], all_sprites_attack1, False)
    player_st1 = Playerstay(pl_stay1, 2, 1, pl1_pos[0], pl1_pos[1], all_sprites_stay1, False)
    player_ru1 = Playerrun(pl_run1, 8, 1, pl1_pos[0], pl1_pos[1], all_sprites_run1, False)

    pl2_pos = [1040, 206]   # [1300, 257]

    pl_stay2 = load_image('player_stay.png', -1, size=0.8)
    pl_run2 = load_image('player_run.png', -1, size=0.8)
    pl_jump2 = load_image('player_jump.png', -1, size=0.8)
    pl_sit2 = load_image('player_sit.png', -1, size=0.8)
    pl_at2 = load_image('player_attack.png', -1, size=0.8)
    pl_de2 = load_image('booom.png', -1, size=0.8)

    player_at2 = Playerattack(pl_at2, 11, 1, pl2_pos[0], pl2_pos[1], all_sprites_attack2)
    player_sit2 = Playersit(pl_sit2, 6, 1, pl2_pos[0], pl2_pos[1], all_sprites_sit2)
    player_ju2 = Playerjump(pl_jump2, 11, 1, pl2_pos[0], pl2_pos[1], all_sprites_jump2)
    player_st2 = Playerstay(pl_stay2, 10, 1, pl2_pos[0], pl2_pos[1], all_sprites_stay2)
    player_ru2 = Playerrun(pl_run2, 11, 1, pl2_pos[0], pl2_pos[1], all_sprites_run2)
    player_de2 = Playerdeath(pl_de2, 3, 2, pl2_pos[0], pl2_pos[1], all_sprites_akira_death)

    time = 0
    counter = 10

    font = pygame.font.Font(None, 120)  # 150
    font1 = pygame.font.Font(None, 80)  # 100
    name = font1.render('Akira', True, 'White')
    name1 = font1.render('Cody', True, 'White')
    text_x = 572        # 715
    text_y = 16         # 20
    safe_zone = 184     # 230
    fps = 10

    Cody_is_win = False
    Akira_is_win = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        screen.blit(image, (0, 0))
        time1 = time // 1000 // 60
        if time1 < 10:
            time1 = '0' + str(time1)
        time2 = time // 1000 % 60
        if time2 < 10:
            time2 = '0' + str(time2)
        text = font.render(f'{time1}:{time2}', True, (255, 200, 0))
        screen.blit(text, (text_x, text_y))
        screen.blit(name1, (12, 92))        # (15, 115)
        screen.blit(name, (1200, 92))       # (1500, 115)
        pl1_HPbar.render(screen)
        pl2_HPbar.render(screen)
        keys = pygame.key.get_pressed()
        if Cody_is_win:
            all_sprites_stay1.draw(screen)
            player_st1.update()
            all_sprites_akira_death.draw(screen)
            player_de2.update()
            counter -= 1
            if counter == 0:
                break
        elif Akira_is_win:
            all_sprites_stay2.draw(screen)
            player_st2.update()
            all_sprites_cody_death.draw(screen)
            player_de1.update()
            counter -= 1
            if counter == 0:
                break
        else:
            if (keys[pygame.K_w] or player_ju1.is_jumping) and not player_at1.is_attacking:
                player_sit1.is_sitting = False
                player_ju1.is_jumping = True
                player_ju1.update()
                all_sprites_jump1.draw(screen)
            elif keys[pygame.K_LALT] or player_at1.is_attacking:
                player_sit1.is_sitting = False
                player_sit1.cur_frame = 0
                player_at1.is_attacking = True
                player_at1.update()
                all_sprites_attack1.draw(screen)
                if abs(pl1_pos[0] - pl2_pos[0]) < safe_zone + 20 and player_at1.cur_frame == 4 \
                        and not player_sit2.is_sitting:  # 25
                    pl2_HPbar.hp -= 1
                    if pl2_HPbar.hp == 0:
                        Cody_is_win = True
            elif keys[pygame.K_d] and pl1_pos[0] < 1160 and abs(pl1_pos[0] - pl2_pos[0]) > safe_zone:   # 1450
                player_ru1.way = 1
                player_sit1.cur_frame = 0
                all_sprites_run1.draw(screen)
                player_ru1.update(pl1_pos, pl2_pos)
            elif keys[pygame.K_s]:
                player_sit1.is_sitting = True
                player_sit1.update()
                all_sprites_sit1.draw(screen)
            elif keys[pygame.K_a] and 0 < pl1_pos[0]:
                player_sit1.is_sitting = False
                player_ru1.way = -1
                player_sit1.cur_frame = 0
                all_sprites_run1.draw(screen)
                player_ru1.update(pl1_pos, pl2_pos)
            else:
                player_sit1.is_sitting = False
                player_sit1.cur_frame = 0
                all_sprites_stay1.draw(screen)
                player_st1.update()
            player_de1.update_pos(pl1_pos, pl2_pos)
            player_ju1.update_pos(pl1_pos, pl2_pos)
            player_ru1.update_pos(pl1_pos, pl2_pos)
            player_st1.update_pos(pl1_pos, pl2_pos)
            player_at1.update_pos(pl1_pos, pl2_pos)
            player_sit1.update_pos(pl1_pos, pl2_pos)

            if (keys[pygame.K_UP] or player_ju2.is_jumping) and not player_at2.is_attacking:
                player_sit2.is_sitting = False
                player_ju2.is_jumping = True
                player_ju2.update()
                all_sprites_jump2.draw(screen)
            elif keys[pygame.K_RCTRL] or player_at2.is_attacking:
                player_sit2.is_sitting = False
                player_at2.is_attacking = True
                all_sprites_attack2.draw(screen)
                player_at2.update()
                if abs(pl1_pos[0] - pl2_pos[0]) < safe_zone + 20 and player_at2.cur_frame == 5 \
                        and not player_sit1.is_sitting:     # 25
                    pl1_HPbar.hp -= 2
                    if pl1_HPbar.hp == 0:
                        Akira_is_win = True
            elif keys[pygame.K_RIGHT] and pl2_pos[0] < 1160:        # 1450
                player_sit2.is_sitting = False
                player_ru2.way = -1
                player_sit2.cur_frame = 0
                all_sprites_run2.draw(screen)
                player_ru2.update(pl1_pos, pl2_pos)
            elif keys[pygame.K_DOWN]:
                player_sit2.is_sitting = True
                player_sit2.update()
                all_sprites_sit2.draw(screen)
            elif keys[pygame.K_LEFT] and 0 < pl2_pos[0] and abs(pl1_pos[0] - pl2_pos[0]) > safe_zone:
                player_sit2.is_sitting = False
                player_ru2.way = 1
                player_sit2.cur_frame = 0
                all_sprites_run2.draw(screen)
                player_ru2.update(pl1_pos, pl2_pos)
            else:
                player_sit2.is_sitting = False
                player_sit2.cur_frame = 0
                all_sprites_stay2.draw(screen)
                player_st2.update()
            player_at2.update_pos(pl1_pos, pl2_pos)
            player_ru2.update_pos(pl1_pos, pl2_pos)
            player_ju2.update_pos(pl1_pos, pl2_pos)
            player_sit2.update_pos(pl1_pos, pl2_pos)
            player_st2.update_pos(pl1_pos, pl2_pos)
            player_de2.update_pos(pl1_pos, pl2_pos)

            time += clock.get_time()

        clock.tick(fps)
        pygame.display.flip()

    width, height = 1070, 600
    screen = pygame.display.set_mode((width, height))
    if Akira_is_win:
        winscreen(screen, clock, width, height, 'Akira', time1, time2, FPSM)
    else:
        winscreen(screen, clock, width, height, 'Cody', time1, time2, FPSM)

    pygame.quit()
