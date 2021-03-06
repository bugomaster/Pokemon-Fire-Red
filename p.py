import pygame
import sys
import pickle
import pypokedex
import socket
import threading
import requests
import random
import PIL
import PIL.Image
from bs4 import BeautifulSoup
from datetime import datetime

import ast

pygame.init()
screen = pygame.display.set_mode((850, 450))
clock = pygame.time.Clock()
done = False
bg_surface = pygame.image.load('pics/bg2.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
l = 0
pokeBall = pygame.image.load(
    'pics/pokeball.png').convert_alpha()
pokeBall = pygame.transform.scale(
    pokeBall, (30, 30))
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
whenThrew = "0"
ashright1 = pygame.image.load('pics/ashright1.png').convert_alpha()
ashright1 = pygame.transform.scale(ashright1, (50, 62))
ashright2 = pygame.image.load('pics/ashright2.png').convert_alpha()
ashright2 = pygame.transform.scale(ashright2, (50, 62))
ashright3 = pygame.image.load('pics/ashright3.png').convert_alpha()
ashright3 = pygame.transform.scale(ashright3, (50, 62))
pokeBack = ashdown3
choose_wh = 5
battle_Choose = pygame.image.load(
    'pics/battle/fights.png').convert_alpha()
battle_Choose = pygame.transform.scale(
    battle_Choose, (600, int(600/choose_wh)))
stats_wh = 104/37

battle_stats = pygame.image.load(
    'pics/battle/stats.png').convert_alpha()
battle_stats = pygame.transform.scale(
    battle_stats, (250, int(250/stats_wh)))
whenFightChosen = 0

imgs_run = [[ashleft1, ashleft2], [ashright1, ashright2],
            [ashdown1, ashdown2], [ashup1, ashup2]]
x = -3330
z = -13302
ez = []
ez1 = []

Press_1 = 0
Press_12 = 0
noPokeMonPic = False
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
pokemon = pypokedex.get(
    dex=3)
didNothing = False
sameBattle = False
levelPokemon = 0
caught = False
# Define Colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
fights = []
x_arrow, y_arrow = 570, 350
chose = "Default"

attacks = ["Sky Attack", "wambo1", "wambo2", "wambo3"]
attacks_wild = []
attacks_wild_damage = [80, 30, 40, 40]
MyPokemonNumbers = [12, 48, 85, 132]
MyPokemonLvls = [4, 7, 11, 5]

mypokemon = pypokedex.get(
    dex=MyPokemonNumbers[0])

choseNumber = 0
tryingTooCatch = False
WildPoks = [[1, 4, 7], [10, 13, 16], [19, 21, 23],
            [25, 27, 29], [32, 35, 37], [39, 41, 43]]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

strCords = ""
beforeCords = "df"


def InFeild():
    global pokemon
    global pokemon_pic
    global pokeBack
    global In_Battle
    global attacks_wild
    global mypokemon
    for feild in range(0, len(feilds)):
        if feilds[feild][0] < (x_a + abs(x)) and feilds[feild][1] > (x_a + abs(x)) and feilds[feild][2] < (z_a + abs(z)) and feilds[feild][3] > (z_a + abs(z)):
            if random.randint(0, 60) == 42:

                pokemonNumber = random.randint(
                    feild//3 + 1, feild//3 + 6)

                pokemonColor = 'default'
                if random.randint(0, 200) == 69:
                    pokemonColor = 'shiny'
                pokemon = pypokedex.get(
                    dex=pokemonNumber)
                response = requests.get(
                    pokemon.sprites.front.get(pokemonColor))

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
                    pokeSur, (200, int(200*hw)))
                pokemon_pic = pokeSur
                mypokemon = pypokedex.get(
                    dex=MyPokemonNumbers[0])
                response = requests.get(
                    mypokemon.sprites.back.get('default'))

                file = open("pokemonBack.png", "wb")
                file.write(response.content)
                file.close()
                fp = open("pokemonBack.png", "rb")
                im = PIL.Image.open(fp)
                width, height = im.size

                hw = height/width
                im.save('pokemonBack.png')

                pokeSurBack = pygame.image.load(
                    'pokemonBack.png').convert_alpha()

                pokeSurBack = pygame.transform.scale(
                    pokeSurBack, (200, int(200*hw)))
                pokeBack = pokeSurBack

                url = 'https://pokemondb.net/move/all'

                response = requests.get(url)

                soup = BeautifulSoup(response.text, "html.parser")
                counter = 0
                line_count = 1
                typee = "jj"
                for one_a_tag in soup.findAll('a'):
                    if line_count >= 36:
                        if one_a_tag['href'][1:5] == "type":
                            typee = (one_a_tag['href'][6:])
                        elif one_a_tag['href'][1:5] == "move" and typee == mypokemon.types[0]:
                            attacks_wild.append(one_a_tag['href'][6:])
                            counter += 1
                        if counter == 4:
                            break
                    line_count += 1
                In_Battle = True
            break


def printFont(stringP, color, size, x, y):

    score_surface = pygame.font.Font('font.ttf', size).render(
        stringP, True, color)

    score_rect = score_surface.get_rect(center=(x, y))
    screen.blit(score_surface, score_rect)


def printThick(stringP, color, size, x, y):
    printFont(stringP, color, size, x, y)
    printFont(stringP, color, size, x+1, y)
    printFont(stringP, color, size, x+2, y)


def drawStats(x, y, lengthRect, pokemonName, Poklvl):
    screen.blit(battle_stats, (x, y))
    printThick(str(int(Poklvl)), BLACK, 30, x+225, y+20)
    printFont(pokemonName, BLACK, 40, x+100, y+15)
    pygame.draw.rect(screen, LIME, (x+114, y+40, lengthRect, 9))


def printText(text, color, size, x, y):
    text_obj = pygame.font.Font('font.ttf', size).render(text, True, color)
    screen.blit(text_obj, (x, y))


def battle():
    screen.blit(battle_Sur, (0, 0))
    if not tryingTooCatch:

        if not noPokeMonPic:
            screen.blit(pokemon_pic, (550, 100))
        else:
            printText(f"you caught {pokemon.name}", BLACK, 45, 550, 100)
        screen.blit(pokeBack, (50, 270))

        screen.blit(battle_Choose, (250, 330))
        drawStats(0, 0, 118, pokemon.name, levelPokemon)
        drawStats(600, 250, 118, mypokemon.name, MyPokemonLvls[0])
        printText(mypokemon.name, WHITE, 45, 280, 390)

        if chose == "Fight":

            printText(">", BLACK, 37, x_arrow, y_arrow)
            printText(attacks_wild[0], BLACK, 28, 580, 350)
            printText(attacks_wild[1], BLACK, 28, 580, 400)
            printText(attacks_wild[2], BLACK, 28, 700, 350)
            printText(attacks_wild[3], BLACK, 28, 700, 400)

        elif chose == "Pokemon":
            print("show pokemons")
        else:
            printText(">", BLACK, 37, x_arrow, y_arrow)

            printText("Fight", BLACK, 37, 580, 350)
            printText("Pokemon", BLACK, 37, 580, 400)
    else:
        screen.blit(battle_Sur, (0, 0))
        screen.blit(pokeBall, (550, 260))


endidx = 0

rc = ""
gotMsg = False

usernames = []

idxPl = 0
xlist = []
zlist = []
ilist = []
jlist = []

newborn = False


def handle_messages():
    global xlist
    global zlist
    global ilist
    global jlist
    global rc
    global z
    global newborn
    global gotMsg
    global usernames
    while 1:

        gotMsg = False
        x_rc = ""
        z_rc = ""
        i_rc = ""
        j_rc = ""
        try:
            rc = s.recv(1024).decode()
            for startidx in range(0, len(rc)):
                if rc[startidx] == '@':
                    for endidx in range(startidx, len(rc)):
                        if rc[endidx] == 'E':
                            usernames = ast.literal_eval(rc[startidx+1:endidx])
                            usernames = [n.strip() for n in usernames]

                            break
                    else:
                        continue
                    xlist = []
                    zlist = []
                    ilist = []
                    jlist = []
                    z -= len(usernames)*62
                    for d in usernames:
                        xlist.append(0)
                        zlist.append(0)
                        ilist.append(0)
                        jlist.append(0)

                    break
            else:
                for i in range(0, len(rc)):
                    if rc[i] == 'S':
                        eidx = i
                        i3 = 0
                        for i2 in range(i, len(rc)):
                            if rc[i2] == 'E':
                                i3 = i2 + 1
                                break
                            eidx += 1
                        if rc[i3] == 'J':
                            print(f"{rc[i+1:eidx]} joined")
                            newborn = True
                            usernames.append(rc[i+1:eidx])
                            xlist = []
                            zlist = []
                            ilist = []
                            jlist = []

                            for d in usernames:
                                xlist.append(0)
                                zlist.append(0)
                                ilist.append(0)
                                jlist.append(0)

                        elif rc[i3] == 'L':
                            print(f"{rc[i+1:eidx]} left")
                            usernames.remove(rc[i+1:eidx])
                        break
                else:

                    for i in range(0, len(rc)):
                        idxPl = 0
                        for nameU in usernames:
                            if nameU == rc[i:i+len(nameU)] and rc[i+len(nameU):i+len(nameU)+1] == 'x':
                                print(f"{nameU} is moving")
                                break
                            idxPl += 1
                        else:
                            continue
                        break
                    for i in range(0, len(rc)):
                        if rc[i] == 'x':
                            eidx = i
                            for i2 in range(i, len(rc)):
                                if rc[i2] == 'z':
                                    break
                                eidx += 1

                            x_rc = rc[i+1:eidx]
                            break
                    for i in range(0, len(rc)):
                        if rc[i] == 'z':
                            eidx = i
                            for i2 in range(i, len(rc)):
                                if rc[i2] == 'i':
                                    break
                                eidx += 1

                            z_rc = rc[i+1:eidx]

                            break
                    for i in range(0, len(rc)):
                        if rc[i] == 'i':
                            eidx = i
                            for i2 in range(i, len(rc)):
                                if rc[i2] == 'j':
                                    break
                                eidx += 1

                            i_rc = rc[i+1:eidx]
                            break
                    for i in range(0, len(rc)):
                        if rc[i] == 'j':
                            eidx = i
                            for i2 in range(i, len(rc)):
                                if rc[i2] == 'x':
                                    break
                                eidx += 1

                            j_rc = rc[i+1:eidx]
                            break

                    try:
                        xlist[idxPl] = int(x_rc)
                        zlist[idxPl] = int(z_rc)
                        ilist[idxPl] = int(i_rc)
                        jlist[idxPl] = int(j_rc)

                    except:
                        pass

        except:
            pass


def input_handler():
    global newborn
    already_sent_X = 0
    already_sent_Z = 0
    already_sent_I = 0
    already_sent_J = 0
    while 1:
        if already_sent_I != i or already_sent_J != j or already_sent_X != x or already_sent_Z != z or newborn:
            already_sent_X = x
            already_sent_Z = z
            already_sent_I = i
            already_sent_J = j
            newborn = False
            s.send((f"{username}x{x}z{z}i{i}j{j}").encode())


while True:
    try:

        s.connect((socket.gethostbyname(socket.gethostname()), 12345))
        break
    except:
        pass
username = input('Enter username ')
s.send(username.encode())

message_handler = threading.Thread(target=handle_messages, args=())
message_handler.start()
hit_player = False

input_handler = threading.Thread(target=input_handler, args=())
input_handler.start()
again = False
while True:

    clock.tick(game_speed)
    keyState = pygame.key.get_pressed()
    if (keyState[pygame.K_x] and hit_player) or again:
        battle()
        again = True
    if In_Battle and not sameBattle:
        levelPokemon = random.randint(1, 10)
        caught = False
        battle()
        sameBattle = True
    elif In_Battle and sameBattle:

        if whenThrew != "0" and (int(datetime.now().strftime("%H:%M:%S")[6:]) - int(whenThrew[6:]) > 3):
            if random.randint(0, 3) == 2:
                caught = True
                noPokeMonPic = True
            else:
                whenThrew = "0"  # new throw
            battle()
            tryingTooCatch = False
        if keyState[pygame.K_RIGHT] and x_arrow == 570 and chose == "Fight":
            x_arrow += 120
            choseNumber -= 2

        elif keyState[pygame.K_LEFT] and x_arrow == 690 and chose == "Fight":
            x_arrow -= 120
            choseNumber += 2

        elif keyState[pygame.K_z] and chose == "Fight":
            chose = "Default"
            x_arrow, y_arrow = 570, 350

        elif keyState[pygame.K_z] and chose == "Pokemon":
            chose = "Default"
            x_arrow, y_arrow = 570, 350

        elif keyState[pygame.K_DOWN] and y_arrow == 350:
            y_arrow += 50
            choseNumber += 1

        elif keyState[pygame.K_x] and y_arrow == 350 and chose == "Default":
            chose = "Fight"

            whenFightChosen = datetime.now().strftime("%H:%M:%S")

        elif keyState[pygame.K_x] and chose == "Fight" and (int(datetime.now().strftime("%H:%M:%S")[6:]) - int(whenFightChosen[6:]) > 1):
            print(f"do {attacks_wild[choseNumber]}")

        elif keyState[pygame.K_x] and y_arrow == 400 and chose == "Default":
            chose = "Pokemon"

        elif keyState[pygame.K_UP] and y_arrow == 400:
            y_arrow -= 50
            choseNumber -= 1
        elif whenThrew == "0" and not caught and keyState[pygame.K_SPACE]:
            whenThrew = datetime.now().strftime("%H:%M:%S")
            tryingTooCatch = True
        battle()
        if keyState[pygame.K_ESCAPE] and In_Battle:
            In_Battle = False
            sameBattle = False
            screen.blit(bg_surface, (x, z))
            chose = "Default"
            whenThrew = "0"
            attacks_wild = []
            x_arrow, y_arrow = 570, 350
            caught = False
            screen.blit(imgs_run[i][j], (x_a, z_a))
            noPokeMonPic = False
    else:
        screen.blit(bg_surface, (x, z))
        screen.blit(
            imgs_run[i][j], (x_a, z_a))

        try:
            for player in range(0, len(usernames)):
                x_other_player = x_a+(x - xlist[player])
                z_other_player = z_a+(z - zlist[player])
                screen.blit(
                    imgs_run[ilist[player]][jlist[player]], (x_other_player, z_other_player))
            for player in range(0, len(usernames)):
                x_other_player = x_a+(x - xlist[player])
                z_other_player = z_a+(z - zlist[player])

                printFont(usernames[player], FUCHSIA, 30,
                          x_other_player + 25, z_other_player - 10)

        except:
            pass
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
            InFeild()
            Hit = False
            x -= m_s
            x_a += a_s
            hitplayer = True
            for barier in range(0, len(arr_Ash_X_Z_range)):
                if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                    Hit = True
                    break
            for player_barier in range(0, len(xlist)):
                if abs(xlist[player_barier]) + 22 > abs(x) and abs(xlist[player_barier]) - 22 < abs(x) and abs(zlist[player_barier]) - 31 < abs(z) and abs(zlist[player_barier]) + 31 > abs(z):
                    Hit = True
                    hit_player = True

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

                j += nig
                nig *= -1

        elif keyState[pygame.K_LEFT]:
            InFeild()
            Hit = False
            x += m_s
            x_a -= a_s
            hitplayer = True
            for barier in range(0, len(arr_Ash_X_Z_range)):
                if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                    Hit = True
                    break
            for player_barier in range(0, len(xlist)):
                if abs(xlist[player_barier]) + 22 > abs(x) and abs(xlist[player_barier]) - 22 < abs(x) and abs(zlist[player_barier]) - 31 < abs(z) and abs(zlist[player_barier]) + 31 > abs(z):
                    Hit = True
                    hit_player = True

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
                j += nig
                nig *= -1
        elif keyState[pygame.K_DOWN]:
            InFeild()
            Hit = False
            z -= m_s
            z_a += a_s
            hitplayer = True
            for barier in range(0, len(arr_Ash_X_Z_range)):
                if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                    Hit = True
                    break
            for player_barier in range(0, len(xlist)):
                if abs(xlist[player_barier]) + 22 > abs(x) and abs(xlist[player_barier]) - 22 < abs(x) and abs(zlist[player_barier]) - 31 < abs(z) and abs(zlist[player_barier]) + 31 > abs(z):
                    Hit = True
                    hit_player = True

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

                j += nig
                nig *= -1
        elif keyState[pygame.K_UP]:
            InFeild()
            Hit = False
            z += 10
            z_a -= a_s
            hitplayer = True
            for barier in range(0, len(arr_Ash_X_Z_range)):
                if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                    Hit = True
                    break
            for player_barier in range(0, len(xlist)):
                if abs(xlist[player_barier]) + 22 > abs(x) and abs(xlist[player_barier]) - 22 < abs(x) and abs(zlist[player_barier]) - 31 < abs(z) and abs(zlist[player_barier]) + 31 > abs(z):
                    Hit = True
                    hit_player = True

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
                pickle.dump(arr_Ash_X_Z_range, fi)
            with open('feilds.pk', 'wb') as fi:
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
