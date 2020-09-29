#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        pass

    return []


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mota: imput("entrer un mot: ")
        motb: imput("entrer un deuxieme mot: ")
        if car in mota == cara in motb:
            return True
            

 


def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        avg = sum(value) / len(value)
        if len(best_student) == 0: 
            best_student = [key: avg}
                            
        if list(best_student.values())[0] < avg:
            best_student = {key: avg}
    
    return {}
                            


def frequence(sentence: str) -> dict:
    frequency = dict()
                            
    for car in sentence:
        list(range(0: len(sentence))
             frequency[letter] = sentence.count(letter)
             
     sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=true)
     for key in sorted_keys:
             if frequency[key] > 5:
                print(f"Le caratere {key} revient {frequency[key]} fois.")
                            

    return frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recettes = dict()
             nom_de_recette = input("entrer le nom de votre recette: \n")
             recettes[nom_de_recette] = input("entrer l'ingredient: ")
   
             
             
   name = =input("entrez le nom de votre recette:\n")
             ingrediants = input("entrez la liste d,ingredients de la recette, svp s/parer les ingr/dients par une ,\n").split(",")
             return {name: ingrediants}



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
           name = input("entrer le nom de votre recette: \n")
           if name in ingrdients:
             print(ingredients[name])
           else:
             print("la recette demand/e n<existe pas!")
             print(f"Les recettes existantes sont: {list(ingredients.keys())}")

def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
