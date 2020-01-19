import pygame, load_image, sqlite3

con = sqlite3.connect("data/database.db")
cur = con.cursor()


def presentation(classes, screen):
#    if classes == 'wizard':
#        image = load_image.loadimage('wizard.png')
 #   elif classes == 'archer':
 #       image = load_image.loadimage('archer.png')
 #   elif classes == 'barbarian':
  #      image = load_image.loadimage('barbarian.png')
  #  elif classes == 'crusader':
       # image = load_image.loadimage('crusader.png')
   # else:
       # image = load_image.loadimage('necromancer.png')
    #screen.blit(image, (290, 120))
    BACKGROUND_COLOR = (254, 240, 205)
    font = pygame.font.Font('data/game_font.ttf', 20)
    font_for_level = pygame.font.Font('data/game_font.ttf', 36)
    num_defence = (cur.execute(f"""SELECT defence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_health = (cur.execute(f"""SELECT health FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_intelligence = (cur.execute(f"""SELECT intelligence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_strength = (cur.execute(f"""SELECT strength FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_speed = (cur.execute(f"""SELECT speed FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_level = (cur.execute(f"""SELECT level FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    text_defence = font.render(str(num_defence), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_health = font.render(str(num_health), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_intelligence = font.render(str(num_intelligence), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_strength = font.render(str(num_strength), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_speed = font.render(str(num_speed), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_level = font_for_level.render(str(num_level), 1, (0, 0, 0), (222, 227, 235))
    screen.blit(text_defence, (380, 440))
    screen.blit(text_health, (530, 440))
    screen.blit(text_intelligence, (460, 470))
    screen.blit(text_strength, (390, 500))
    screen.blit(text_speed, (510, 500))
    screen.blit(text_level, (130, 20))
