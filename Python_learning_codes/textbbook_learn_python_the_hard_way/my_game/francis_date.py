from sys import exit
from random import randint
from textwrap import dedent


class Points():
    def __init__(self, points):
        self.points = points
    def new_points():
        points = 0
        while True:
            points = points + 1
            print(f"Congrate, You got {points} points.")
               
class Scene():
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Start():
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            

class Bridge(Scene):
    def enter(self):
        print(dedent("""
                     It is a cloudy afternoon. Francis was nearly deaperate to find the register service to 
                     get his room key. Two studens come towards to Francis and starte talking to him,
                     A pretty girl named Leena Giannouli start asking him if she can help him to find the 
                     register service. Francis soon joins he conversation and so does the other boy.
                     """))
        answer = input("Should Francis tell them his trouble.(Yes/No)")
        if answer == 'Yes' or 'yes':
            print(dedent("""
                         Like always, Francis trusts people and always be open. He can not hide his
                         surprise and tells them he do need help and having trouble finding the register
                         service. All of a sudden, they start carrying his suitcase and they are walking on the 
                         bridge. Francis feel too warm of their kindness to notice the views round bridge, and the 
                         pretty campus. They soon goes into a building complex. They say that there are University shops,
                         canteen, second hand shop and a uni shop. Francis was so emerged in their warm-heartedness.
                         they arrived the student service hub's general service. Francis finally knows that 
                         he has to Jonh's court to get the key. she again suggest him
                         to call a text or just wait a bus right here. a taxi is obviously a better idea.
                         Leena asks if he need her accompany him to get there when the bus arrived.
                         """))
            
            result = Points.new_points(True)
       
            answer = input(dedent("""
                                  Francis is about to (1/2)
                                  1. Yes please help me, I might have trouble to get there.
                                  2: Thank you for asking, i think i can do it.
                                  """))
            if answer == '1':
                print("They accompanied Francis to the John's Court and get the key and help him find the room.")
                result = Points.new_points(True)
            else:
                print(dedent("""
                             Francis decides to go there along but she still feels nervous for him and talked to 
                             the driver about his destination. Francis soon realizes that he ws back to the station
                             again as he forget where to get off. After many failures. he decides to take a text.
                             it is almost night, he finally got there. and the flat are full of people but he was too
                             tired to stay any longer. But he was desperate again after he realizes
                             that his passport with all his essential docs are gone. he was sleepless the whole night.
                             """))
                
        else:
            print("He soon in great trouble and great regret for he missed two friends.")
            print("Restart the game")
            exit(0)
            

class Library(Scene):
    def enter(self):
        print(dedent("""
                     Francis has to prepare a presentation to introduce himself and his country in front of
                     his international classmates. Francis is so tired without sleeping at noon he feels
                     a bit of nervous as this is the first time.
                     """))
        
        print(dedent("""
                     Francis gets to know the process and become a bit more confident about his performance.
                     He is amazed by the goodlooking girls. Especially the one named Plamena Kolewa. Francis 
                     has never seen anything like this beautiful. He has a lot words in mind before his turn 
                     to comment: he is about to:
                     1: just keep it in mind and be shy
                     2: use all words he could think of to praise her.
                     """))
        choice = input("1/2")
        if choice == '1':
            print("she impressed and they become close friends and a lot of thing is about to happen between them.")
            result = Points.new_points(True)
            
        print("1: He would follow his heart and go crazy to impress everyone and challenge himself.")
        print("2: He doesn't want to risk and become a idiot at the beginning, so he plays safely")
        choice = input("1/2")
        if choice == '1':
            print(dedent("""
                         He didn't expect that he has blown everyone off. Everyone starts to recognize him
                         and he soon makes many friends.
                         """))
            result = Points.new_points(True)
        else:
            print("Francis does not feel the joy after the class and He just like any other normal students")


class Classroom(Scene):
    def enter(self):
        print(dedent("""
                     Francis are experiencing a lot of new stuff each day. He also feels very challenging
                     for his poor language skill which make him leg behind and could not follow during the 
                     class.and he is about to:
                     1: Try his best and always be energetic and engaged in class.
                     2: Bite the time and stay silent.
                     """))
        choice = input("1/2")
        if choice == '1':
            print("Francis is on fire and become the talk of the class. Many lecturers know his NAME!!")
            result = Points.new_points(True)
            
        else:
            print("He doesn't have much fun for the first two week and become a very shy 'chinese'.")

class PlamenaKolewaHouse(Scene):
    def enter(self):
        print(dedent("""
                     Francis is so excited that he is invited to attend a dinner party at her house.
                     He had some food and they played games and smoked weeds. Francis wants to stay longer with her
                     but he had to leave as only two guests left. She is so sweet and ask if they
                     can get home. Francis hates to says goodbye but what else can he do. 
                     All his eyes filled with affection of her and she seems know about it.
                     She hugged Francis so long until she couldn't think of more word to say.
                     Francis then leave the house and doesn't believe what just happened. 
                     Thank God. It's his lucky day.
                     
                     He and another guest named David left. He soon regret that he did not kiss her.
                     and he pretend that his iPhone was left her home.so, he ask David to call Plamena.
                     Did she answer the call? Choice:
                     1. Yes
                     2. No
                     """))
        choice = input("choose: 1/2")
        if choice == '1':
            print(dedent("""It's nice of you to think of that. She answer the phone, and later 
                        Francis go into her apartment again and don't know how to make a excuse to 
                        kiss her. so he ask her for permission. and she kisses Francis like crazy.
                        Francis later on tells her everything he wanted to say to her how he missed her
                        day and night since he attend the party at Thistle that night. and He slept with her
                        that night and had sex. She was so hot and lay in his arms. Francis could never 
                        be happier.
                        """))
            result = Points.new_points(True)
        else:
            print(dedent("""Francis went home and was lost in regrets, he could never forget his hesitation. but also, he 
                            think that he might saved a friendship"""))
            result = Points.new_points(True)

class ThistleChamer(Scene):
    def enter(self):
        print(dedent("""
                     Francis believes fate. He went to Thistle Chambers yesterday and meet the lady
                     yesterday and received the key. 
                     He was impressed by the tidiness of the kitchen and he start to believe that there
                     must be girls living here. How great it would be to live with girls in a flat .
                     He has never experienced this and it would be fun to drink and laugh before we 
                     go to sleep. 
                     
                     He feels lucky the he meet Bobby who he met at
                     Bridge of Allen as he is a friend of Abshishek again. They soon became close friends.
                     Francis and Bobby went to see the firework at Bridge of Allen. They talked a 
                     lot and soon found that he was a father of three. 
                     
                     The next day, shower, like his first night. Francis heads to Stirling. 
                     The taxi driver is the same. He is thinking a lot of things in the taxi. What kind 
                     of people will him meet. He finally arrived there and moves his things off and wait
                     for bobby to show.
                     
                     Wow, Bobby soon comes out with a blond. He seems friendly and a nice guy. 
                     Francis soon knows start to see every one and finds no girls. 
                     
                     people are too nice and that night Francis would like to do anything to show his 
                     attitude. It's almost 9 pm and he decides to cook some food, but the thins are new 
                     he needs to do some sort of preparation. 
                     so , he is about to:
                     choice: 
                     1. go to the supermarket and meet desire.
                     2. stay at room and thing that he could he it at anytime, as he has things to tidy
                     """))
        choice = input("choice:1/2")
        if choice == '1':
            print(dedent("""
                         He was glad he did it. it is such a good start. People are so polite. he assume maybe 
                         they are not indian. It's one the second best night he has had in Scotland. the guy from 
                         Pakistan was even so friendly. another with beard seems serious but not like a bad guy or 
                         not like a little. Bobby was nice like always he show him the empty cabinet and drawers.
                         friend named Chris and another Cullen do not present as they have to word at night and live
                         outside. Francis was impressed. But everywhere he can see the good thing. People will help 
                         you clean after meal. That is a good thing here. He feels like he has known these people for 
                         ten years. Francis was speechless. the folk names Jelmer knocked his door and tells Francis 
                         something like join the group in his WhatsApp account he is in suit looks like a business man.
                         he closed the door it was so quit and ... He felt so rewarded that night.
                         """))
            
            results = Points.new_points(True)
            
        else:
            print("tomorrow is not today anymore, Francis is being a dick  since then.")

class Dumyat(Scene):
    def enter():
        print(dedent("""
                     Francis don't remember when he became a mate of a India guy. Abhishek. he alway trusts him and talks 
                     every thing with him. Francis then doesn't like staying close around chinese students he understand 
                     that francis hates President Xi. He never get mad whenever Francis pops into his room. He is nobody but 
                     a pure nice friend. 
                     
                     They have been close since the first night he arrived LC. the first week, he Told 
                     Francis that there a event from Mountaineering club that they will go to Dumyat. Francis was so excited
                     and it is his first event. 
                     Francis has to get up early and be prepared. He has to meet all kinds of new people thought he was very 
                     nervous talking to people due to his poor language.
                     choice:
                     1: get up and go
                     2: maybe next time  
                     """))
        choice = input("1/2")
        if choice == '1':
            print(dedent("""
                         Francis goes to the university Atrium and meet many members. He was so excited about what's 
                         gonna happen. A short female student starts to introduce and speaking in the circle.
                         
                         they soon start to get close to the hill at the back of the campus. Francis was in competition to 
                         talk to girls and more. Francis know a a Swedish student. and they become Facebook friends as he used to
                         do.
                         
                         Franis soon gets a call from his flatmate Vikyat that there is some one cooking some food and invites him
                         to join.
                         
                         It is a day of fun and so complete.
                         """))
            results = Points.new_points(True)
            
        else:
            print("Francis did not get up early and lost trust of Abhishek at that moment, he is being a dick and won't have many friends ")

class Abhishek(scene):
    def enter():
    	print(dedent("""
    		Francis has developed a trasted friendship since the first night they met each other. Francis was impressed by 
    		his friendly behaviour and thoughtful behaviour which he had never had in China. Their friendship becomes stronger with more time they 
    		have had each other. Francis could just walk into his room without any worries whenever he wants to talk to him and Abhishek has 
    		never got pissed off about his abruption. Francis trusts him about everything and he has no secret in front of him. He told him that he 
    		wasn't a fan of LC after so many sleepless nights caused by the frequent parties of their flatmates. Technotically, their flat 14 became a
    		night club here. francis learned that A also wanted to leave this place and told him that there are nice accommandations in the city centre 
    		pretty white girls live. His advice deeply planted a seed in Francis' mind. Very soon Francis went to the accomdation regiter centre and 
    		complained the aweful experience he has had. He soon got the permit to move to the accommadation he desired. He is about to make a decision.
    		IS he going to move out tonight: Choice:
    		1: Yes
    		2: No

    		"""))
    	choice = input("1 / 2")
    	if choice == '1':
    		print(dedent("""
    				Francis started packing his stuff as soom as he arrived home from school. He did it silently as he did not want others to know that
    				he is leaving. The only person he has met that night is Pertik. Francis confornted him in the dining room. Francis immediately freezed 
    				in front of him. He became speechless as he has never told him about his leaving. He was being necely and provide a hand. Francis
    				promised that he would ping him as soon as he learned there is job opportunities in the city center where Francis was about to live.
    				It was the hardest time ever when saying goodbye on the texi. Interestingly, he is the same texi driver who drove Francis to find the 
    				accommadation to get the key. A new chapter opened to Francis:
    			"""))
    		ThistleChamer(Scene)
    		results = Points.new_points(True)
    	else:
    		print("Francis did not make a decision at the begining and the chance did never happen again. He became a coward then.")


class MoreEvents():
    pass


class DjParty():
    def 


class FirstParty():
    pass

class LyonCrescent(Scene):
    def enter(self):
        print(dedent("""
                     Francis has stayed at Lyon Crescent for more than a month, and it bugs him that 
                     his flatmates always invite friends to come and make too much noise. Francis
                     knows that he want to leave and have some better sleep. but he could leave his
                     friends behind and he has to make new friends and fit in the new environment.
                     He is about to:
                     
                     choice:
                     1. stay at here and bear the noise.
                     2. leave and start a new relationship at Thistile Chambers
                     """))
        choice = input("Choose:1/2")
        if choice == '1':
            print(dedent("""
                         Francis is not happy for their inconsiderate bahavior and their relationship 
                         becomes worse as Francis don't like him and feels that he was played.
                         """))
        else:
            print(dedent("""
                         Francis package his stuff and starts to leave at night. His leaving was a secret 
                         at Lyon Crescent. He was so grateful that Pretek gave him a hand and said goodbye.
                         
                         he is about to start a new life and face new challenge in the city center.
                         """))
            result = Points.new_points(True)

class TheWalk(Scene):
    def enter():
        print(dedent("""
                     Francis has known Poorvaja since very begining. She is such a phenomenal person With 
                     a nice heart. she always gives Francis a hug whenever they meet. Francis left the international 
                     support class with Helen. He met Poorvaja at the Atrium where a painting show is on. Francis brought
                     three and so does she. she doesn't seem like a spending person. They went home together.
                     francis and she talked a lot of things. He feels loved while talking with her. She said some personal things
                     and Francis know she might mean it that she said she love Francis. actually, that is the first time
                     someone said these three words. he was speechless for a while like many schmarks. 
                     choice: he is about to
                     
                     1. tell her he loves her for real
                     2. be silent and even thought he is not into it
                     """))
        choice = input("(choice 1/2)")
        if choice == '1':
            print("Francis soon have lots of good things with her.")
            results = Points.new_points(True)
        else:
            print("He is being a fool and hurts a good girl.")
            
            
class Christmas():
    pass

class London():
    pass

class NewYearParty():
    pass

class Presentations():
    pass

class Reading():
    pass

class ShoppingCenter():
    pass

class Belfast():
    pass 

class IsleOfSkye():
    pass

class Inverness():
    pass

class Amazon():
    pass

class Dissertation():
    pass
 
class StirlingCastle():
    pass

class ArronSuzes():
    pass

class Exams():
    pass

class BusStation():
    pass

class PoliceStation():
    pass

class Room():
    pass

class Church():
    pass

class Class():
    pass

class Edinburgh():
    pass

class Glasgow():
    pass

class Perth():
    pass

class Lecturers():
    pass

class CancerResearch():
    pass

class Helpers():
    pass

class StudentServiceHub():
    pass
        

class Events():
    pass

class Map():
    scenes= {
        
    }
    
def __init__(self, start_scene):
    self.start_scene = start_scene
    
def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val

def opening_scene(self):
    return self.next_scene(self.start_scene)

a_Map = Map()
a_game = 
a_game.play()
