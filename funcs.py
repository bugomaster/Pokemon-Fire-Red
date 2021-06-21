from pokOn import *
colorNames = ["white", "green", "red", "blue", "black",
              "fuchsia", "gray", "lime", "maroon", "navyblue", "olive", "purple", "teal"]
colorsNumbers = [[255, 255, 255], [0, 255, 0], [255, 0, 0], [0, 0, 255], [
    0, 0, 0], [255, 0, 255], [128, 128, 128], [0, 128, 0], [128, 0, 0], [0, 0, 128], [128, 128, 0], [128, 0, 128], [0, 128, 128]]


def printFont(stringP, color):
    i = 0
    colorNumber = []
    for name in colorNames:
        if name == color:
            colorNumber = colorsNumbers[i]
            break
        i += 1

    score_surface = game_font.render(
        stringP, True, (colorsNumbers[0], colorsNumbers[1], colorsNumbers[2]))

    score_rect = score_surface.get_rect(center=(288, 100))
    screen.blit(score_surface, score_rect)
