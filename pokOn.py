import pygame
import sys
import random
import pypokedex
import urllib3
from io import BytesIO
import tkinter as tk
import PIL.Image
import PIL.ImageTk

import pickle
import requests
from PIL.Image import Image
pygame.init()
screen = pygame.display.set_mode((850, 450))
clock = pygame.time.Clock()
done = False
bg_surface = pygame.image.load('pics/bg2.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
l = 0
battle_Sur = pygame.image.load('pics/battle.png').convert_alpha()
battle_Sur = pygame.transform.scale(battle_Sur, (850, 450))
ashdown1 = pygame.image.load('pics/ashdown1.png').convert_alpha()
ashdown1 = pygame.transform.scale(ashdown1, (50, 62))
ashdown2 = pygame.image.load('pics/ashdown2.png').convert_alpha()
ashdown2 = pygame.transform.scale(ashdown2, (50, 62))
ashdown3 = pygame.image.load('pics/ashdown3.png').convert_alpha()
ashdown3 = pygame.transform.scale(ashdown3, (50, 62))
In_Battle = False
ashup1 = pygame.image.load('pics/ashup1.png').convert_alpha()
ashup1 = pygame.transform.scale(ashup1, (50, 62))
ashup2 = pygame.image.load('pics/ashup2.png').convert_alpha()
ashup2 = pygame.transform.scale(ashup2, (50, 62))
ashup3 = pygame.image.load('pics/ashup3.png').convert_alpha()
ashup3 = pygame.transform.scale(ashup3, (50, 62))


ashleft1 = pygame.image.load('pics/ashleft1.png').convert_alpha()
ashleft1 = pygame.transform.scale(ashleft1, (50, 62))
ashleft2 = pygame.image.load('pics/ashleft2.png').convert_alpha()
ashleft2 = pygame.transform.scale(ashleft2, (50, 62))
ashleft3 = pygame.image.load('pics/ashleft3.png').convert_alpha()
ashleft3 = pygame.transform.scale(ashleft3, (50, 62))

ashright1 = pygame.image.load('pics/ashright1.png').convert_alpha()
ashright1 = pygame.transform.scale(ashright1, (50, 62))
ashright2 = pygame.image.load('pics/ashright2.png').convert_alpha()
ashright2 = pygame.transform.scale(ashright2, (50, 62))
ashright3 = pygame.image.load('pics/ashright3.png').convert_alpha()
ashright3 = pygame.transform.scale(ashright3, (50, 62))

imgs_run = [[ashleft1, ashleft2], [ashright1, ashright2],
            [ashdown1, ashdown2], [ashup1, ashup2]]
x = -3090
z = -13180
ez = []
ez1 = []

Press_1 = 0
Press_12 = 0

x_a = 850/2
z_a = 450/2
i = 0
j = 0
l1 = 0
a_s = 0
m_s = 10
nig = 1
strBefore = "D"
strBefore1 = "D"
strNow1 = "D"
strBefore2 = "D"
filename = 'mypickle.pk'
pokemon_pic = ashdown2
f = open(filename, 'rb')
arr_Ash_X_Z_range = pickle.load(f)
f = open('feilds.pk', 'rb')
feilds = pickle.load(f)
game_speed = 30
lastMove = "down"
game_font = pygame.font.Font('04B_19.ttf', 40)

sameBattle = False
levelPokemon = 0
while True:
    clock.tick(game_speed)
    if In_Battle and not sameBattle:
        levelPokemon = random.randint(0, 10)

        screen.blit(battle_Sur, (0, 0))
        screen.blit(pokemon_pic, (550, 100))
        score_surface = game_font.render(
            str(int(levelPokemon)), True, (255, 255, 255))

        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)
        sameBattle = True

    keyState = pygame.key.get_pressed()
    if not keyState[pygame.K_1]:
        Press_1 = 0
    if keyState[pygame.QUIT]:
        pygame.quit()
        sys.exit()
    elif keyState[pygame.K_ESCAPE] and In_Battle:
        In_Battle = False
        sameBattle = False
        screen.blit(bg_surface, (x, z))

        screen.blit(imgs_run[i][j], (x_a, z_a))
    elif keyState[pygame.K_F3]:
        if game_speed > 30:
            game_speed -= 10
    elif keyState[pygame.K_F4]:
        if game_speed < 200:
            game_speed += 10

    elif keyState[pygame.K_RIGHT]:
        InFeild = False
        for feild in range(0, len(feilds)):
            if feilds[feild][0] < (x_a + abs(x)) and feilds[feild][1] > (x_a + abs(x)) and feilds[feild][2] < (z_a + abs(z)) and feilds[feild][3] > (z_a + abs(z)):
                InFeild = True
                if random.randint(0, 60) == 42:
                    if (feild - 1)*5 + 5 <= 150:
                        pokemonNumber = random.randint(
                            (feild-1)*2 + 1, (feild-1)*2 + 2)
                        strPokNumber = "0"
                        if pokemonNumber < 10:
                            strPokNumber += f"0{(str(pokemonNumber))}"
                        elif pokemonNumber < 100:
                            strPokNumber += f"{(str(pokemonNumber))}"
                        else:
                            strPokNumber = str(pokemonNumber)

                        pokemon = pypokedex.get(
                            dex=pokemonNumber)

                        response = requests.get(
                            f"https://www.serebii.net/pokearth/sprites/frlg/{strPokNumber}.png")

                        file = open("pokemon.png", "wb")
                        file.write(response.content)
                        file.close()
                        fp = open("pokemon.png", "rb")
                        im = PIL.Image.open(fp)
                        width, height = im.size
                        hw = height/width
                        im.save('pokemon.png')

                        pokeSur = pygame.image.load(
                            'pokemon.png').convert_alpha()

                        pokeSur = pygame.transform.scale(
                            pokeSur, (150, int(150*hw)))
                        pokemon_pic = pokeSur
                        In_Battle = True
                break
        Hit = False
        x -= m_s
        x_a += a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = True
                break
        x += m_s
        x_a -= a_s
        if lastMove == "left" and Hit:
            x -= m_s
            x_a += a_s
        if (not Hit):
            lastMove = "right"

            i = 1
            x -= m_s
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))

            j += nig
            nig *= -1

    elif keyState[pygame.K_LEFT]:
        InFeild = False
        for feild in range(0, len(feilds)):
            if feilds[feild][0] < (x_a + abs(x)) and feilds[feild][1] > (x_a + abs(x)) and feilds[feild][2] < (z_a + abs(z)) and feilds[feild][3] > (z_a + abs(z)):
                InFeild = True
                if random.randint(0, 60) == 42:
                    if (feild - 1)*5 + 5 <= 150:
                        pokemonNumber = random.randint(
                            (feild-1)*2 + 1, (feild-1)*2 + 2)
                        strPokNumber = "0"
                        if pokemonNumber < 10:
                            strPokNumber += f"0{(str(pokemonNumber))}"
                        elif pokemonNumber < 100:
                            strPokNumber += f"{(str(pokemonNumber))}"
                        else:
                            strPokNumber = str(pokemonNumber)

                        pokemon = pypokedex.get(
                            dex=pokemonNumber)

                        response = requests.get(
                            f"https://www.serebii.net/pokearth/sprites/frlg/{strPokNumber}.png")

                        file = open("pokemon.png", "wb")
                        file.write(response.content)
                        file.close()
                        fp = open("pokemon.png", "rb")
                        im = PIL.Image.open(fp)
                        width, height = im.size
                        hw = height/width
                        im.save('pokemon.png')

                        pokeSur = pygame.image.load(
                            'pokemon.png').convert_alpha()

                        pokeSur = pygame.transform.scale(
                            pokeSur, (150, int(150*hw)))
                        pokemon_pic = pokeSur
                        In_Battle = True
                break
        Hit = False
        x += m_s
        x_a -= a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = True
                break
        x -= m_s
        x_a += a_s
        if lastMove == "right" and Hit:
            x += m_s
            x_a -= a_s
        if (not Hit):
            lastMove = "left"

            i = 0
            x += m_s
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))
            j += nig
            nig *= -1
    elif keyState[pygame.K_DOWN]:
        InFeild = False
        for feild in range(0, len(feilds)):
            if feilds[feild][0] < (x_a + abs(x)) and feilds[feild][1] > (x_a + abs(x)) and feilds[feild][2] < (z_a + abs(z)) and feilds[feild][3] > (z_a + abs(z)):
                InFeild = True
                if random.randint(0, 60) == 42:
                    if (feild - 1)*5 + 5 <= 150:
                        pokemonNumber = random.randint(
                            (feild-1)*2 + 1, (feild-1)*2 + 2)
                        strPokNumber = "0"
                        if pokemonNumber < 10:
                            strPokNumber += f"0{(str(pokemonNumber))}"
                        elif pokemonNumber < 100:
                            strPokNumber += f"{(str(pokemonNumber))}"
                        else:
                            strPokNumber = str(pokemonNumber)

                        pokemon = pypokedex.get(
                            dex=pokemonNumber)

                        response = requests.get(
                            f"https://www.serebii.net/pokearth/sprites/frlg/{strPokNumber}.png")

                        file = open("pokemon.png", "wb")
                        file.write(response.content)
                        file.close()
                        fp = open("pokemon.png", "rb")
                        im = PIL.Image.open(fp)
                        width, height = im.size
                        hw = height/width
                        im.save('pokemon.png')

                        pokeSur = pygame.image.load(
                            'pokemon.png').convert_alpha()

                        pokeSur = pygame.transform.scale(
                            pokeSur, (150, int(150*hw)))
                        pokemon_pic = pokeSur
                        In_Battle = True
                break
        Hit = False
        z -= m_s
        z_a += a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = True
                break
        z += m_s
        z_a -= a_s
        if lastMove == "up" and Hit:
            z -= m_s
            z_a += a_s

        if (not Hit):
            lastMove = "down"
            i = 2
            z -= m_s
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))
            j += nig
            nig *= -1
    elif keyState[pygame.K_UP]:
        InFeild = False
        for feild in range(0, len(feilds)):
            if feilds[feild][0] < (x_a + abs(x)) and feilds[feild][1] > (x_a + abs(x)) and feilds[feild][2] < (z_a + abs(z)) and feilds[feild][3] > (z_a + abs(z)):
                InFeild = True
                if random.randint(0, 60) == 42:
                    if (feild - 1)*5 + 5 <= 150:
                        pokemonNumber = random.randint(
                            (feild-1)*2 + 1, (feild-1)*2 + 2)
                        strPokNumber = "0"
                        if pokemonNumber < 10:
                            strPokNumber += f"0{(str(pokemonNumber))}"
                        elif pokemonNumber < 100:
                            strPokNumber += f"{(str(pokemonNumber))}"
                        else:
                            strPokNumber = string(pokemonNumber)

                        pokemon = pypokedex.get(
                            dex=pokemonNumber)

                        response = requests.get(
                            f"https://www.serebii.net/pokearth/sprites/frlg/{strPokNumber}.png")

                        file = open("pokemon.png", "wb")
                        file.write(response.content)
                        file.close()
                        fp = open("pokemon.png", "rb")
                        im = PIL.Image.open(fp)
                        width, height = im.size
                        hw = height/width
                        im.save('pokemon.png')

                        pokeSur = pygame.image.load(
                            'pokemon.png').convert_alpha()

                        pokeSur = pygame.transform.scale(
                            pokeSur, (150, int(150*hw)))
                        pokemon_pic = pokeSur
                        In_Battle = True
                break
        Hit = False
        z += 10
        z_a -= a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = True

                break
        z -= 10
        z_a += a_s
        if lastMove == "down" and Hit:
            z += 10
            z_a -= a_s
        if (not Hit):
            lastMove = "up"
            i = 3

            z += 10
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))

            j += nig
            nig *= -1
    elif keyState[pygame.K_SPACE]:
        strNow = f"ash_array: {(x_a + abs(x))} {(z_a + abs(z))}"
        if strNow != strBefore:
            strBefore = strNow

            ez.append(x_a + abs(x))
            ez.append(z_a + abs(z))
            l += 2
            if l == 4:
                print("push barier")
                nigf = []
                nigf.append(min(ez[0], ez[2]))
                nigf.append(max(ez[0], ez[2]))
                nigf.append(min(ez[1], ez[3]))
                nigf.append(max(ez[1], ez[3]))
                arr_Ash_X_Z_range.append(nigf)
                l = 0
                ez = []
    elif keyState[pygame.K_TAB]:
        strNow1 = f"ash_array: {(x_a + abs(x))} {(z_a + abs(z))}"
        if strNow1 != strBefore1:
            strBefore1 = strNow1

            ez1.append(x_a + abs(x))
            ez1.append(z_a + abs(z))
            l1 += 2
            if l1 == 4:
                print("push feild")
                nigf2 = []
                nigf2.append(min(ez1[0], ez1[2]))
                nigf2.append(max(ez1[0], ez1[2]))
                nigf2.append(min(ez1[1], ez1[3]))
                nigf2.append(max(ez1[1], ez1[3]))
                feilds.append(nigf2)
                l1 = 0
                ez1 = []
    elif keyState[pygame.K_9]:
        with open(filename, 'wb') as fi:
            # dump your data into the file
            pickle.dump(arr_Ash_X_Z_range, fi)
        with open('feilds.pk', 'wb') as fi:
            # dump your data into the file
            pickle.dump(feilds, fi)
    elif keyState[pygame.K_1]:
        Press_1 += 1
        if Press_1 < 2:
            print("pop barier")

            arr_Ash_X_Z_range.pop()
    elif keyState[pygame.K_2]:
        Press_12 += 1
        if Press_12 < 2:
            print("pop feild")

            feilds.pop()
    pygame.event.pump()
    pygame.display.flip()
