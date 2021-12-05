from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead("man, learn to type a number.")
        
    if how_much < 50:
        print("Nice, you are not greedy, you win!")
        exit(0)
    else:
        dead("you greedy bastard.")
    
def bear_room():
    print("there is a bear here.")
    print("The bear has a bunch a honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear.")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice =="take honey":
            dead("The bear looks at you then slaps your face...")
        elif choice == "taunt bear" and not bear_moved:
            print("You can go through it now.")
            bear_moved = True
            
        elif choice == "taunt bear" and bear_moved:
            dead("the bear get pissed off you and chews your bones...")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got not idea what that means...") 
            
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane..")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well, that was tasty!")
    else:
        cthulhu_room()
        
def dead(why):
    print(why, "good, job!")
    exit(0)
    
def start():
    print("You are in dark room..")
    print("There is a door to your right and left.")
    print("which one do you take?")
    
    choice = input ("> ")
    if choice == "left":
        bear_room()
    elif choice == "left":
        cthulhu_room()
    else:
        dead("You stumble around and the room until you starve to death...")
        
start()