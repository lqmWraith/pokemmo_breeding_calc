#LqmWraith's Breeding Calculator

#~~~~~DEPENDENCIES~~~~~
import os
import time
#for list sort
import operator

#global to lazily pass between functions
poke_list = []

#~~~~~POKEMON CLASS INSTANCE~~~~~
class Pokemon():
    def __init__(self, name, box_position, nature, hp, attack, defense, special_attack, special_defense, speed, score):
        self.name = name
        self.pos = box_position
        self.nat = nature
        self.hp = hp
        self.atk = attack
        self.dfn = defense
        self.spatk = special_attack
        self.spdef = special_defense
        self.spd = speed
        self.score = score

#~~~~~COMMAND LINE POKEMON CREATON FUNCTION~~~~~
def make_poke():
    #references poke_list out of scope
    global poke_list
    print "Don\'t break this! No error handling\n"
    #runs determines number of pokemon
    runs = int(raw_input("How many pokemon do you have?:  "))
    #used to realize when user has entered enough pokemon
    counter = 0
    #the following could be for (i > runs), i++:
    while counter < runs:
        #get stats int() converts to integer, str() to string.
        #raw_input() for python2.x, use input() for 3.x +
        #temp variables, for garbage collection
        temp_pos = int(raw_input("Enter a position for the pokemon in a box:  "))
        temp_nature = int(raw_input("Enter a Nature (1-25):  "))
        temp_hp = int(raw_input("Enter pokemon\'s HP IV:  "))
        temp_atk = int(raw_input("Enter pokemon\'s Attack IV:  "))
        temp_dfn = int(raw_input("Enter pokemon\'s Defense IV:  "))
        temp_spatk = int(raw_input("Enter pokemon\'s Sp Attack IV:  "))
        temp_spdef = int(raw_input("Enter pokemon\'s Sp Defense IV:  "))
        temp_spd = int(raw_input("Enter pokemon\'s Speed IV:  "))
        temp_name = str(raw_input("Enter a Unique Name:  "))
        #placeholder for next function
        score = 0
        #create instances
        temp_name = Pokemon(temp_name, temp_pos, temp_nature, temp_hp, temp_atk, temp_dfn, temp_spatk, temp_spdef, temp_spd, score)
        #this is probably a bad way to do it
        poke_list.append(temp_name)
        print "\n"
        counter += 1

#~~~~~APPLY SCORE~~~~~
def score_poke():
    #apply score to object based on number of perfect iv values
    global poke_list
    for i in poke_list:
        if i.hp == 31:
            i.score += 1
        if i.atk == 31:
            i.score += 1
        if i.dfn == 31:
            i.score += 1
        if i.spatk == 31:
            i.score += 1
        if i.spdef == 31:
            i.score += 1
        if i.spd == 31:
            i.score += 1
        #print i.score

#~~~~~SORT LIST, DO YOU NEED AN EXPLANATION?~~~~~
def sort_list():
    global poke_list
    #poke_list sorted by descending value based on score attribute that was changed by score_poke function
    poke_list = sorted(poke_list, key=operator.attrgetter('score'), reverse=True)
    print "Pokemon have been sorted based on number of IV\'s. Use the highest pokemon on the list for your base pokemon\n"
    for i in poke_list:
        print "Name     :  ", i.name, "\nBox Pos  :  ", i.pos, "\nScore    :  ", i.score, "\n"

#~~~~~THE NEXT THING TO DO~~~~~
def breed_path():
    #calculate 1st breed, next breed, maybe hypotheticals. not sure how deep this one will go yet.
    pass

#~~~~~ALSO THE NEXT THING TO DO~~~~~
def choose_preferences():
    #this function will allow the user to target what is important to them. ie, nature=adamant(1), hp, def, spdef (3x31)
    #this in combination with breed_path() is next
    pass

#~~~~~SAVE CURRENT POKEMON~~~~~
def save_list():
    #save list to file or db
    global poke_list
    pass

#~~~~~LOAD LIST FROM FILE~~~~~
def load_list():
    #import poke_list from file
    pass

#~~~~~~~~~~~~~~
#~~~~~MAIN~~~~~
#~~~~~~~~~~~~~~
def main():
    make_poke()
    score_poke()
    sort_list()
    time.sleep(5)
    quit()
    #last 2 are just autoquit for testing
main()
