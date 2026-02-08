from src.constants import WIDTH, CHAR_WIDTH, IMAGE_WIDTH

def char_width(char):
    # Return width of given character. For characters other than the letters A to Z (i.e. space, and the digits 0 to 9),
    # the width of the letter A is returned. ord gives the ASCII/Unicode code for the given character.
    index = max(0, ord(char) - 65)
    return CHAR_WIDTH[index]

def draw_text(screen, text, y, x=None):
    if x == None:
        # If no X pos specified, draw text in centre of the screen - must first work out total width of text
        x = (WIDTH - sum([char_width(c) for c in text])) // 2

    for char in text:
        screen.blit("font0"+str(ord(char)), (x, y))
        x += char_width(char)

def draw_status(screen, game):
    # Display score, right-justified at edge of screen
    number_width = CHAR_WIDTH[0]
    s = str(game.player.score)
    draw_text(screen, s, 451, WIDTH - 2 - (number_width * len(s)))

    # Display level number
    draw_text(screen, "LEVEL " + str(game.level + 1), 451)

    # Display lives and health
    # We only display a maximum of two lives - if there are more than two, a plus symbol is displayed
    lives_health = ["life"] * min(2, game.player.lives)
    if game.player.lives > 2:
        lives_health.append("plus")
    if game.player.lives >= 0:
        lives_health += ["health"] * game.player.health

    x = 0
    for image in lives_health:
        screen.blit(image, (x, 450))
        x += IMAGE_WIDTH[image]
