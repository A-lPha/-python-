﻿from sys import exit

q = "*" * 20

def start():
    print "You are in a dark room.\n"
    print "There is a door to your right and left.\n"
    print "Which one do you take?\n"
    print q,"\n"
    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def bear_room():
    print "There is a bear here.\n"
    print "The bear has a bunch of honey.\n"
    print "The fat bear is in front of another door.\n"
    print "How are you going to move the bear?\n"
    print q, "\n"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.\n")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now.\n"
            bear_moved = True
        elif next == "taunt bear" and  bear_moved:
            dead("The bear gets pissed off and chews your leg off.\n")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means.\n"

def cthulhu_room():
    print "Here you see the great evil Cthulhu.\n"
    print "He, it, whatever stares at you and you go insane.\n"
    print "Do you flee for your life or eat your head?\n"
    print q,"\n"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!\n")
    else:
        cthulhu_room()

def gold_room():
    print "This room is full of gold. How much do you take?\n"

    next = raw_input("> ")

    if "0" in next or "1" in next: #暂时解决不了，用其他方式判断是否输入的是数字
        how_much = int(next)
    else:
        dead("Man, learn to type a number.\n")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!\n"
        exit(0)
    else:
        dead("You greedy bastard!\n")
        
def dead(why):
    print why, "\nGood job!\n"
    exit(0)
        
start()
