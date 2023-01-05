import RPi.GPIO as GPIO
from gpiozero import Button, LED
from time import sleep
import random
import time

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    
    if sec < 60 and mins < 1:
        print("Pressed in {} sec(s)" .format(round(sec, 2)))
    
    elif 0 < mins < 60:
        print("Pressed in {0} min(s): {1} sec(s)" .format(int(mins), round(sec, 2)))
    
    else:
        print("Pressed in {0} hr(s): {1} min(s): {2} sec(s)" .format(int(hours,), int(mins), round(sec, 2)))
    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

player_1 = Button(27)
player_2 = Button(18)

def Trueness():
    global bool
    bool = True

def Fake_news():
    global bool
    bool = False
    
Ready_to_play = 1
player_1_wins = 0
player_2_wins = 0
Foul = 0 
Trueness()

while bool == True:
    GPIO.output(17,GPIO.HIGH)
    print("Player 1 (Yellow button). Are you ready?")
    player_1.wait_for_press()
    player_1.wait_for_release()
    print("Player 1: OK")
    sleep(0.5)
    print("Player 2 (Black button). Are you ready?")
    player_2.wait_for_press()
    player_2.wait_for_release()
    print("Player 2: OK")
    sleep(0.5)
    print("We are ready to start.")
    sleep(1)
    print("Press your button as soon as you see the blue LED turn on.")
    time_r = random.uniform(6, 12)
    sleep(time_r)
    if not player_1.is_pressed and not player_2.is_pressed:
        Foul = 0
    if player_1.is_pressed:
        Foul = 1
    if player_2.is_pressed:
        Foul = 2
    if player_1.is_pressed and player_2.is_pressed:
        Foul = 3
    
    GPIO.output(17,GPIO.LOW)
    start_time = time.time()
    
    while True and Foul == 0:
        
        if player_1.is_pressed:
            print("Player 1 wins!")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            player_1_wins = player_1_wins + 1
            break
    
        if player_2.is_pressed:
            print("Player 2 wins!")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            player_2_wins = player_2_wins + 1
            break
        
    while True and Foul > 0:
        
        if Foul == 1:
            print(" ")
            print("Foul from Player 1 for holding the button down.")
            player_1_wins = player_1_wins - 1
            player_2_wins = player_2_wins + 1
            break
    
        if Foul == 2:
            print(" ")
            print("Foul from Player 2 for holding the button down.")
            player_2_wins = player_2_wins - 1
            player_1_wins = player_1_wins + 1
            break
        
        if Foul == 3:
            print(" ")
            print("Foul from both players for holding the button down.")
            player_1_wins = player_1_wins - 1
            player_2_wins = player_2_wins - 1
            break
       
    GPIO.output(17, GPIO.HIGH)
    sleep(1)
    print(" ")
    print("Score:      P1:{0}       P2:{1}" .format(player_1_wins, player_2_wins))
    sleep(1)
    print(" ")
    
    while player_1.is_pressed or player_2.is_pressed:
        if player_1.is_pressed:
            print("Please release the button Player 1.")
            player_1.wait_for_release()
            player_2.wait_for_release()
            break
        if player_2.is_pressed:
            print("Please release the button Player 2.")
            player_2.wait_for_release()
            player_1.wait_for_release()
            break
    
    print(" ")
    sleep(2)
    

 