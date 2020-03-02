import pygame, load_image, sqlite3


def presentation(classes, screen, cur):
    # подгрузка картнки
    if classes == 'wizard':
        image = load_image.loadimage('wizard present.jpg')
    elif classes == 'archer':
        image = load_image.loadimage('archer present.jpg')
    elif classes == 'barbarian':
        image = load_image.loadimage('barbarian present.jpg')
    elif classes == 'crusader':
        image = load_image.loadimage('crusader present.jpg')
    else:
        image = load_image.loadimage('necromancer present.jpg')
    screen.blit(image, (290, 120))
    BACKGROUND_COLOR = (254, 240, 205)
    # текст статов персонажа
    font = pygame.font.Font('data/game_font.ttf', 20)
    # текст для уровня персонажа
    font_for_level = pygame.font.Font('data/game_font.ttf', 36)

    # значения статов из БД
    num_defence = (cur.execute(f"""SELECT defence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_health = (cur.execute(f"""SELECT health FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_intelligence = (cur.execute(f"""SELECT intelligence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_strength = (cur.execute(f"""SELECT strength FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_speed = (cur.execute(f"""SELECT speed FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
    num_level = (cur.execute(f"""SELECT level FROM classes WHERE name = '{classes}'""").fetchall())[0][0]

    # создание текста со значениями статов
    text_defence = font.render(str(num_defence), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_health = font.render(str(num_health), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_intelligence = font.render(str(num_intelligence), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_strength = font.render(str(num_strength), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_speed = font.render(str(num_speed), 1, (0, 0, 0), BACKGROUND_COLOR)
    text_level = font_for_level.render(str(num_level), 1, (0, 0, 0), (222, 227, 235))

    # отрисока текста
    pygame.draw.rect(screen, BACKGROUND_COLOR, ((380, 440), text_defence.get_size()))
    screen.blit(text_defence, (380, 440))
    pygame.draw.rect(screen, BACKGROUND_COLOR, ((530, 440), text_health.get_size()))
    screen.blit(text_health, (530, 440))
    pygame.draw.rect(screen, BACKGROUND_COLOR, ((460, 470), text_intelligence.get_size()))
    screen.blit(text_intelligence, (460, 470))
    pygame.draw.rect(screen, BACKGROUND_COLOR, ((390, 500), text_strength.get_size()))
    screen.blit(text_strength, (390, 500))
    pygame.draw.rect(screen, BACKGROUND_COLOR, ((510, 500), text_speed.get_size()))
    screen.blit(text_speed, (510, 500))
    pygame.draw.rect(screen, BACKGROUND_COLOR, ((130, 20), text_level.get_size()))
    screen.blit(text_level, (130, 20))
