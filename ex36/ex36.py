#!/usr/bin/python
# vim: et:sts=4:sw=4


from sys import exit

def dogs_eat_you():
    print "You open a door and walk into a room. The door closes behind you."
    print "You see many yellow eyes and hear snarling. You are eaten by the"
    print "monestary watch dogs."
    print ""
    dead ("Awesome!")

def fall_in_pit():
    print "The deaf monk looks offended. He steps back and points to the left."
    print "You walk down a pitch black tunnel. Suddenly, you are falling, and"
    print "you land in a slimy goo with many skeletons around you. It turns out"
    print "That you are in a pit with man-eating worms. As you are being eaten"
    print "alive, your last thought is..."
    print ""
    print 'Saying "The mute mean misboden monk masticates" ten times fast would be hard.'
    print ""
    dead ("Epic fail!")

def deaf_monk():
    print "A monk greets you in the tunnel. You try to talk to him, and he"
    print "signs to you. Finally, you realize he is deaf. Also, you realize"
    print "that he is standing at a tee, with a tunnel going left and a"
    print "tunnel going right. You have to ask him a yes/no question to"
    print "solve the murder."
    print ""
    print "What do you ask?"

    while True:
        next = raw_input("> ")

        if next == "clue":
            print "Some detective you are. On the wall next to you is a sign"
            print "that shows you the possible questions:"
            print ""
            print "Did you kill Fro?"
            print "You?"
            print "Can you tell me who killed Fro?"
            print "Who?"
            continue
        elif next == "Did you kill Fro?":
            fall_in_pit()
        elif next == "You?":
            fall_in_pit()
        elif next == "Can you tell me who killed Fro?":
            go_to_fork()
        elif next == "Who?":
            go_to_fork()
        else:
            print "The monk whistles loudly and the monestary griffin grabs"
            print "you, carries you to her eyrie and feeds you to her children."
            print ""
            dead ("Nice.")

def go_to_fork():
    print "Without expression the deaf monk holds up a sign that points right"
    print 'with the words, "Go to Guru." You walk down the tunnel and you come to'
    print "a fork in the road. What do you do?"
    print ""

    while True:
        next = raw_input("> ")

        if next == "go left":
            go_to_guru()
        elif next == "go right":
            sirens_get_you()
        elif next == "clue":
            print 'Really? "go left" or "go right". Sheesh!'
            next = ""
            continue
        else:
            dead("You are shot as an intruder by the monestary NRA rep.")

def go_to_guru():
    print "You walk down a tunnel, and come to another tee. There, sitting"
    print "cross-legged, is guru. He has long hear, is wearing hippy-beads"
    print "and sun glasses, and has a peace sign tatooed into his forehead."
    print ""
    print "What do you ask?"

    while True:
        next = raw_input("> ")

        if next == "clue":
            print "Some detective you are. His tee shirt has writing that"
            print "that shows you the possible questions:"
            print ""
            print "Did you kill Fro?"
            print "You?"
            print "Can you tell me who killed Fro?"
            print "Who?"
            continue
        elif next == "Did you kill Fro?":
            death_by_bats()
        elif next == "You?":
            death_by_bats()
        elif next == "Can you tell me who killed Fro?":
            solve_case()
        elif next == "Who?":
            solve_case()
        else:
            print "The monk whistles loudly and the monestary griffin grabs"
            print "you, carries you to her eyrie and feeds you to her children."
            dead ("Nice.")


def death_by_bats():
    print "You walk down a dark tunnel. You smell something, and just as you"
    print "recognize the smell as bat guano, a giant bat bites your head off"
    print "and feeds your brain to her babies."
    print ""
    dead ("Wow!")

def sirens_get_you():
    print "You walk down the tunnel and hear beautiful music. You can't stop"
    print "yourself. Entranced, you run... into the cave of the sirens."
    print "They stop singing and eat you."
    print ""
    dead("Powerful Jedi are you...NOT!")

def solve_case():
    print "You traverse down a dark tunnel that loops to the right. Finally,"
    print "you come out of a hidden cave entrance, and you are in front of the"
    print "monestary again. As you look down at Fro and think what a bazaar"
    print "hair style he has, you notice a piece of paper under his afro."
    print "Remembering guru's words, you know what the paper is even before"
    print 'you read "Goodbye cruel world...".'
    print ""
    print "Contgratulations! You have solved the case."
    exit (0)

def dead(why):
    print why, "Great deduction, Sherlock!"
    exit(0)

def start():
    print "Your name is Hercules Parrot. You are a famous detective. There"
    print "has been a murder reported at the corner monestary, and you are"
    print "sent there to solve the case. When you arrive, you find Fro lying"
    print "on the doorstep with a long knife in his chest. He is called"
    print "Fro because he has a big purple afro. There are bloody footsteps"
    print "leading to the door of the monestary, and you follow them and"
    print "enter the monestary."
    print ""
    print "The bloody footsteps end as soon as you step into the monestary."
    print "Before you is a fork. One tunnel goes left, one goes right."
    print ""
    print "What will you do?"
    print '(Type the word "clue" to get suggestions at any juncture.)'

    while True:
        next = raw_input("> ")

        if next == "go left":
            dogs_eat_you()
        elif next == "go right":
            deaf_monk()
        elif next == "clue":
            print 'Really? "go left" or "go right". Sheesh!'
            next = ""
            continue
        else:
            dead("You are shot as an intruder by the monestary NRA rep.")


start()


