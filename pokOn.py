import pygame
import sys
import random
import pickle
pygame.init()
screen = pygame.display.set_mode((1700, 900))
clock = pygame.time.Clock()
done = False
bg_surface = pygame.image.load('pics/bg2.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
l = 0

ashdown1 = pygame.image.load('pics/ashdown1.png').convert_alpha()
ashdown1 = pygame.transform.scale(ashdown1, (50, 62))
ashdown2 = pygame.image.load('pics/ashdown2.png').convert_alpha()
ashdown2 = pygame.transform.scale(ashdown2, (50, 62))
ashdown3 = pygame.image.load('pics/ashdown3.png').convert_alpha()
ashdown3 = pygame.transform.scale(ashdown3, (50, 62))

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
x = -3150
z = -9450
ez = []

x_a = 740
z_a = 400
i = 0
j = 0
a_s = 0
m_s = 10
nig = 1
strBefore = "D"
strBefore2 = "D"
filename = 'mypickle.pk'
arr_Ash_X_Z_range = [[0, 0, 0, 0], [
    0, 0, 0, 0], [0, 0, 0, 0]]

game_speed = 30
lastMove = "down"
while True:
    clock.tick(game_speed)

    keyState = pygame.key.get_pressed()
    if keyState[pygame.QUIT]:
        pygame.quit()
        sys.exit()
    elif keyState[pygame.K_F3]:
        if game_speed > 30:
            game_speed -= 10
    elif keyState[pygame.K_F4]:
        if game_speed < 200:
            game_speed += 10

    elif keyState[pygame.K_RIGHT]:
        Hit = True
        x -= m_s
        x_a += a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = False
                break
        x += m_s
        x_a -= a_s
        if lastMove == "left" and not Hit:
            x -= m_s
            x_a += a_s
        if (Hit):
            lastMove = "right"

            i = 1
            x -= m_s
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))

            j += nig
            nig *= -1

    elif keyState[pygame.K_LEFT]:
        Hit = True
        x += m_s
        x_a -= a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = False
                break
        x -= m_s
        x_a += a_s
        if lastMove == "right" and not Hit:
            x += m_s
            x_a -= a_s
        if (Hit):
            lastMove = "left"

            i = 0
            x += m_s
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))
            j += nig
            nig *= -1
    elif keyState[pygame.K_DOWN]:
        Hit = True
        z -= m_s
        z_a += a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = False
                break
        z += m_s
        z_a -= a_s
        if lastMove == "up" and not Hit:
            z -= m_s
            z_a += a_s

        if (Hit):
            lastMove = "down"
            i = 2
            z -= m_s
            screen.blit(bg_surface, (x, z))

            screen.blit(imgs_run[i][j], (x_a, z_a))
            j += nig
            nig *= -1
    elif keyState[pygame.K_UP]:
        Hit = True
        z += 10
        z_a -= a_s
        for barier in range(0, len(arr_Ash_X_Z_range)):
            if arr_Ash_X_Z_range[barier][0] < (x_a + abs(x)) and arr_Ash_X_Z_range[barier][1] > (x_a + abs(x)) and arr_Ash_X_Z_range[barier][2] < (z_a + abs(z)) and arr_Ash_X_Z_range[barier][3] > (z_a + abs(z)):
                Hit = False

                break
        z -= 10
        z_a += a_s
        if lastMove == "down" and not Hit:
            z += 10
            z_a -= a_s
        if (Hit):
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
                print(
                    f"[{min(ez[0], ez[2])}, {max(ez[0], ez[2])},{min(ez[1], ez[3])}, {max(ez[1], ez[3])}]")
                nigf = []
                nigf.append(min(ez[0], ez[2]))
                nigf.append(max(ez[0], ez[2]))
                nigf.append(min(ez[1], ez[3]))
                nigf.append(max(ez[1], ez[3]))
                arr_Ash_X_Z_range.append(nigf)
                l = 0
                ez = []
    elif keyState[pygame.K_9]:
        with open(filename, 'wb') as fi:
            # dump your data into the file
            pickle.dump(arr_Ash_X_Z_range, fi)

        # strNow = f"ash_array: {x_a},{z_a} | {x}, {z} "
        # if strNow != strBefore2:
        #     strBefore2 = strNow
        #     print(f"ash_array: {x_a},{z_a} | {x}, {z} ")

    pygame.event.pump()
    pygame.display.flip()
