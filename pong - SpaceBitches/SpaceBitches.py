import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.load('Butterfly.mp3')
pygame.mixer.music.play(-1)
# barulho_colisao = pygame.mixer.Sound('smw_kick.wav')

window = pygame.display.set_mode([1220,686])
window_title = pygame.display.set_caption("Space Bitches")

win = pygame.image.load("assets/win.png")
espaço = pygame.image.load("assets/espaço.jpg")

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")

score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 343
player1_moveup = False
player1_movedown = False 

player2 = pygame.image.load("assets/player2.png")
player2_y = 343
player2_moveup = False
player2_movedown = False 

lua = pygame.image.load("assets/lua.png")
lua_x, lua_y = 610, 343
lua_dirx, lua_diry = -1, 0.5

def move_player1():
    global player1_y
    
    if player1_movedown:
        player1_y += 5
    if player1_moveup:
        player1_y -= 5
    
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 480:
        player1_y = 480

def move_player2():
    global player2_y

    if player2_movedown:
        player2_y += 5
    if player2_moveup:
        player2_y -= 5
    
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 480:
        player2_y = 480

def move_ball():
    global lua_x, lua_y, lua_dirx, lua_diry
    global score1, score2, score1_img, score2_img

    lua_x += lua_dirx
    lua_y += lua_diry

    if lua_x < 275:
        if player1_y < lua_y + 43:
            if player1_y + 120 > lua_y:
                lua_dirx *= -1
                #barulho_colisao.play()

    if lua_x > 900:
        if player2_y < lua_y + 43:
            if player2_y + 120 > lua_y:
                lua_dirx *= -1
                #barulho_colisao.play()

    if lua_y > 620 or lua_y <= -10:
        lua_diry *= -1

    if lua_x < -130:
        lua_x, lua_y = 617, 337
        lua_diry *= -1
        lua_dirx *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")

    elif lua_x > 1410:
        lua_x, lua_y = 617, 337
        lua_diry *= -1
        lua_dirx *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")
        # barulho_vida.play()

game_over = False

def draw():
    global game_over
    
    if score1 > 10:
        window.blit(win,(70,100))
        pygame.mixer.music.stop()
        game_over = True
        
    elif score2 > 10:
        window.blit(win,(800,100))
        pygame.mixer.music.stop()
        game_over = True
       
    else:
        window.blit(espaço,( 0, 0))
        window.blit(player1,(20, player1_y)) 
        window.blit(player2,(1050, player2_y))
        window.blit(lua,(lua_x, lua_y))
        window.blit(score1_img, (470, 20))
        window.blit(score2_img, (640, 20))
        move_player1()
        move_player2()
        move_ball()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: player1_moveup = True
                if event.key == pygame.K_s: player1_movedown = True
                if event.key == pygame.K_UP: player2_moveup = True
                if event.key == pygame.K_DOWN: player2_movedown = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: player1_moveup = False
                if event.key == pygame.K_s: player1_movedown = False
                if event.key == pygame.K_UP: player2_moveup = False
                if event.key == pygame.K_DOWN: player2_movedown = False
    
    draw()
    pygame.display.update()