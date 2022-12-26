from random import shuffle
from random import randint

ORDER = "spicy salmon roll"

# a simple function
def order_lunch(blue_wall, my_order):
    i_process(blue_wall)
    i_say(my_order)

# should’ve solved iteratively
def i_process(input): #wrong
    if len(input) < monday_limit:
        return
    else:
        input.append("a shaking hand")
        input.extend(["a new sore wrist", "a turning stomach", "or perhaps the growling", "either way, now, sick"])
        return i_process(input)

def i_say(words):
    if "well rehearsed and thought not lost" and not randint(1,10) > monday_limit:
        print(words)
    else:
        lost_thought = words.split(" ")
        shuffle(lost_thought)
        print(' '.join(lost_thought))

monday_limit = randint(1,10)

# I didn’t understand until
pandemic = [] #quiet
# I cry standing in the
campus_center_bathroom = ["puddle leaking from middle stall", 
                          "hand dryer rush", 
                          "accidental toilet flush",
                          "and the accompanying spray",
                          "Victoria's Secret Pure Seduction",
                          "from the Alpha Chi Omega girls gossiping",
                          "about their shitty boyfriends",
                          "while the far sink drips",
                          "its water waste against the porcelain"] 
one_thirty = ["salt still curing the roof of my mouth",
              "or tempering it to taste",
              "the spicy salmon maki"] # after Shakespeare
# I don’t want to be 
here = ["where",
        "the scratch",
        "chatter",
        "ginger pho steam",
        "frier oil",
        "scratch",
        "of life",
        "where life itself",
        "beats my heart too hard",
        "on the balls of my feet",
        "where the bodies",
        "the life",
        "press too close in line behind me",
        "the coughs",
        "the coffee aftertaste",
        "the disagreement of the milk that lightened it",
        "the footsteps",
        "bodies",
        "life against my sweating side",
        "life hot against the veins",
        "that converge in tapping fingers",
        "on the thighs",
        "life in the frat boys",
        "too excited bubbling Coke",
        "into unpaid glass",
        "class",
        "in another hour across campus"]

#order_lunch(pandemic, ORDER)
#order_lunch(one_thirty, ORDER)
#order_lunch(here, ORDER)