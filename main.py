import pygame
import os, sqlite3
import window, load_image, defaut_stats, hero_presentation, generate_levels

pygame.init()
size = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(size)

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


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


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
                defaut_stats.defaultstats()
                Flag_dialog_window_on = False
                Flag_player_window_on = True
                curr.execute("""UPDATE player SET money = 50 WHERE key = 1""").fetchall()
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                screen.blit(text_money, (390, 20))
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
            if 450 < event.pos[1] < 520 and 20 < event.pos[0] < 250 and Flag_player_window_on:
                levelwindow = window.Window(screen)
                levelwindow.draw('levels window.jpg')
                Flag_player_window_on = False
                Flag_level_window_on = True
            if 540 < event.pos[1] < 580 and 40 < event.pos[0] < 230 and Flag_player_window_on:
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
                Flag_start_window_on = True
                Flag_player_window_on = False
            if 530 < event.pos[1] < 580 and 230 < event.pos[0] < 370 and Flag_level_window_on:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                money_number = (curr.execute("""SELECT money FROM player WHERE key = 1""").fetchall())[0][0]
                text_money = font.render(str(money_number), 1, (0, 0, 0), BACKGROUND_TEXT_MONEY)
                screen.blit(text_money, (390, 20))
                Flag_level_window_on = False
                Flag_player_window_on = True
            if 250 < event.pos[1] < 350 and 50 < event.pos[0] < 150 and Flag_level_window_on:
                generate_levels.generate_level(generate_levels.load_level("level 1.txt"),
                                               tiles_group, all_sprites, 1)
            if 250 < event.pos[1] < 350 and 250 < event.pos[0] < 350 and Flag_level_window_on:
                generate_levels.generate_level(generate_levels.load_level("level 2.txt"),
                                               tiles_group, all_sprites, 2)
            if 250 < event.pos[1] < 350 and 450 < event.pos[0] < 550 and Flag_level_window_on:
                generate_levels.generate_level(generate_levels.load_level("level 3.txt"),
                                               tiles_group, all_sprites, 3)

    tiles_group.draw(screen)

    pygame.display.flip()