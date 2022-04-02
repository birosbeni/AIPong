
#hibák:-
#megoldani:-
#AI:
#hiányzó AI:
#abbahagyí:

import pygame
import random

pygame.init()

screen_width = 300
screen_heigth = 300

screen = pygame.display.set_mode((screen_width, screen_heigth))

font = pygame.font.SysFont(None, 40)

again_rect = pygame.Rect(screen_width//2-100, screen_heigth//2, 200, 50)

#színek
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bg = (100,150,50)
black = (0,0,0)

#változók
player = 1
winner = 0
line_width = 5
clicked = False
game_over = False

#alap
markers = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
#cellák pontozása
markers_point = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def draw_window():
    #háttér kitöltése
    screen.fill(bg)

    #vonalak megrajzolása
    pygame.draw.line(screen, black, (screen_width/3, 0), (screen_width/3, screen_heigth), 5)
    pygame.draw.line(screen, black, (screen_width/3*2, 0), (screen_width/3*2, screen_heigth), 5)
    pygame.draw.line(screen, black, (0, screen_heigth/3), (screen_width, screen_heigth/3), 5)
    pygame.draw.line(screen, black, (0, screen_heigth/3*2), (screen_heigth, screen_heigth/3*2), 5)


def draw_markers():
    y_pos = 0
    for x in markers:
        x_pos = 0
        for y in x:
            #x megrajzolása két vonallal
            if y == 1:
                pygame.draw.line(screen, black, (x_pos*100+20, y_pos*100+20), (x_pos*100+80, y_pos*100+80), line_width)
                pygame.draw.line(screen, black, (x_pos*100+20, y_pos*100+80), (x_pos*100+80, y_pos*100+20), line_width)
            #y megrajzolása körrel
            if y == -1:
                pygame.draw.circle(screen, black, (x_pos*100+50, y_pos*100+50), 35, line_width-1)
            x_pos += 1
        y_pos += 1


def check_winner():
    global winner
    global game_over

    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
    for x in range(0, 3):
        if markers[0][x] + markers[1][x] + markers[2][x] == 3:
            winner = 1
            game_over = True
        if markers[0][x] + markers[1][x] + markers[2][x] == -3:
            winner = 2
            game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[0][2] + markers[1][1] + markers[2][0] == -3:
        winner = 2
        game_over = True

    filled = 0
    for x in markers:
        for y in x:
            if y != 0:
                filled += 1
    if filled == 9 and winner != 1 and winner != 2:
        game_over = True
        winner = 3


def draw_winner(winner):
    if winner == 2:
        w_text = 'CPU wins!'
        winner_img = font.render(w_text, 1, black)
        pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_heigth // 2 - 60, 200, 50))
        screen.blit(winner_img, (screen_width // 2 - 90, screen_heigth // 2 - 50))
    if winner == 1:
        w_text = 'Player wins!'
        winner_img = font.render(w_text, 1, black)
        pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_heigth // 2 - 60, 200, 50))
        screen.blit(winner_img, (screen_width // 2 - 90, screen_heigth // 2 - 50))
    if winner == 3:
        w_text = 'Tie'
        winner_img = font.render(w_text, 1, black)
        pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_heigth // 2 - 60, 200, 50))
        screen.blit(winner_img, (screen_width // 2 - 90, screen_heigth // 2 - 50))

    play_again_text = 'Play again?'
    play_again_img = font.render(play_again_text, 1, black)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(play_again_img, (screen_width//2-90, screen_heigth//2+10))


def AI():
    global player
    global markers
    global markers_point

    filled = 0
    for x in markers:
        for y in x:
            if y != 0:
                filled += 1

    #sorok, oszlopok és átlók ellenőrzése, hogy van e 2 egymás mellet a playernek-8p
    #felső sorban lévők
    if (markers[0][1] + markers[0][2] == 2 or markers[1][0] + markers[2][0] == 2 or markers[1][1] + markers[2][2] == 2) and markers_point[0][0] >= 0:
        markers_point[0][0] += 12
    if (markers[0][0] + markers[0][2] == 2 or markers[1][1] + markers[2][1] == 2) and markers_point[0][1] >= 0:
        markers_point[0][1] += 12
    if (markers[0][1] + markers[0][0] == 2 or markers[1][2] + markers[2][2] == 2 or markers[1][1] + markers[2][0] == 2) and markers_point[0][2] >= 0:
        markers_point[0][2] += 12
    # középső sorban lévők
    if (markers[1][1] + markers[1][2] == 2 or markers[0][0] + markers[2][0] == 2) and markers_point[1][0] >= 0:
        markers_point[1][0] += 12
    if (markers[1][0] + markers[1][2] == 2 or markers[0][1] + markers[2][1] == 2 or markers[0][0] + markers[2][2] == 2 or markers[0][2] + markers[2][0] == 2) and markers_point[1][1] >= 0:
        markers_point[1][1] += 12
    if (markers[1][1] + markers[1][0] == 2 or markers[0][2] + markers[2][2] == 2) and markers_point[1][2] >= 0:
        markers_point[1][2] += 12
    # alsó sorban lévők
    if (markers[0][0] + markers[1][0] == 2 or markers[2][1] + markers[2][2] == 2 or markers[1][1] + markers[0][2] == 2) and markers_point[2][0] >= 0:
        markers_point[2][0] += 12
    if (markers[0][1] + markers[1][1] == 2 or markers[2][0] + markers[2][2] == 2) and markers_point[2][1] >= 0:
        markers_point[2][1] += 12
    if (markers[0][2] + markers[1][2] == 2 or markers[2][0] + markers[2][1] == 2 or markers[1][1] + markers[0][0] == 2) and markers_point[2][2] >= 0:
        markers_point[2][2] += 12

    #sorok, oszlopok és átlók ellenőrzése, hogy van e 2 egymás mellet a CPUnak-10p
    # felső sorban lévők
    if (markers[0][1] + markers[0][2] == -2 or markers[1][0] + markers[2][0] == -2 or markers[1][1] + markers[2][2] == -2) and markers_point[0][0] >= 0:
        markers_point[0][0] += 15
    if (markers[0][0] + markers[0][2] == -2 or markers[1][1] + markers[2][1] == -2) and markers_point[0][1] >= 0:
        markers_point[0][1] += 15
    if (markers[0][1] + markers[0][0] == -2 or markers[1][2] + markers[2][2] == -2 or markers[1][1] + markers[2][0] == -2) and markers_point[0][2] >= 0:
        markers_point[0][2] += 15
    # középső sorban lévők
    if (markers[1][1] + markers[1][2] == -2 or markers[0][0] + markers[2][0] == -2) and markers_point[1][0] >= 0:
        markers_point[1][0] += 15
    if (markers[1][0] + markers[1][2] == -2 or markers[0][1] + markers[2][1] == -2 or markers[0][0] + markers[2][2] == -2 or markers[0][2] + markers[2][0] == -2) and markers_point[1][1] >= 0:
        markers_point[1][1] += 15
    if (markers[1][1] + markers[1][0] == -2 or markers[0][2] + markers[2][2] == -2) and markers_point[1][2] >= 0:
        markers_point[1][2] += 15
    # alsó sorban lévők
    if (markers[0][0] + markers[1][0] == -2 or markers[2][1] + markers[2][2] == -2 or markers[1][1] + markers[0][2] == -2) and markers_point[2][0] >= 0:
        markers_point[2][0] += 15
    if (markers[0][1] + markers[1][1] == -2 or markers[2][0] + markers[2][2] == -2) and markers_point[2][1] >= 0:
        markers_point[2][1] += 15
    if (markers[0][2] + markers[1][2] == -2 or markers[2][0] + markers[2][1] == -2 or markers[1][1] + markers[0][0] == -2) and markers_point[2][2] >= 0:
        markers_point[2][2] += 15


    #v alak megelőzésének ellenőrzése
    #az oldal közepén lévő v alak a sarokba
    if (markers[1][0] + markers[0][1] == 2) and (markers[0][0] != -1 and markers[0][2] != -1 and markers[2][0] != -1) and (markers_point[0][0] >= 0):
        markers_point[0][0] += 5
    if (markers[1][0] + markers[2][1] == 2) and (markers[0][0] != -1 and markers[2][0] != -1 and markers[2][2] != -1) and (markers_point[2][0] >= 0):
        markers_point[2][0] += 5
    if (markers[0][1] + markers[1][2] == 2) and (markers[0][0] != -1 and markers[0][2] != -1 and markers[2][2] != -1) and (markers_point[0][2] >= 0):
        markers_point[0][2] += 5
    if (markers[2][1] + markers[1][2] == 2) and (markers[2][0] != -1 and markers[2][2] != -1 and markers[0][2] != -1) and (markers_point[2][2] >= 0):
        markers_point[2][2] += 5
    #oldal közepén lévő v alak középre
    if (markers[1][0] + markers[0][1] == 2) and markers[1][1] != -1 and markers[2][1] != -1 and markers[1][2] != -1 and markers_point[1][1] >= 0:
        markers_point[1][1] += 5
    if (markers[1][0] + markers[2][1] == 2) and markers[1][1] != -1 and markers[0][1] != -1 and markers[1][2] != -1 and markers_point[1][1] >= 0:
        markers_point[1][1] += 5
    if (markers[0][1] + markers[1][2] == 2) and markers[1][1] != -1 and markers[2][1] != -1 and markers[1][0] != -1 and markers_point[1][1] >= 0:
        markers_point[1][1] += 5
    if (markers[2][1] + markers[1][2] == 2) and markers[1][1] != -1 and markers[0][1] != -1 and markers[1][0] != -1 and markers_point[1][1] >= 0:
        markers_point[1][1] += 5
    #sarkokban lévő v alak
    if (markers[2][0] + markers[0][2] == 2) and (markers[0][0] != -1 and markers[0][1] != -1 and markers[1][0] != -1) and (markers_point[0][0] >= 0):
        markers_point[0][0] += 5
    if (markers[0][0] + markers[2][2] == 2) and (markers[1][0] != -1 and markers[2][0] != -1 and markers[2][1] != -1) and (markers_point[2][0] >= 0):
        markers_point[2][0] += 5
    if (markers[0][0] + markers[2][2] == 2) and (markers[0][1] != -1 and markers[0][2] != -1 and markers[1][2] != -1) and (markers_point[0][2] >= 0):
        markers_point[0][2] += 5
    if (markers[2][0] + markers[0][2] == 2) and (markers[2][1] != -1 and markers[2][2] != -1 and markers[1][2] != -1) and (markers_point[2][2] >= 0):
        markers_point[2][2] += 5
    #sarokban és oldal közepén lévő v alak
    if (markers[2][0] + markers[0][1] == 2 and markers[1][0] != -1 and markers[0][0] != -1 and markers[0][2] != -1) and (markers_point[0][0] >= 0):
        markers_point[0][0] += 5
    if (markers[2][0] + markers[0][1] == 2 and markers[1][1] != -1 and markers[2][1] != -1 and markers[2][2] != -1) and (markers_point[2][1] >= 0):
        markers_point[2][1] += 5
    if (markers[1][0] + markers[0][2] == 2 and markers[0][0] != -1 and markers[0][1] != -1 and markers[2][0] != -1) and (markers_point[0][0] >= 0):
        markers_point[0][0] += 5
    if (markers[1][0] + markers[0][2] == 2 and markers[1][1] != -1 and markers[1][2] != -1 and markers[2][2] != -1) and (markers_point[1][2] >= 0):
        markers_point[1][2] += 5
    if (markers[0][0] + markers[2][1] == 2 and markers[1][0] != -1 and markers[2][0] != -1 and markers[2][2] != -1) and (markers_point[2][0] >= 0):
        markers_point[2][0] += 5
    if (markers[0][0] + markers[2][1] == 2 and markers[0][1] != -1 and markers[1][1] != -1 and markers[0][2] != -1) and (markers_point[0][1] >= 0):
        markers_point[0][1] += 5
    if (markers[1][0] + markers[2][2] == 2 and markers[2][0] != -1 and markers[2][1] != -1 and markers[0][0] != -1) and (markers_point[2][0] >= 0):
        markers_point[2][0] += 5
    if (markers[1][0] + markers[2][2] == 2 and markers[1][1] != -1 and markers[1][2] != -1 and markers[0][2] != -1) and (markers_point[1][2] >= 0):
        markers_point[1][2] += 5
    if (markers[0][0] + markers[1][2] == 2 and markers[0][1] != -1 and markers[0][2] != -1 and markers[2][2] != -1) and (markers_point[0][2] >= 0):
        markers_point[0][2] += 5
    if (markers[0][0] + markers[1][2] == 2 and markers[1][0] != -1 and markers[1][1] != -1 and markers[2][0] != -1) and (markers_point[1][0] >= 0):
        markers_point[1][0] += 5
    if (markers[0][1] + markers[2][2] == 2 and markers[0][0] != -1 and markers[0][2] != -1 and markers[1][2] != -1) and (markers_point[0][2] >= 0):
        markers_point[0][2] += 5
    if (markers[0][1] + markers[2][2] == 2 and markers[1][1] != -1 and markers[2][1] != -1 and markers[2][0] != -1) and (markers_point[2][1] >= 0):
        markers_point[2][1] += 5
    if (markers[2][0] + markers[1][2] == 2 and markers[2][1] != -1 and markers[2][2] != -1 and markers[0][2] != -1) and (markers_point[2][2] >= 0):
        markers_point[2][2] += 5
    if (markers[2][0] + markers[1][2] == 2 and markers[1][0] != -1 and markers[0][0] != -1 and markers[1][1] != -1) and (markers_point[1][0] >= 0):
        markers_point[1][0] += 5
    if (markers[0][1] + markers[2][2] == 2 and markers[0][0] != -1 and markers[0][2] != -1 and markers[1][2] != -1) and (markers_point[0][1] >= 0):
        markers_point[0][2] += 5
    if (markers[0][2] + markers[2][1] == 2 and markers[0][0] != -1 and markers[0][1] != -1 and markers[1][1] != -1) and (markers_point[0][1] >= 0):
        markers_point[0][1] += 5
    if (markers[2][1] + markers[0][2] == 2 and markers[2][2] != -1 and markers[2][0] != -1 and markers[1][1] != -1) and (markers_point[2][2] >= 0):
        markers_point[2][2] += 5
    if (markers[0][1] + markers[2][2] == 2 and markers[1][1] != -1 and markers[2][1] != -1 and markers[2][0] != -1) and (markers_point[2][1] >= 0):
        markers_point[2][1] += 5

    #sarok-közép->döntetlen
    if (markers[0][0] == 1 and markers[1][1] == -1 and markers[2][2] == 1) or (markers[2][0] == 1 and markers[1][1] == -1 and markers[0][2] == 1):
        markers_point[2][1] += 6
        markers_point[1][2] += 6
        markers_point[1][0] += 6
        markers_point[0][1] += 6

    #ha sarokba kezd a player
    if markers[0][0] == 1 and filled == 1:
        markers_point[0][2] += 6
        markers_point[2][0] += 6
    if markers[0][2] == 1 and filled == 1:
        markers_point[0][0] += 6
        markers_point[2][2] += 6
    if markers[2][0] == 1 and filled == 1:
        markers_point[0][0] += 6
        markers_point[2][2] += 6
    if markers[2][2] == 1 and filled == 1:
        markers_point[0][2] += 6
        markers_point[2][0] += 6

    # dupla v alak megelőzése
    if markers[0][1] == 1 and filled == 1:
        markers_point[0][0] += 1
        markers_point[0][2] += 1
        markers_point[1][0] += 1
        markers_point[1][1] += 2
        markers_point[1][2] += 1
        markers_point[2][1] += 2
    if markers[1][0] == 1 and filled == 1:
        markers_point[0][0] += 1
        markers_point[2][0] += 1
        markers_point[0][1] += 1
        markers_point[1][1] += 2
        markers_point[2][1] += 1
        markers_point[1][2] += 2
    if markers[2][1] == 1 and filled == 1:
        markers_point[2][0] += 1
        markers_point[2][2] += 1
        markers_point[1][0] += 1
        markers_point[1][1] += 2
        markers_point[1][2] += 1
        markers_point[0][1] += 2
    if markers[1][2] == 1 and filled == 1:
        markers_point[0][2] += 1
        markers_point[2][2] += 1
        markers_point[0][1] += 1
        markers_point[1][1] += 2
        markers_point[2][1] += 1
        markers_point[1][0] += 2


    max = -1
    #megnézi, hogy hol van a legtöbb pontos cella
    for x in range(3):
        for y in range(3):
            if markers_point[x][y] >= max:
                max = markers_point[x][y]

    max_count = 0
    for x in markers_point:
        max_count += x.count(max)

    ai_pick = random.randint(1, max_count)
    max_was = 0
    x_index, y_index = 0, 0
    for x in range(3):
        for y in range(3):
            if markers_point[x][y] == max:
                max_was += 1
            if max_was == ai_pick:
                x_index = x
                y_index = y
                max_was += 1

    markers[x_index][y_index] = -1
    print(markers_point)
    markers_point[x_index][y_index] = -100


run = True
while run:

    #háttér rajzolása
    draw_window()

    #kilépés
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over and player == 1:
            #cellába kattintás keresése
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                x_pos = pos[0]
                y_pos = pos[1]
                if markers[y_pos//100][x_pos//100] == 0:
                    markers[y_pos // 100][x_pos//100] = 1
                    markers_point[y_pos // 100][x_pos//100] = -100
                    player *= -1
                    check_winner()

    #csak akkor tehet az AI, amikor még nincs mind a 9 hely teli
    filled = 0
    for x in markers:
        for y in x:
            if y != 0:
                filled += 1

    if player == -1 and filled != 9 and winner != 1:
        AI()
        check_winner()
        player *= -1
        
    draw_markers()

    if game_over:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                player = 1
                winner = 0
                clicked = False
                game_over = False
                markers = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                markers_point = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]

    #képernyő frissítése
    pygame.display.update()

pygame.quit()

