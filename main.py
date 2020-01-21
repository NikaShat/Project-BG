import pygame
import os, sqlite3
import window, load_image, defaut_stats, hero_presentation, generate_levels, camera, classes

pygame.init()
size = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

startwindow = window.Window(screen)
startwindow.draw('start window.jpg')

Flag_start_window_on = True
Flag_rules_window_on = False
Flag_player_window_on = False
Flag_dialog_window_on = False
Flag_level_window_on = False

Flag_select_wizard = False
Flag_select_archer = False
Flag_select_barbarian = False
Flag_select_crusader = False
Flag_select_necromancer = False

pygame.mixer.init()
pygame.mixer.music.load('data/music/start_window_theme.mp3')
pygame.mixer.music.play(-1)

FPS = 50
STEP = 10

different_images = 0
UPDATE_IMAGE = 30
pygame.time.set_timer(UPDATE_IMAGE, 3000)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group_not_collide = pygame.sprite.Group()
tiles_group_collide = pygame.sprite.Group()

conn = sqlite3.connect("data/database.db")
curr = conn.cursor()
check = curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall()

if check[0][0] == -1:
    save_file_exist = False
else:
    save_file_exist = True

font = pygame.font.Font('data/game_font.ttf', 36)
BACKGROUND_TEXT_MONEY = (214, 221, 231)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
            if 200 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250 and Flag_start_window_on:
                if save_file_exist:
                    dialogwindow = window.Window(screen)
                    dialogwindow.draw('dialog window.jpg')
                    Flag_start_window_on = False
                    Flag_dialog_window_on = True
                else:
                    playerwindow = window.Window(screen)
                    playerwindow.draw('player window.jpg')
                    defaut_stats.defaultstats()
                    Flag_player_window_on = True
                    save_file_exist = True
                    curr.execute("""UPDATE player
                                    SET money = 50
                                    WHERE key = 1""").fetchall()
                    money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                    text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                    screen.blit(text_money, (390, 20))
                    Flag_start_window_on = False
            if 180 <= event.pos[0] <= 280 and 350 <= event.pos[1] <= 380 and Flag_dialog_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                Flag_dialog_window_on = False
                Flag_player_window_on = True
                curr.execute("""UPDATE player SET money = 50 WHERE key = 1""").fetchall()
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                screen.blit(text_money, (390, 20))
                defaut_stats.defaultstats()
            if 320 <= event.pos[0] <= 420 and 350 <= event.pos[1] <= 380 and Flag_dialog_window_on:
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
                Flag_start_window_on = True
                Flag_dialog_window_on = False
            if 200 <= event.pos[0] <= 400 and 300 <= event.pos[1] <= 350 and save_file_exist and Flag_start_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                Flag_start_window_on = False
                Flag_player_window_on = True
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                screen.blit(text_money, (390, 20))
            if 200 <= event.pos[0] <= 400 and 400 <= event.pos[1] <= 450 and Flag_start_window_on:
                ruleswindow = window.Window(screen)
                ruleswindow.draw('rules window.jpg')
                Flag_start_window_on = False
                Flag_rules_window_on = True
            if 200 <= event.pos[0] <= 400 and 500 <= event.pos[1] <= 550:
                running = False
            if 520 <= event.pos[0] <= 600 and 0 <= event.pos[1] <= 30 and Flag_rules_window_on:
                Flag_rules_window_on = False
                Flag_start_window_on = True
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
            if 520 <= event.pos[0] <= 600 and 0 <= event.pos[1] <= 40 and Flag_player_window_on:
                curr.execute(f"""UPDATE player
                                SET money = {money_number}
                                WHERE key = 1""").fetchall()
            if 100 < event.pos[1] < 160 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('wizard', screen)
                Flag_select_wizard = True
                Flag_select_archer = False
                Flag_select_barbarian = False
                Flag_select_crusader = False
                Flag_select_necromancer = False
            if 160 < event.pos[1] < 220 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('archer', screen)
                Flag_select_wizard = False
                Flag_select_archer = True
                Flag_select_barbarian = False
                Flag_select_crusader = False
                Flag_select_necromancer = False
            if 220 < event.pos[1] < 280 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('barbarian', screen)
                Flag_select_wizard = False
                Flag_select_archer = False
                Flag_select_barbarian = True
                Flag_select_crusader = False
                Flag_select_necromancer = False
            if 280 < event.pos[1] < 340 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('crusader', screen)
                Flag_select_wizard = False
                Flag_select_archer = False
                Flag_select_barbarian = False
                Flag_select_crusader = True
                Flag_select_necromancer = False
            if 340 < event.pos[1] < 400 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                hero_presentation.presentation('necromancer', screen)
                Flag_select_wizard = False
                Flag_select_archer = False
                Flag_select_barbarian = False
                Flag_select_crusader = False
                Flag_select_necromancer = True
            if (450 < event.pos[1] < 520 and 20 < event.pos[0] < 250 and Flag_player_window_on and
               (Flag_select_archer or Flag_select_wizard or Flag_select_necromancer or Flag_select_barbarian or
               Flag_select_crusader)):
                levelwindow = window.Window(screen)
                levelwindow.draw('levels window.jpg')
                Flag_player_window_on = False
                Flag_level_window_on = True
            if 540 < event.pos[1] < 580 and 40 < event.pos[0] < 230 and Flag_player_window_on:
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
                Flag_start_window_on = True
                Flag_player_window_on = False
            if 370 <= event.pos[0] <= 500 and 540 <= event.pos[1] <= 570 and Flag_player_window_on:
                print('ok')
                if Flag_select_necromancer and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'necromancer', 0, 0)
                    upgrade_hero_stats.upgrade(money_number, screen)
                elif Flag_select_archer and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'archer', 0, 0)
                    upgrade_hero_stats.upgrade(money_number, screen)
                elif Flag_select_wizard and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'wizard', 0, 0)
                    upgrade_hero_stats.upgrade(money_number, screen)
                elif Flag_select_barbarian and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'barbarian', 0, 0)
                    upgrade_hero_stats.upgrade(money_number, screen)
                elif Flag_select_crusader and money_number - 100 >= 0:
                    upgrade_hero_stats = classes.Hero(player_group, all_sprites, 'crusader', 0, 0)
                    upgrade_hero_stats.upgrade(money_number, screen)
            if 530 < event.pos[1] < 580 and 230 < event.pos[0] < 370 and Flag_level_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                screen.blit(text_money, (390, 20))
                Flag_level_window_on = False
                Flag_player_window_on = True
            if 250 < event.pos[1] < 350 and 50 < event.pos[0] < 150 and Flag_level_window_on:
                if Flag_select_crusader:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'crusader', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_barbarian:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'barbarian', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_wizard:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'wizard', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_archer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'archer', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_necromancer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                                                            player_group, tiles_group, all_sprites, 1,
                                                                            'necromancer', tiles_group_collide,
                                                                            tiles_group_not_collide)
                pygame.mixer.music.stop()
                game_camera = camera.Camera((level_x, level_y))
            if 250 < event.pos[1] < 350 and 250 < event.pos[0] < 350 and Flag_level_window_on:
                if Flag_select_crusader:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'crusader', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_barbarian:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'barbarian', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_wizard:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'wizard', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_archer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'archer', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_necromancer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                                                            player_group, tiles_group, all_sprites, 2,
                                                                            'necromancer', tiles_group_collide,
                                                                            tiles_group_not_collide)
                game_camera = camera.Camera((level_x, level_y))
            if 250 < event.pos[1] < 350 and 450 < event.pos[0] < 550 and Flag_level_window_on:
                if Flag_select_crusader:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'crusader', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_barbarian:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'barbarian', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_wizard:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'wizard', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_archer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'archer', tiles_group_collide,
                                                                            tiles_group_not_collide)
                elif Flag_select_necromancer:
                    hero, level_x, level_y = generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                                                            player_group, tiles_group, all_sprites, 3,
                                                                            'necromancer', tiles_group_collide,
                                                                            tiles_group_not_collide)
                game_camera = camera.Camera((level_x, level_y))
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                hero.rect.x -= STEP
                if not hero.update(tiles_group_not_collide, tiles_group_collide):
                    hero.rect.x += STEP
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                hero.rect.x += STEP
                if not hero.update(tiles_group_not_collide, tiles_group_collide):
                    hero.rect.x -= STEP
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                hero.rect.y -= STEP
                if not hero.update(tiles_group_not_collide, tiles_group_collide):
                    hero.rect.y += STEP
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                hero.rect.y += STEP
                if not hero.update(tiles_group_not_collide, tiles_group_collide):
                    hero.rect.y -= STEP

    if 'game_camera' in globals():
        game_camera.update(hero, WIDTH, HEIGHT)

    for sprite in all_sprites:
        game_camera.apply(sprite)

    tiles_group.draw(screen)
    player_group.draw(screen)

    clock.tick(FPS)

    pygame.display.flip()
