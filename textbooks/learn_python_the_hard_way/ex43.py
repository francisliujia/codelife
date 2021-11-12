from sys import exit
from random import randint
from textwrap import dedent

class Scene:
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map
    

    def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene("finished")
            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)
                
                # be sure to print out the last scene
                current_scene.enter()
                
class Death(Scene):  
    quips = [
        "You dies. You kinda suck at this.",
        "Your Mom would be proud of you if she were smarter. ",
        "I have a small puppy that's better at this. ",
        "You're worse than your Dad's jokes."
    ]
    def enter(self):
            print(Death.quips[randint(0, len(self.quips)-1)])
            exit(1)

class CenterCorridor(Scene):
    def enter(self):
        print(dedent("""
                    The Gothon of Planet Percal #25 have a invaded
                    destroyed your entire crew. You are last number and you
                    last mission is to get nuclear bomb from the Weapon
                    armory, put it in the bridge and blow the ship up after
                    geting into a escape capsue.
                    
                    You're running down teh central corridor to the 
                    Armory when a Gothon jumps put, red scaly skin
                    filled with evil clown costume flowing around, his filled 
                    body. He's blocking the door to the Arm and is about to 
                    pull a weapon to blast your dick off.
                    """)) 
        action = input("> ")
        if action == "shoot!":
            print(dedent("""
                        Quick on the draw you yank out your blast it at the
                        Gothon. His clown costum is flowing around his body,
                        which throws off you, your laser hits his costume but
                        misses him. This completely ruins his brand new costum
                        his mom brought him, which makes him fly into an and blast 
                        you repeatedly in the face until dead. Then he eats your 
                        penis. 
                        """))
            return 'death'
        elif action == 'dodge!':
            print(dedent("""
                        Like a world class boxer you dodge, weave, slide right
                        as the Gothon's blaster cranks past your head. In the middle of your
                        art, your foot slips and you bang your head on wall
                        and pass out. You wake up shortly after a while. You die as the 
                        Gothon stomps on your penis and chews is off.
                        """))
            return 'death'
            
        elif action =="tell a joke":
            print(dedent("""
                         Lucky for you they made yu learn Gothon i 
                         the academy. You tell the one Gothon joke Lhn zb
                         gure gn nheu n, ubher fur. The Gothon stop not to 
                         laugh, then busts out laughing and while he's laughing
                         you run up and shoot his at his back, then jump through 
                         the weapon armory door.
                         """))
            return "laser_weapon_armory"
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
        
class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                     You do a dive roll into the Weapon Armory, cry the room for
                     more Gothons that might be hiding quit, too quiet. You stand up,
                     and run to the room and find the neutron bomb in its con, there is a 
                     keypad lock on the box and you need to get the bomb out, if you get the 
                     code wrong the lock closes forever and you can't get the code in 3 
                     digits.
                     """))
        code = f"{randint(1, 9)} {randint(1, 9)} {randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print("BUZZZZEEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
            
        if guess == code:
            print(dedent("""
                         The container clicks open and seal bring the gas out
                         you grab th neutron bomb adn run. you come to the bridge where you 
                         must ignite the bomb.
                         """))
            return 'the_bridge'
        
        else:
            print(dedent("""
                         The lock buzzes one last time and then you sicking melting sound
                         as the mechanism together, you decide to sit there, and Gothon blows
                         up the ship for their ship
                         """))
            return 'death'
            
        
class TheBridge(Scene):
    def enter(self):
        print(dedent("""
                     You burst into the bridge with the netron under your arm and surprised 
                     5 Gothons who are taking control the ship. Each of them has an clown 
                     costum than the last. They haven't pull weapons out yet. as they see the
                     active bomb arm and don't want to set it off.
                     """))
        action = input("> ")
        if action == 'throw the bomb':
            print(dedent("""
                         In a panic you throw the bomb at the ground and make a leap
                         for the door. right as you Gothon shoot you right in the back kill
                         you die you see another Gothon frantically disarm the bomb. you 
                         die knowing they will blow up when it goes off.
                         """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
                         You point your blaster at the bomb under the Gothens but their
                         hands up and start. you inch backward to the door, open it, a 
                         carefully place the bomb on the floor, punch the close button and 
                         blast the bomb you run to the escape pod to get off this.
                         """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return "the_bridge"
    
class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                     You rush through the ship desperately trying teh escape pod before the 
                     whole ship explodes, like hardly any Gothond are on the ship , so you clear
                     of interference. get to the chamber escape pads, and now need to pick one
                     them could be damaged but you don't have time to figure out.
                     There are five pods, which one do you take.
                     """))
        good_pod = randint(1, 5)
        guess = input("[pod #]> ")
        
        if int(guess) != good_pod:
            print(dedent("""
                         You jump into pod {guess} and hit the . the pod escapes put into
                         the void of space implodes as the hull ruptures, crushing you jelly jam. 
                         """))
            return 'death'
        else:
            print(dedent("""
                         The pod easily slides into the space head teh  planet below, as it 
                         flies to the planet, back and see your ship implode then explores as bright as a star
                          taking out teh Gothons ships a time. You won!
                         """))
            return "finished"
        
class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'
        
        
class Map(object):
    scenes = {
        'central_corridor': CenterCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()