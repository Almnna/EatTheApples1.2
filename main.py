#############################|
###########PROGRAMMED########|
###############BY############|
#############AHMAD###########|
############MUSTAFA##########|
#############ALMNNA###########|
##############################|
#NICK-NAME##JASONDZ##########|
#############################|
####THIS-GAME-IS-OPEN-SOURCE#|
###SO-ANY-ONE-CAN-EDIT##|
########IT-AND-DO-WHAT-EVER##|
#########HE-WANT'S###########|
###########DONE##############|
############AT###############|
###########1:13PM############|
###########7/22/2018#########|
#EAT#THE#APPLES#V2.0#########|
#############################|




import pygame
from pygame import *
import time
import random
import math
from math import *

init()

#color's Defenations#
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
    

#Load Image's#
bg = image.load('background/eat the apples bg.gif')
player_right1 = image.load('turtle right/turtle1.gif')
player_right2 = image.load('turtle right/turtle2.gif')
player_right3 = image.load('turtle right/turtle3.gif')
player_right4 = image.load('turtle right/turtle4.gif')
player_left1 = image.load('turtle left/turtle11.gif')
player_left2 = image.load('turtle left/turtle22.gif')
player_left3 = image.load('turtle left/turtle33.gif')
player_left4 = image.load('turtle left/turtle44.gif')
block = image.load('ground block/ground_block.gif')
ground_lock = image.load('ground block/ground_lock.gif')
red_apple = image.load('apples/apple.gif')
green_apple = image.load('apples/apple3.gif')
purple_apple = image.load('apples/apple2.gif')
live = image.load('live/live.gif')
pause = image.load('messages/pause.gif')
fall = image.load('messages/fall.gif')
rebuild_soild = image.load('messages/rebuild.gif')
not_enough = image.load('messages/not_enough.gif')
no_broken_solid = image.load('messages/no_broken_solid.gif')
lives_increased = image.load('messages/lives_increased.gif')
gameoverpic = image.load('background/gameoverpic.png')
intropic = image.load('intro/intropic.gif')
play_button_active = image.load('intro/play_button_active.gif')
play_button_inactive = image.load('intro/play_button_inactive.gif')
how_to_play_button_active = image.load('intro/how_to_play_button_active.gif')
how_to_play_button_inactive = image.load('intro/how_to_play_button_inactive.gif')
quit_button_active = image.load('intro/quit_button_active.gif')
quit_button_inactive = image.load('intro/quit_button_inactive.gif')
how_to_pic = image.load('intro/how to play.gif')
exit_how_to = image.load('intro/exit how to.gif')
icon = image.load('background/icon.png')
###########################################_____________SOUND'S_______________###################################
eat_sound = pygame.mixer.music.load('sound effect/bite/Bite Sounds _ Free Sound Effects _ Bite Sound Clips _ Sound Bites.wav')
button_sound = pygame.mixer.music.load('sound effect/button/button.wav')
explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
gameover_sound = pygame.mixer.music.load('sound effect/gameover/Game Over Sound _ Free Sounds from Orange Free Sounds.wav')
fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
##################################################################################################################
##display_setting##   
display_width = 600  
display_height = 500
screen = display.set_mode((display_width, display_height),FULLSCREEN)
screen_name = display.set_caption('eat the apples')
icon1 = display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 15
#block_positions#
#1-5#    
block_x1 = 0
block_y1 = 440
block_x2 = 40
block_y2 = 440
block_x3 = 80
block_y3 = 440
block_x4 = 120
block_y4 = 440
block_x5 = 160
block_y5 = 440
##############
#6-10#
block_x6 = 200
block_y6 = 440
block_x7 = 240
block_y7 = 440
block_x8 = 280
block_y8 = 440
block_x9 = 320
block_y9 = 440
block_x10 = 360
block_y10 = 440
###############
#11-15#
block_x11 = 400
block_y11 = 440
block_x12 = 440
block_y12 = 440
block_x13 = 480
block_y13 = 440
block_x14 = 520
block_y14 = 440
block_x15 = 560
block_y15 = 440
##################
#player_positions#
player_x = 280
player_y = 425
#move_Player#
player_left_x = 0
player_right_x = 0
#player_State
player_s = "turtle1"
lives = 5
FALL = False
#apple_state's#
apple_x_move = random.choice([10,40,80,120,160,200,240,280,320,360,400,440,480,520,560]) #random.randrange(20,570)
apple_y_move = -10
green_apple_x = random.randrange(20,570)
green_apple_y = -30
purple_apple_x = random.randrange(20,570)
purple_apple_y = -30
#block_State's
block1s = "placed"
block2s = "placed"
block3s = "placed"
block4s = "placed"
block5s = "placed"
block6s = "placed"
block7s = "placed"
block8s = "placed"
block9s = "placed"
block10s = "placed"
block11s = "placed"
block12s = "placed"
block13s = "placed"
block14s = "placed"
block15s = "placed"
##################
broken_block = False
##################
#block_images#
block1pic = block
block2pic = block
block3pic = block
block4pic = block
block5pic = block
block6pic = block
block7pic = block
block8pic = block
block9pic = block
block10pic = block
block11pic = block
block12pic = block
block13pic = block
block14pic = block
block15pic = block
#red_apple_score#
red_apple_score = 0


def gamereset():
    global white,black,red,green,bg,player_right1,player_right2,player_right3,player_right4,player_left1,player_left2,player_left3
    global player_x,player_y,player_left_x,player_right_x,player_s,apple_x_move,apple_y_move,red_apple_score
    global green_apple_x,green_apple_y,purple_apple_x,purple_apple_y,lives
    global block_x1,block_y1,block_x2,block_y2,block_x3,block_y3,block_x4,block_y4,block_x5,block_y5,block_x6,block_y6
    global block_x7,block_y7,block_x8,block_y8,block_x9,block_y9,block_x10,block_y10,block_x11,block_y11,block_x12,block_y12
    global block_x13,block_y13,block_x14,block_y14,block_x15,block_y15
    global block1s,block2s,block3s,block4s,block5s,block6s,block7s,block8s,block9s,block10s
    global block11s,block12s,block13s,block14s,block15s
    global block1pic,block2pic,block3pic,block4pic,block5pic,block6pic,block7pic
    global block8pic,block9pic,block10pic,block11pic,block12pic,block13pic,block14pic,block15pic,FALL,broken_block,FPS
    #color's Defenations#
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,155,0)
    

    #Load Image's#
    bg = image.load('background/eat the apples bg.gif')
    player_right1 = image.load('turtle right/turtle1.gif')
    player_right2 = image.load('turtle right/turtle2.gif')
    player_right3 = image.load('turtle right/turtle3.gif')
    player_right4 = image.load('turtle right/turtle4.gif')
    player_left1 = image.load('turtle left/turtle11.gif')
    player_left2 = image.load('turtle left/turtle22.gif')
    player_left3 = image.load('turtle left/turtle33.gif')
    player_left4 = image.load('turtle left/turtle44.gif')
    block = image.load('ground block/ground_block.gif')
    ground_lock = image.load('ground block/ground_lock.gif')
    red_apple = image.load('apples/apple.gif')
    green_apple = image.load('apples/apple3.gif')
    purple_apple = image.load('apples/apple2.gif')
    live = image.load('live/live.gif')
    pause = image.load('messages/pause.gif')
    fall = image.load('messages/fall.gif')
    rebuild_soild = image.load('messages/rebuild.gif')
    not_enough = image.load('messages/not_enough.gif')
    no_broken_solid = image.load('messages/no_broken_solid.gif')
    lives_increased = image.load('messages/lives_increased.gif')
    gameoverpic = image.load('background/gameoverpic.png')
    intropic = image.load('intro/intropic.gif')
    play_button_active = image.load('intro/play_button_active.gif')
    play_button_inactive = image.load('intro/play_button_inactive.gif')
    how_to_play_button_active = image.load('intro/how_to_play_button_active.gif')
    how_to_play_button_inactive = image.load('intro/how_to_play_button_inactive.gif')
    quit_button_active = image.load('intro/quit_button_active.gif')
    quit_button_inactive = image.load('intro/quit_button_inactive.gif')
    how_to_pic = image.load('intro/how to play.gif')
    exit_how_to = image.load('intro/exit how to.gif')
    ###########################################_____________SOUND'S_______________###################################
    eat_sound = pygame.mixer.music.load('sound effect/bite/Bite Sounds _ Free Sound Effects _ Bite Sound Clips _ Sound Bites.wav')
    button_sound = pygame.mixer.music.load('sound effect/button/button.wav')
    explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
    gameover_sound = pygame.mixer.music.load('sound effect/gameover/Game Over Sound _ Free Sounds from Orange Free Sounds.wav')
    fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
    ##################################################################################################################
    ##display_setting##
    display_width = 600  
    display_height = 500
    screen = display.set_mode((display_width, display_height))
    screen_name = display.set_caption('eat the apples')
    clock = pygame.time.Clock()
    FPS = 15
    #block_positions#
    #1-5#    
    block_x1 = 0
    block_y1 = 440
    block_x2 = 40
    block_y2 = 440
    block_x3 = 80
    block_y3 = 440
    block_x4 = 120
    block_y4 = 440
    block_x5 = 160
    block_y5 = 440
    ##############
    #6-10#
    block_x6 = 200
    block_y6 = 440
    block_x7 = 240
    block_y7 = 440
    block_x8 = 280
    block_y8 = 440
    block_x9 = 320
    block_y9 = 440
    block_x10 = 360
    block_y10 = 440
    ###############
    #11-15#
    block_x11 = 400
    block_y11 = 440
    block_x12 = 440
    block_y12 = 440
    block_x13 = 480
    block_y13 = 440
    block_x14 = 520
    block_y14 = 440
    block_x15 = 560
    block_y15 = 440
    ##################
    #player_positions#
    player_x = 280
    player_y = 425
    #move_Player#
    player_left_x = 0
    player_right_x = 0
    #player_State
    player_s = "turtle1"
    lives = 5
    FALL = False
    #apple_state's#
    apple_x_move = random.choice([10,40,80,120,160,200,240,280,320,360,400,440,480,520,560]) #random.randrange(20,570)
    apple_y_move = -10
    green_apple_x = random.randrange(20,570)
    green_apple_y = -30
    purple_apple_x = random.randrange(20,570)
    purple_apple_y = -30
    #block_State's
    block1s = "placed"
    block2s = "placed"
    block3s = "placed"
    block4s = "placed"
    block5s = "placed"
    block6s = "placed"
    block7s = "placed"
    block8s = "placed"
    block9s = "placed"
    block10s = "placed"
    block11s = "placed"
    block12s = "placed"
    block13s = "placed"
    block14s = "placed"
    block15s = "placed"
    ##################
    broken_block = False
    ##################
    #block_images#
    block1pic = block
    block2pic = block
    block3pic = block
    block4pic = block
    block5pic = block
    block6pic = block
    block7pic = block
    block8pic = block
    block9pic = block
    block10pic = block
    block11pic = block
    block12pic = block
    block13pic = block
    block14pic = block
    block15pic = block
    #red_apple_score#
    red_apple_score = 0


    
#screen_messages#
sys_font = font.SysFont(None, 25)
font = font.SysFont(None, 80)
def lives_message(msg,color):
    screen_text = sys_font.render(msg, True, color)
    screen.blit(screen_text, [20,2])

def redapple_message(msg,color):
    screen_text = sys_font.render(msg, True, color)
    screen.blit(screen_text, [20,25])

def game_speed_message(msg,color):
    screen_text = sys_font.render(msg, True, color)
    screen.blit(screen_text, [459,2])
    

def apple_ground_collision(applex,groundx,appley,groundy):
    if((applex - groundx) <= 20 and (applex - groundx) >= 0):
         if((groundy - appley) < 0):
              tt = (groundy - appley) * -1
         else:
              tt = groundy - appley 
              if(tt <= 20):
                  return True
              else:
                  return False

def player_ground_collision(playerx,groundx,playery,groundy):
    if((playerx - groundx) <= 10 and (playerx - groundx) >= 0):
         if((groundy - playery) < 0):
              tt = (groundy - playery) * -1
         else:
              tt = groundy - playery 
              if(tt <= 30 and tt >= 0):
                  return True
              else:
                  return False

def broke_if_near():
    global  player_y,apple_y_move,apple_x_move
    global  block_x1,block_y1,block_x2,block_y2,block_x3,block_y3,block_x4,block_y4,block_x5,block_y5,block_x6,block_y6
    global  block_x7,block_y7,block_x8,block_y8,block_x9,block_y9,block_x10,block_y10,block_x11,block_y11,block_x12,block_y12
    global  block_x13,block_y13,block_x14,block_y14,block_x15,block_y15
    global  block1s
    global  block2s
    global  block3s
    global  block4s
    global  block5s
    global  block6s
    global  block7s
    global  block8s
    global  block9s
    global  block10s
    global  block11s
    global  block12s
    global  block13s
    global  block14s
    global  block15s
    global block1pic,block2pic,block3pic,block4pic,block5pic,block6pic,block7pic
    global block8pic,block9pic,block10pic,block11pic,block12pic,block13pic,block14pic,block15pic
    #RED___APPLE_GROUND_COLLISION#
    #1-------------5#
    if apple_ground_collision(apple_x_move,block_x1,apple_y_move,block_y1):
        if(block1s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block1s = "unplaced"
            block1pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x2,apple_y_move,block_y2):
        if(block2s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block2s = "unplaced"
            block2pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x3,apple_y_move,block_y3):
        if(block3s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block3s = "unplaced"
            block3pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x4,apple_y_move,block_y4):
        if(block4s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block4s = "unplaced"
            block4pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x5,apple_y_move,block_y5):
        if(block5s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block5s = "unplaced"
            block5pic = ground_lock
    #6-------------10#
    if apple_ground_collision(apple_x_move,block_x6,apple_y_move,block_y6):
        if(block6s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block6s = "unplaced"
            block6pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x7,apple_y_move,block_y7):
        if(block7s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block7s = "unplaced"
            block7pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x8,apple_y_move,block_y8):
        if(block8s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block8s = "unplaced"
            block8pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x9,apple_y_move,block_y9):
        if(block9s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block9s = "unplaced"
            block9pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x10,apple_y_move,block_y10):
        if(block10s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block10s = "unplaced"
            block10pic = ground_lock
    #11-------------15#
    if apple_ground_collision(apple_x_move,block_x11,apple_y_move,block_y11):
        if(block11s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block11s = "unplaced"
            block11pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x12,apple_y_move,block_y12):
        if(block12s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block12s = "unplaced"
            block12pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x13,apple_y_move,block_y13):
        if(block13s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block13s = "unplaced"
            block13pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x14,apple_y_move,block_y14):
        if(block14s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block14s = "unplaced"
            block14pic = ground_lock
    if apple_ground_collision(apple_x_move,block_x15,apple_y_move,block_y15):
        if(block15s == "placed"):
            explosion_sound = pygame.mixer.music.load('sound effect/explosion/explosion.wav')
            explosion_sound = pygame.mixer.music.play()
            block15s = "unplaced"
            block15pic = ground_lock
    #########################################################################


def respawn_if_fall():
    global block1s,block2s,block3s,block4s,block5s,block6s,block7s,block8s,block9s,block10s
    global block11s,block12s,block13s,block14s,block15s,player_x,player_y
    if (block1s == "placed"):
         player_x = 0
         player_y = 425
    elif(block2s == "placed"):
          player_x = 40
          player_y = 425
    elif(block3s == "placed"):
          player_x = 80
          player_y = 425
    elif(block4s == "placed"):
          player_x = 120
          player_y = 425
    elif(block5s == "placed"):
          player_x = 160
          player_y = 425
    elif(block6s == "placed"):
          player_x = 200
          player_y = 425
    elif(block7s == "placed"):
          player_x = 240
          player_y = 425
    elif(block8s == "placed"):
          player_x = 280
          player_y = 425
    elif(block9s == "placed"):
          player_x = 320
          player_y = 425
    elif(block10s == "placed"):
          player_x = 360
          player_y = 425
    elif(block11s == "placed"):
          player_x = 400
          player_y = 425
    elif(block12s == "placed"):
          player_x = 425
          player_y = 425
    elif(block13s == "placed"):
          player_x = 480
          player_y = 425
    elif(block14s == "placed"):
          player_x = 520
          player_y = 425
    elif(block15s == "placed"):
          player_x = 560
          player_y = 425
          
def fall_if_not_equal():
    global  block1s,block2s,block3s,block4s,block5s,block6s,block7s,block8s,block9s,block10s
    global block11s,block12s,block13s,block14s,block15s,player_y
    global block_x1,block_y1,block_x2,block_y2,block_x3,block_y3,block_x4,block_y4,block_x5,block_y5,block_x6,block_y6
    global block_x7,block_y7,block_x8,block_y8,block_x9,block_y9,block_x10,block_y10,block_x11,block_y11,block_x12,block_y12
    global block_x13,block_y13,block_x14,block_y14,block_x15,block_y15,lives,FPS,FALL
    if player_ground_collision(player_x,block_x1,player_y,block_y1):
        if(block1s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
            
    if player_ground_collision(player_x,block_x2,player_y,block_y2):
        if(block2s != "placed"):

            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x3,player_y,block_y3):
        if(block3s != "placed"):

            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x4,player_y,block_y4):
        if(block4s != "placed"):

            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x5,player_y,block_y5):
        if(block5s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x6,player_y,block_y6):
        if(block6s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x7,player_y,block_y7):
        if(block7s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x8,player_y,block_y8):
        if(block8s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x9,player_y,block_y9):
        if(block9s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x10,player_y,block_y10):
        if(block10s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x11,player_y,block_y11):
        if(block11s != "placed"):
            FALL = True
            player_y = 540
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x12,player_y,block_y12):
        if(block12s != "placed"):
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            FALL = True
            player_y = 540
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x13,player_y,block_y13):
        if(block13s != "placed"):
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            FALL = True
            player_y = 540
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x14,player_y,block_y14):
        if(block14s != "placed"):
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            FALL = True
            player_y = 540
            respawn_if_fall()
            lives -= 1
    if player_ground_collision(player_x,block_x15,player_y,block_y15):
        if(block15s != "placed"):
            fall_sound = pygame.mixer.music.load('sound effect/fall/Fall And Splat-SoundBible.com-1428277441.wav')
            fall_sound = pygame.mixer.music.play()
            time.sleep(0.01)
            FALL = True
            player_y = 540
            respawn_if_fall()
            lives -= 1
            

def rebuild():
    global block1s,block2s,block3s,block4s,block5s,block6s,block7s,block8s,block9s,block10s
    global block11s,block12s,block13s,block14s,block15s
    global block_y1,block_y2,block_y3,block_y4,block_y5,block_y6,block_y7,block_y8,block_y9,block_y10
    global block_y11,block_y12,block_y13,block_y14,block_y15
    global block1pic,block2pic,block3pic,block4pic,block5pic,block6pic,block7pic,broken_block
    global block8pic,block9pic,block10pic,block11pic,block12pic,block13pic,block14pic,block15pic,red_apple_score
    onetime = 1
    if(onetime == 1):
        if(block1s == "unplaced"):
            block1s = "placed"
            block1pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block2s == "unplaced"):
            block2s = "placed"
            block2pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block3s == "unplaced"):
            block3s = "placed"
            block3pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block4s == "unplaced"):
            block4s = "placed"
            block4pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block5s == "unplaced"):
            block5s = "placed"
            block5pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block6s == "unplaced"):
            block6pic = block
            
            block6s = "placed"
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block7s == "unplaced"):
            block7s = "placed"
            block7pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block8s == "unplaced"):
            block8s = "placed"
            block8pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block9s == "unplaced"):
            block9s = "placed"
            block9pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block10s == "unplaced"):
            block10s = "placed"
            block10pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block11s == "unplaced"):
            block11s = "placed"
            block11pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block12s == "unplaced"):
            block12s = "placed"
            block12pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block13s == "unplaced"):
            block13s = "placed"
            block13pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block14s == "unplaced"):
            block14s = "placed"
            block14pic = block
            
            onetime -= 1
            broken_block = True
    if(onetime == 1):
        if(block15s == "unplaced"):
            block15s = "placed"
            block15pic = block
            
            onetime -= 1
            broken_block = True
            
    if(onetime == 1):
        broken_block = False
        
        


def paused():
    Paused = True
    screen.blit(pause, (0,0))
    #screen.blit(pause, (100,200))
    display.update()
    while Paused == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if(event.type == KEYDOWN):
                if(event.key == K_SPACE):
                    Paused = False
                if(event.key == K_q):
                    pygame.quit()
                    quit()
                    



def gameintro():
    play_x = 100
    play_y = 350
    how_x = 250
    how_y = 350
    quit_x = 400
    quit_y = 350
    exit_how_x = 475
    exit_how_y = 130
    play = play_button_inactive
    how = how_to_play_button_inactive
    quit_ = quit_button_inactive
    how_to = False
    while True:
        click = pygame.mouse.get_pressed()
        cursor = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                
            if ((play_x + 100 > cursor[0] > play_x) and (play_y + 50 > cursor[1] > play_y)):
                if(click[0] == 1):
                    if(how_to != True):
                        button_sound = pygame.mixer.music.load('sound effect/button/button.wav')
                        button_sound = pygame.mixer.music.play()
                        gameloop()

            if ((how_x + 100 > cursor[0] > how_x) and (how_y + 50 > cursor[1] > how_y)):
                if(click[0] == 1):
                    button_sound = pygame.mixer.music.load('sound effect/button/button.wav')
                    button_sound = pygame.mixer.music.play()
                    how_to = True
                    

            if ((quit_x + 100 > cursor[0] > quit_x) and (quit_y + 50 > cursor[1] > quit_y)):
                if(click[0] == 1):
                    if(how_to != True):
                        button_sound = pygame.mixer.music.load('sound effect/button/button.wav')
                        button_sound = pygame.mixer.music.play()
                        pygame.quit()
                        quit()
            if ((exit_how_x + 25 > cursor[0] > exit_how_x) and (exit_how_y + 25 > cursor[1] > exit_how_y)):
                if(click[0] == 1):
                    button_sound = pygame.mixer.music.load('sound effect/button/button.wav')
                    button_sound = pygame.mixer.music.play()
                    how_to = False
                    
                
        if ((play_x + 100 > cursor[0] > play_x) and (play_y + 50 > cursor[1] > play_y)):
            play = play_button_active
        else:
            play = play_button_inactive
        if ((how_x + 100 > cursor[0] > how_x) and (how_y + 50 > cursor[1] > how_y)):
            how = how_to_play_button_active
        else:
            how = how_to_play_button_inactive
        if ((quit_x + 100 > cursor[0] > quit_x) and (quit_y + 50 > cursor[1] > quit_y)):
            quit_ = quit_button_active
        else:
            quit_ = quit_button_inactive

        screen.blit(intropic, (0,0))
        screen.blit(play,(play_x,play_y))
        screen.blit(how,(how_x,how_y))
        screen.blit(quit_,(quit_x,quit_y))
        if(how_to == True):
            screen.blit(how_to_pic,(100,130))
        if(how_to == True):
            screen.blit(exit_how_to,(exit_how_x,exit_how_y))
        display.update()
                    
        
def gameover():
    global lives
    gameover_sound = pygame.mixer.music.load('sound effect/gameover/Game Over Sound _ Free Sounds from Orange Free Sounds.wav')
    gameover_sound = pygame.mixer.music.play()
    screen.blit(gameoverpic, (0,0))
    display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if(event.type == KEYDOWN):
                if(event.key == K_r):
                    lives += 5
                    gamereset()
                    gameloop()
                if(event.key == K_q):
                    pygame.quit()
                    quit()
                    
        
    
def gameloop():
    global player_x,player_y,player_left_x,player_right_x,player_s,apple_x_move,apple_y_move,red_apple_score
    global green_apple_x,green_apple_y,purple_apple_x,purple_apple_y,lives
    global block_x1,block_y1,block_x2,block_y2,block_x3,block_y3,block_x4,block_y4,block_x5,block_y5,block_x6,block_y6
    global block_x7,block_y7,block_x8,block_y8,block_x9,block_y9,block_x10,block_y10,block_x11,block_y11,block_x12,block_y12
    global block_x13,block_y13,block_x14,block_y14,block_x15,block_y15
    global block1s,block2s,block3s,block4s,block5s,block6s,block7s,block8s,block9s,block10s
    global block11s,block12s,block13s,block14s,block15s
    global block1pic,block2pic,block3pic,block4pic,block5pic,block6pic,block7pic
    global block8pic,block9pic,block10pic,block11pic,block12pic,block13pic,block14pic,block15pic,FALL,broken_block,FPS
    fallcounter = 0
    once1 = 1
    once2 = 1
    once3 = 1
    once4 = 1
    gapple = False
    papple = False
    go_right = False
    go_left = False
    score = red_apple_score
    n25 = 1
    n50 = 1
    n75 = 1
    n100 = 1
    n25s = False
    n50s = False
    n75s = False
    n100s = False
    message1 = 0
    message2 = 0
    message3 = 0
    message4 = 0
    message5 = 0
    message6 = 0
    while True:
        if(lives <= 0):
            gameover()
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    if(red_apple_score >= 10):
                        rebuild()
                        if(broken_block == True):
                            red_apple_score -= 10
                            
                            message1 = 30
                        else:
                            message6 = 30
                    else:
                        message2 = 30
                if event.key == K_h:
                    if(red_apple_score >= 20):
                        message3 = 30
                        red_apple_score -= 20
                        heal_sound = pygame.mixer.music.play()
                        lives += 1 
                    else:
                        message4 = 30
                if(event.key == K_SPACE):
                    paused()
                if event.key == K_LEFT:
                    if(player_x != 5):
                        a = random.choice([1,2,3,4])
                        if(a == 1):
                            player_s = "turtle11"
                        elif(a == 2):
                              player_s = "turtle22"
                        elif(a == 3):
                              player_s = "turtle33"
                        elif(a == 4):
                              player_s = "turtle44"
                        go_left = True
                        
                if event.key == K_RIGHT:
                    if(player_x != 570):
                        a = random.choice([1,2,3,4])
                        if(a == 1):
                            player_s = "turtle1"
                        elif(a == 2):
                              player_s = "turtle2"
                        elif(a == 3):
                              player_s = "turtle3"
                        elif(a == 4):
                              player_s = "turtle4"
                        go_right = True
                
            if(event.type == KEYUP):
                if(event.key == K_LEFT):
                    go_left = False
                if(event.key == K_RIGHT):
                    go_right = False
                
        if(FALL == True):
            message5 = 30
            FALL = False

        if(player_x < 570):
            if(go_right == True):
                player_left_x = 12
            
        if(player_x > 6):
            if(go_left == True):
                player_left_x = -12

            
        skin = player_right1
        if(player_s == "turtle11"):
            skin = player_left1
        elif(player_s == "turtle22"):
              skin = player_left2
        elif(player_s == "turtle33"):
              skin = player_left3
        elif(player_s == "turtle44"):
              skin = player_left4
        elif(player_s == "turtle1"):
              skin = player_right1
        elif(player_s == "turtle2"):
              skin = player_right2
        elif(player_s == "turtle3"):
              skin = player_right3
        elif(player_s == "turtle4"):
              skin = player_right4
              
        

            
        player_x += player_left_x
        
        apple_y_move += 10
        if(gapple == True):
            green_apple_y += 10
        if(papple == True):
            purple_apple_y += 10
        

        if(apple_y_move > 500):
            apple_x_move = random.choice([10,40,80,120,160,200,240,280,320,360,400,440,480,520,560])
            apple_y_move = -10

        if(green_apple_y > 500):
            green_apple_x = random.randrange(20,570)
            green_apple_y = -30
            gapple = False

        #RED______APPLE_DETECTION#
        if((apple_x_move - player_x) <= 25 and (apple_x_move - player_x) >= 0):
             if((player_y - apple_y_move) < 0):
                  tt = (player_y - apple_y_move) * -1
             else:
                  tt = player_y - apple_y_move 
             if(tt <= 25 and tt >= 0):
                 apple_x_move = random.choice([10,40,80,120,160,200,240,280,320,360,400,440,480,520,560]) #random.randrange(20,580)
                 apple_y_move = -10
                 red_apple_score += 1
                 eat_sound = pygame.mixer.music.load('sound effect/bite/Bite Sounds _ Free Sound Effects _ Bite Sound Clips _ Sound Bites.wav')
                 eat_sound = pygame.mixer.music.play()

        #GREEN______APPLE_DETECTION#
        if((green_apple_x - player_x) <= 25 and (green_apple_x - player_x) >= 0):
             if((player_y - green_apple_y) < 0):
                  tt = (player_y - green_apple_y) * -1
             else:
                  tt = player_y - green_apple_y 
             if(tt <= 25 and tt >= 0):
                 eat_sound = pygame.mixer.music.load('sound effect/bite/Bite Sounds _ Free Sound Effects _ Bite Sound Clips _ Sound Bites.wav')
                 eat_sound = pygame.mixer.music.play()
                 green_apple_x = random.randrange(20,580)
                 green_apple_y = -30
                 rebuild()
                 
                 if(broken_block == True):
                     message1 = 30
                 else:
                     message6 = 30
                 gapple = False

        #PURPLE______APPLE_DETECTION#
        if((purple_apple_x - player_x) <= 15 and (purple_apple_x - player_x) >= 0):
             if((player_y - purple_apple_y) < 0):
                  tt = (player_y - purple_apple_y) * -1
             else:
                  tt = player_y - purple_apple_y 
             if(tt <= 15 and tt >= 0):
                 eat_sound = pygame.mixer.music.load('sound effect/bite/Bite Sounds _ Free Sound Effects _ Bite Sound Clips _ Sound Bites.wav')
                 eat_sound = pygame.mixer.music.play()
                 message3 = 30
                 lives += 1
                 heal_sound = pygame.mixer.music.play()
                 purple_apple_x = random.randrange(20,580)
                 purple_apple_y = -30
                 papple = False
        
        broke_if_near()
        fall_if_not_equal()

        greenapple = random.choice([1,2,3,4,6,7,8,9,10,11,12,13,14,'greenapple'])
        greenapple2 = random.choice([1,2,3,4,6,7,8,9,10,11,12,13,14,'greenapple'])
        greenapple3 = random.choice([1,'greenapple'])

        
        purpleapple = random.choice([1,2,3,4,6,7,8,9,10,11,12,13,14,'purpleapple'])
        purpleapple2 = random.choice([1,2,3,4,6,7,8,9,10,11,12,13,14,'purpleapple'])
        purpleapple3 = random.choice([1,2,3,'purpleapple'])

        if(greenapple == 'greenapple' and greenapple2 == 'greenapple' and greenapple3 == 'greenapple'):
            gapple = True

        if(purpleapple == 'purpleapple' and purpleapple2 == 'purpleapple' and purpleapple3 == 'purpleapple'):
            papple = True
   
        screen.blit(bg, (0,0))
        #block's_blit_1#
        screen.blit(block1pic ,(block_x1,block_y1))
        screen.blit(block2pic ,(block_x2,block_y2))
        screen.blit(block3pic ,(block_x3,block_y3))
        screen.blit(block4pic ,(block_x4,block_y4))
        screen.blit(block5pic ,(block_x5,block_y5))
        #block's_blit_2#
        screen.blit(block6pic ,(block_x6,block_y6))
        screen.blit(block7pic ,(block_x7,block_y7))
        screen.blit(block8pic ,(block_x8,block_y8))
        screen.blit(block9pic ,(block_x9,block_y9))
        screen.blit(block10pic ,(block_x10,block_y10))
        #block's_blit_3#
        screen.blit(block11pic ,(block_x11,block_y11))
        screen.blit(block12pic ,(block_x12,block_y12))
        screen.blit(block13pic ,(block_x13,block_y13))
        screen.blit(block14pic ,(block_x14,block_y14))
        screen.blit(block15pic ,(block_x15,block_y15))
        #########################################
        screen.blit(red_apple, (apple_x_move,apple_y_move))
        screen.blit(green_apple, (green_apple_x,green_apple_y))
        screen.blit(purple_apple, (purple_apple_x,purple_apple_y))
        screen.blit(skin, (player_x, player_y))
        screen.blit(live, (0,0))
        screen.blit(red_apple, (0, 30))
        redapple_message(" = %s"%red_apple_score,black)
        lives_message(" = %s"%lives,black)
        if(message1 > 0):
            message1 -= 1 
            screen.blit(rebuild_soild, (0,80))
        if(message2 > 0):
            message2 -= 1 
            screen.blit(not_enough, (0,50))
        if(message3 > 0):
            message3 -= 1 
            screen.blit(lives_increased, (0,60))
        if(message4 > 0):
            message4 -= 1
            screen.blit(not_enough, (0,50))
        if(message5 > 0):
            message5 -= 1
            screen.blit(fall, (0,70))
        if(message6 > 0):
            message6 -= 1
            screen.blit(no_broken_solid, (0,100))
            
        if(red_apple_score < 25 and n25 == 0):
            n25 += 1
        if(red_apple_score < 50 and n50 == 0):
            n50 += 1
        if(red_apple_score < 75 and n75 == 0):
            n75 += 1
        if(red_apple_score < 100 and n100 == 0):
            n100 += 1
            
        if(n25 > 0):
            if(red_apple_score >= 25):     
                n25 -= 1
                FPS += 1
                n25s = True
        if(n50 > 0):
            if(red_apple_score >= 50):
                n50 -= 1
                FPS += 2
                n50s = True
        if(n75 > 0):
            if(red_apple_score >= 75):
                n75 -= 1
                FPS += 4
                n75s = True
        if(n100 > 0):
            if(red_apple_score >= 100):
                n100 -= 1
                FPS += 6
                n100s = True
        if(n25s == True and red_apple_score < 25):
            FPS -= 1
            n25s = False

        if(n50s == True and red_apple_score < 50):
            FPS -= 2
            n50s = False

        if(n75s == True and red_apple_score < 75):
            FPS -= 4
            n75s = False

        if(n100s == True and red_apple_score < 100):
            FPS -= 6
            n100s = False
        game_speed_message("Game Speed = %s"%FPS,black)
        display.update()
        player_left_x = 0
        player_right_x = 0
        clock.tick(FPS)

gameintro()
gameloop()
gameover()
