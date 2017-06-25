#LqmWraith's Breeding Calculator

#list/array whatever it is in python
poke_list = []


#make a pokemon class object
class Pokemon():
    def __init__(self, box_position, nature, hp, attack, defense, special_attack, special_defense, speed):
        self.pos = box_position
        self.nat = nature
        self.hp = hp
        self.atk = attack
        self.dfn = defense
        self.spatk = special_attack
        self.spdef = special_defense
        self.spd = speed

#example of a pokemon
#pass arguments right to pokemon class

#pokemon1 = Pokemon(0,1,31,31,31,31,31,31)
#print pokemon1.pos, pokemon1.nat, pokemon1.hp, pokemon1.atk, pokemon1.dfn, pokemon1.spatk, pokemon1.spdef, pokemon1.spd

def make_poke():
    global poke_list
    #this would probably be split between field entry and a submit button function
    #temp_stats will be used as arguments for class object creation
    print "Don\'t break this! No error handling\n"
    #runs determines number of pokemon
    runs = int(raw_input("How many pokemon do you have?:  "))
    counter = 0
    while counter < runs:
        temp_pos = int(raw_input("Enter a position for the pokemon in a box:  "))
        temp_nature = int(raw_input("Enter a Nature (1-25):  "))
        temp_hp = int(raw_input("Enter pokemon\'s HP IV:  "))
        temp_atk = int(raw_input("Enter pokemon\'s Attack IV:  "))
        temp_dfn = int(raw_input("Enter pokemon\'s Defense IV:  "))
        temp_spatk = int(raw_input("Enter pokemon\'s Sp Attack IV:  "))
        temp_spdef = int(raw_input("Enter pokemon\'s Sp Defense IV:  "))
        temp_spd = int(raw_input("Enter pokemon\'s Speed IV:  "))
        temp_name = raw_input("Enter a Unique Name:  ")
        temp_name = Pokemon(temp_pos, temp_nature, temp_hp, temp_atk, temp_dfn, temp_spatk, temp_spdef, temp_spd)
        poke_list.append(temp_name)
        print "\n"
        counter += 1

def main():
    make_poke()
    for i in poke_list:
        print i, i.pos, i.nat, i.hp, i.atk, i.dfn, i.spatk, i.spdef, i.spd, "\n"

main()

