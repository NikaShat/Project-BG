import pygame
import os, sqlite3
import window, defaut_stats, hero_presentation, generate_levels, camera, classes, enemies

pygame.init()
size = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

startwindow = window.Window(screen)
startwindow.draw('start window.jpg')

# флаги, указывающие, какое сейчас открыто окно
Flag_start_window_on = True
Flag_rules_window_on = False
Flag_player_window_on = False
Flag_dialog_window_on = False
Flag_level_window_on = False
Flag_game_process_window_on = False
Flag_win_window_on = False

# флаги, указывающие, какой класс персонажа выбран
Flag_select_wizard = False
Flag_select_archer = False
Flag_select_barbarian = False
Flag_select_crusader = False
Flag_select_necromancer = False

# флаг камеры
Flag_camera_on = False

# музыка (главная тема)
pygame.mixer.init()
pygame.mixer.music.load('data/music/start_window_theme.mp3')
pygame.mixer.music.play(-1)

FPS = 50
STEP = 25

# смена картинки
different_images = 0
UPDATE_IMAGE = 30
pygame.time.set_timer(UPDATE_IMAGE, 3000)

# анимация движения монстров
UPDATE_ENEMIES = 30
pygame.time.set_timer(UPDATE_ENEMIES, 2500)

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group_not_collide = pygame.sprite.Group()
tiles_group_collide = pygame.sprite.Group()
health_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# подключение к БД
conn = sqlite3.connect("data/database.db", timeout=10, isolation_level=None)
curr = conn.cursor()

# проверка на сохранение
check = curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall()
if check[0][0] == -1:
    save_file_exist = False
else:
    save_file_exist = True

# текст кол-ва монет игрока
font = pygame.font.Font('data/game_font.ttf', 36)
BACKGROUND_TEXT_MONEY = (214, 221, 231)

running = True
while running:
    for event in pygame.event.get():
        # завершение программы
        if event.type == pygame.QUIT:
            running = False
        # обновление картинки заставки
        if event.type == UPDATE_IMAGE:
            if Flag_start_window_on:
                if different_images == 1:
                    startwindow = window.Window(screen)
                    startwindow.draw('start window bw.jpg')
                    different_images = 0
                else:
                    startwindow = window.Window(screen)
                    startwindow.draw('start window.jpg')
                    different_images = 1
        # анимация монстров
        if event.type == UPDATE_ENEMIES and Flag_game_process_window_on:
            for i in enemy_group:
                i.animation_move()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
            # кнопка "Старт" (начало игры)
            if 200 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250 and Flag_start_window_on:
                # при наличии сохранения открывается диалоговое окно
                if save_file_exist:
                    dialogwindow = window.Window(screen)
                    dialogwindow.draw('dialog window.jpg')
                    Flag_start_window_on = False
                    Flag_dialog_window_on = True
                # если сохранения нет, то открывается окно игрока
                else:
                    playerwindow = window.Window(screen)
                    playerwindow.draw('player window.jpg')
                    Flag_player_window_on = True
                    save_file_exist = True
                    curr.execute("""UPDATE player
                                    SET money = 50
                                    WHERE key = 1""").fetchall()
                    money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                    text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                    pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((390, 20), text_money.get_size()))
                    screen.blit(text_money, (390, 20))
                    Flag_start_window_on = False
            # кнопка "Да" в диалоговом окне (стирается сохранение)
            if 180 <= event.pos[0] <= 280 and 350 <= event.pos[1] <= 380 and Flag_dialog_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                defaut_stats.defaultstats(curr)
                curr.execute("""UPDATE player 
                                SET money = 50 
                                WHERE key = 1""").fetchall()
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((390, 20), text_money.get_size()))
                screen.blit(text_money, (390, 20))
                Flag_dialog_window_on = False
                Flag_player_window_on = True
            # кнопка "Нет" в диалоговом окне (возвращение к заставке)
            if 320 <= event.pos[0] <= 420 and 350 <= event.pos[1] <= 380 and Flag_dialog_window_on:
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
                Flag_start_window_on = True
                Flag_dialog_window_on = False
            # кнопка "Продолжить" при наличии сохранения
            if 200 <= event.pos[0] <= 400 and 300 <= event.pos[1] <= 350 and save_file_exist and Flag_start_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                Flag_start_window_on = False
                Flag_player_window_on = True
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((390, 20), text_money.get_size()))
                screen.blit(text_money, (390, 20))
            # кнопка "Правила"
            if 200 <= event.pos[0] <= 400 and 400 <= event.pos[1] <= 450 and Flag_start_window_on:
                ruleswindow = window.Window(screen)
                ruleswindow.draw('rules window.jpg')
                Flag_start_window_on = False
                Flag_rules_window_on = True
            # кнопка "Выход" (завершение программы)
            if 200 <= event.pos[0] <= 400 and 500 <= event.pos[1] <= 550 and Flag_start_window_on:
                running = False
            # кнопка закрытия правил
            if 520 <= event.pos[0] <= 600 and 0 <= event.pos[1] <= 30 and Flag_rules_window_on:
                Flag_rules_window_on = False
                Flag_start_window_on = True
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
            # кнопка "Сохранение"
            if 520 <= event.pos[0] <= 600 and 0 <= event.pos[1] <= 40 and Flag_player_window_on:
                curr.execute(f"""UPDATE player
                                SET money = {money_number}
                                WHERE key = 1""").fetchall()
                
            # кнопки выбора персонажа и его просмотра
            if 100 < event.pos[1] < 160 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('wizard', screen, curr)
                Flag_select_wizard = True
                Flag_select_archer = False
                Flag_select_barbarian = False
                Flag_select_crusader = False
                Flag_select_necromancer = False
            if 160 < event.pos[1] < 220 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('archer', screen, curr)
                Flag_select_wizard = False
                Flag_select_archer = True
                Flag_select_barbarian = False
                Flag_select_crusader = False
                Flag_select_necromancer = False
            if 220 < event.pos[1] < 280 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('barbarian', screen, curr)
                Flag_select_wizard = False
                Flag_select_archer = False
                Flag_select_barbarian = True
                Flag_select_crusader = False
                Flag_select_necromancer = False
            if 280 < event.pos[1] < 340 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('crusader', screen, curr)
                Flag_select_wizard = False
                Flag_select_archer = False
                Flag_select_barbarian = False
                Flag_select_crusader = True
                Flag_select_necromancer = False
            if 340 < event.pos[1] < 400 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('necromancer', screen, curr)
                Flag_select_wizard = False
                Flag_select_archer = False
                Flag_select_barbarian = False
                Flag_select_crusader = False
                Flag_select_necromancer = True
            # кнопка "Уровни" (переход к выбору уровня)
            if (450 < event.pos[1] < 520 and 20 < event.pos[0] < 250 and Flag_player_window_on and
               (Flag_select_archer or Flag_select_wizard or Flag_select_necromancer or Flag_select_barbarian or
               Flag_select_crusader)):
                
                levelwindow = window.Window(screen)
                levelwindow.draw('levels window.jpg')
                Flag_player_window_on = False
                Flag_level_window_on = True
            # кнопка "Выход" (переход к заставке)
            if 540 < event.pos[1] < 580 and 40 < event.pos[0] < 230 and Flag_player_window_on:
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
                Flag_start_window_on = True
                Flag_player_window_on = False
            # кнопка "Улучшить" (поднимает статы персонажей)
            if 370 <= event.pos[0] <= 500 and 540 <= event.pos[1] <= 570 and Flag_player_window_on:
                if Flag_select_necromancer and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'necromancer', 0, 0, curr, False)
                    upgrade_hero_stats.upgrade(money_number, screen)
                    money_number -= 100
                elif Flag_select_archer and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'archer', 0, 0, curr, False)
                    upgrade_hero_stats.upgrade(money_number, screen)
                    money_number -= 100
                elif Flag_select_wizard and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'wizard', 0, 0, curr, False)
                    upgrade_hero_stats.upgrade(money_number, screen)
                    money_number -= 100
                elif Flag_select_barbarian and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'barbarian', 0, 0, curr, False)
                    upgrade_hero_stats.upgrade(money_number, screen)
                    money_number -= 100
                elif Flag_select_crusader and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'crusader', 0, 0, curr, False)
                    upgrade_hero_stats.upgrade(money_number, screen)
                    money_number -= 100
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((390, 20), text_money.get_size()))
                screen.blit(text_money, (390, 20))
            # кнопка "Выход" (переход к окну игрока)
            if 530 < event.pos[1] < 580 and 230 < event.pos[0] < 370 and Flag_level_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((390, 20),  text_money.get_size()))
                screen.blit(text_money, (390, 20))
                Flag_level_window_on = False
                Flag_player_window_on = True
            # кнопка 1 уровня
            if 250 < event.pos[1] < 350 and 50 < event.pos[0] < 150 and Flag_level_window_on:
                if Flag_select_crusader:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'crusader', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_barbarian:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'barbarian', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_wizard:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'wizard', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_archer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'archer', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_necromancer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'necromancer', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                
                Flag_level_window_on = False
                game_camera = camera.Camera((level_x, level_y))
                Flag_camera_on = True
                Flag_game_process_window_on = True
            # кнопка 2 уровня
            if 250 < event.pos[1] < 350 and 250 < event.pos[0] < 350 and Flag_level_window_on:
                if Flag_select_crusader:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'crusader', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_barbarian:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'barbarian', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_wizard:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'wizard', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_archer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'archer', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_necromancer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'necromancer', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                Flag_level_window_on = False
                
                game_camera = camera.Camera((level_x, level_y))
                Flag_camera_on = True
                Flag_game_process_window_on = True
            # кнопка 3 уровня
            if 250 < event.pos[1] < 350 and 450 < event.pos[0] < 550 and Flag_level_window_on:
                if Flag_select_crusader:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'crusader', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_barbarian:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'barbarian', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_wizard:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'wizard', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_archer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'archer', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                elif Flag_select_necromancer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'necromancer', tiles_group_collide,
                                                                            tiles_group_not_collide, health_group,
                                                                            money_group, exit_group, enemy_group, curr)
                Flag_level_window_on = False
                
                game_camera = camera.Camera((level_x, level_y))
                Flag_camera_on = True
                Flag_game_process_window_on = True
            if Flag_win_window_on:
                levelwindow = window.Window(screen)
                levelwindow.draw('levels window.jpg')
                Flag_win_window_on = False
                Flag_level_window_on = True

                all_sprites.empty()
                tiles_group.empty()
                player_group.empty()
                tiles_group_not_collide.empty()
                tiles_group_collide.empty()
                health_group.empty()
                money_group.empty()
                exit_group.empty()
                enemy_group.empty()

        # передвижение
        if event.type == pygame.KEYDOWN and Flag_game_process_window_on:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                hero.rect.x -= STEP
                answer = hero.update(tiles_group_not_collide, tiles_group_collide, health_group, money_group, exit_group)
                if not answer[0]:
                    hero.rect.x += STEP
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                hero.rect.x += STEP
                answer = hero.update(tiles_group_not_collide, tiles_group_collide, health_group, money_group, exit_group)
                if not answer[0]:
                    hero.rect.x -= STEP
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                hero.rect.y -= STEP
                answer = hero.update(tiles_group_not_collide, tiles_group_collide, health_group, money_group, exit_group)
                if not answer[0]:
                    hero.rect.y += STEP
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                hero.rect.y += STEP
                answer = hero.update(tiles_group_not_collide, tiles_group_collide, health_group, money_group, exit_group)
                if not answer[0]:
                    hero.rect.y -= STEP
            if answer[1]:
                hero.healing()
            if answer[2]:
                money_number += 50
                curr.execute(f"""UPDATE player
                                        SET money = {money_number}
                                        WHERE key = 1""").fetchall()
            # надписи денег и жизней
            money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]

            text_money = font.render(f'money {str(money_number)}', 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
            pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((10, 550), text_money.get_size()))
            screen.blit(text_money, (10, 550))

            text_health = font.render(f'health {str(hero.health)}', 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
            pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((300, 550), text_health.get_size()))
            screen.blit(text_health, (300, 550))
            # выход из уровня
            if answer[3]:
                winwindow = window.Window(screen)
                winwindow.draw('win.jpg')
                Flag_win_window_on = True
                Flag_game_process_window_on = False

    # включение камеры при открытии уровня
    if Flag_camera_on:
        game_camera.update(hero, WIDTH, HEIGHT)

        for sprite in all_sprites:
            game_camera.apply(sprite)

    # отрисовка клеток и персонажа
    if Flag_game_process_window_on:
        tiles_group.draw(screen)
        health_group.draw(screen)
        money_group.draw(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        # надписи денег и жизней
        money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
        text_money = font.render(f'money {str(money_number)}', 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
        pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((10, 550), text_money.get_size()))
        screen.blit(text_money, (10, 550))

        text_health = font.render(f'health {str(hero.health)}', 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
        pygame.draw.rect(screen, BACKGROUND_TEXT_MONEY, ((300, 550), text_health.get_size()))
        screen.blit(text_health, (300, 550))

    clock.tick(FPS)

    pygame.display.flip()

conn.close()
