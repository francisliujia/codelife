from  sys import exit

def gay_room():
    print("Welcome to the gay room, you little turtle. ")
    choice = input(" are you going to continue?(1:yes/ 2:no)")
    if choice == '1':
        print("You are turning into a cute 18-year-old little virgin girl.")
        input("you are fucked to death and lost your virginity.")
    elif choice == '2':
        print("man, let's do some anus fuck practice.")
    else:
        print("you fucking bastard, masturbate, tiny penis. ")
        exit(0)
        
def lesbian_room():
    print(f"Welcome to my bed, {your_name()}little boy.")
    choice = input("""What are you going to do with me tonight?
                   (1: lick my vagina, 2: fuck my vagina 3: fuck my buttom
                   4: kiss my whole body)/(1,2,3,4)""")
    if choice == '1':
        print("Please be gentle, my pussy is so wet and tight, i just had period www...")
    elif choice == '2':
        print("Your dick is so big, please put it in now, i can't stand any longer...")
    else:
        print("you go fuck yourself.")
        girl_friend()
        
def girl_friend():
    print(f"your girl seems very angry after you found her secret!")
    print(f"What are you doing here.")
    choice = input("1:I want to fuck you, 2: i miss you babe/ (1/2)")
    if choice == '1':
        print("fuck you now, let me blow you peepee")
    elif choice == '2':
        print("I miss you too")
    else:
        print(" I love you Francis, don't forget me i am your Plamena Kolewa")
        lesbian_room()
               
def your_name():
    name = input("what is your name:")
    print(name)
    
def start():
    print("You are going to enter the red zone.")
    print("Please and mind your seeing and choice carefully.")
    print("Good luck and have fun!")
    your_name()
    
    choice = input("Which button would you like to press: 1: red, 2: blue, 3: yellow")
    if choice == '1':
        gay_room()
    elif choice == '2':
        lesbian_room()
    elif choice == '3':
        girl_friend()
    else:
        print("Fuck your pussy, what are you doing?")
        input("Do you want to restart?(1:yes/2:no)")
        if choice == '1':
            print("You made the right choice chicken lol, have fun!")
            start()
        elif choice == '2':
            print("Fuck you You have got not choice haha...")
            start()
        else:
            print("Don't try to fool me, you fool, just do it haha!! ")
            start()
start()
        