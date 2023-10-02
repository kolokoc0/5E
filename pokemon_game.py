import json

with open ('effectiveness_new.json') as file:
    effects = json.load(file)

def calculator(number1,number2,listpok):
    duo_list = []
    cumTypeAdv = 0
    result = 1
    listpok = listpok.split(",")
    pokemons1 = listpok[0:number1:]
    pokemons2 = listpok[number1:number2+1+1:]
    for attack in pokemons1:
        attack = attack.split(" ")
        for defense in pokemons2:
            defense = defense.split(" ")
            if len(attack) ==2 and len(defense) ==1:
                for type_attack in attack:
                    for type_defense in defense:
                        duo_list.append(effects[type_attack][type_defense])
                cumTypeAdv += max(duo_list)
                duo_list = [ ]
            elif len(attack) ==2 and len(defense) ==2:
                for type_attack in attack:
                    for type_defense in defense:
                        duo_list.append(effects[type_attack][type_defense])
                cumTypeAdv += max(duo_list)
                duo_list = [ ]
            elif len(attack) ==1 and len(defense)==1:
                for type_attack in attack:
                    for type_defense in defense:
                        duo_list.append(effects[type_attack][type_defense])
                cumTypeAdv += duo_list[0]
                duo_list = [ ]
            elif len(attack) ==1 and len(defense) ==2:
                for type_attack in attack:
                    for type_defense in defense:
                        duo_list.append(effects[type_attack][type_defense])
                for i in duo_list:
                    result = result*i
                cumTypeAdv += result
                duo_list = [ ]
                result = 1
    print(cumTypeAdv)






calculator(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")





