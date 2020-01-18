import pygame
import os, sqlite3
import window, load_image, defaut_stats

pygame.init()
size = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(size)

startwindow = window.Window(screen)
startwindow.draw('start window.jpg')

Flag_rules_window_on = False
Flag_player_window_on = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
            if 200 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                defaut_stats.defaultstats()
                Flag_player_window_on = True
            if 200 <= event.pos[0] <= 400 and 300 <= event.pos[1] <= 350:
                playerwindow = window.Window(screen)
                playerwindow.draw('player window.jpg')
                Flag_player_window_on = True
            if 200 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250:
                ruleswindow = window.Window(screen)
                ruleswindow.draw('rules window.jpg')
                Flag_rules_window_on = True
            if 200 <= event.pos[0] <= 400 and 500 <= event.pos[1] <= 550:
                running = False
            if 520 <= event.pos[0] <= 600 and 0 <= event.pos[1] <= 30 and Flag_rules_window_on:
                Flag_rules_window_on = False
                startwindow = window.Window(screen)
                startwindow.draw('start window.jpg')
    pygame.display.flip()
