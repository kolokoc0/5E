import json

with open ('effectiveness_new.json') as file:
    effects = json.load(file)

# def calculator(number1,number2,listpok):
#     duo_list = []
#     cumTypeAdv = 0
#     result = 1
#     listpok = listpok.split(",")
#     pokemons1 = listpok[0:number1:]
#     pokemons2 = listpok[number1:number2+1+1:]
#     for attack in pokemons1:
#         attack = attack.split(" ")
#         for defense in pokemons2:
#             defense = defense.split(" ")
#             if len(attack) ==2 and len(defense) ==1:
#                 for type_attack in attack:
#                     for type_defense in defense:
#                         duo_list.append(effects[type_attack][type_defense])
#                 cumTypeAdv += max(duo_list)
#                 duo_list = [ ]
#             elif len(attack) ==2 and len(defense) ==2:
#                 for type_attack in attack:
#                     for type_defense in defense:
#                         duo_list.append(effects[type_attack][type_defense])
#                 cumTypeAdv += max(duo_list)
#                 duo_list = [ ]
#             elif len(attack) ==1 and len(defense)==1:
#                 for type_attack in attack:
#                     for type_defense in defense:
#                         duo_list.append(effects[type_attack][type_defense])
#                 cumTypeAdv += duo_list[0]
#                 duo_list = [ ]
#             elif len(attack) ==1 and len(defense) ==2:
#                 for type_attack in attack:
#                     for type_defense in defense:
#                         duo_list.append(effects[type_attack][type_defense])
#                 for i in duo_list:
#                     result = result*i
#                 cumTypeAdv += result
#                 duo_list = [ ]
#                 result = 1
#     print(cumTypeAdv)

def calculator(pokemons1,pokemons2):
    duels = []
    duo_list = []
    cumTypeAdv = 0
    result = 1
    for attack in pokemons1:
        attack = attack.split(" ")
        for defense in pokemons2:
            defense = defense.split(" ")
            for type_attack in attack:
                for type_defense in defense:
                    duo_list.append(effects[type_attack][type_defense])

            if len(attack) >= 2 and len(defense) ==1:
                cumTypeAdv += max(duo_list)

            elif len(attack) >= 2 and len(defense) >= 2:
                for i in range(0,len(duo_list),len(defense)):
                    for num in duo_list[i:i+len(defense):]:
                        result = result * num
                    duels.append(result)
                    result = 1   
                cumTypeAdv += max(duels)
                duels = [ ]

            elif len(attack) == 1 and len(defense) ==1:
                cumTypeAdv += max(duo_list)

            elif len(attack) == 1 and len(defense) >=2:
                for i in duo_list:
                    result = result *i
                cumTypeAdv += result

            result = 1
            duo_list = [ ]

    return(cumTypeAdv)


def game(number1,number2,listpok):
    listpok = listpok.split(",")
    pokemons1 = listpok[0:number1:]
    pokemons2 = listpok[number1:number1+number2:]
    player1_val = calculator(pokemons1,pokemons2)
    player2_val = calculator(pokemons2,pokemons1)
    if player1_val >player2_val:
        return "{:.1f}".format(player1_val),"{:.1f}".format(player2_val),"ME"
    elif player1_val==player2_val:
        return "{:.1f}".format(player1_val),"{:.1f}".format(player2_val),"BALANCE"
    elif player1_val<player2_val:
        return "{:.1f}".format(player1_val),"{:.1f}".format(player2_val),"FOE"

print(game(4,4,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))