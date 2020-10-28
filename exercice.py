#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
# def compare_files(first_file: str,sec_file: str):
#     with open(first_file,"r", encoding="utf-8") as f1, open(sec_file,"r",encoding="utf-8") as f2:
#         same = True
#         while same:
#             a = f1.read(1)
#             b = f2.read(1)
#             same = a==b
#     return -1 if same else f1.tell()
#     #     for _ in first_file:
#     #         if f1.read(1) != f2.read(1):
#     #             return "false"
#     # return "true"
# def triple_space(file1,file2):
#     with open(file1, "r") as data,open(file2, "w") as result:
#         text = data.read()

#         new_text = text.replace(" ", "   ")
#         result.write(new_text)
# def assign_note_letter(note_file, target_file):
#     correspondances = {​​20: "F", 40: "D", 50: "C", 70: "B", 85: "A"}​​
#     results = []
#     with open(note_file, 'r') as note_data, open(target_file, 'w') as target:
#         for line in note_data.readlines():
#             note = float(line)
#             for grade in correspondances.keys():
#                 if grade == 85 and note > grade:
#                     results.append("A*\n")
#                 if note <= grade:
#                     results.append(correspondances[grade] + "\n")
#                     break
#         target.writelines(results)
# def livre_recettes(fichier_recettes):
#     reponse = input("Voulez-vous ajouter(1),modifier(2) ou supprimer(3) une recette? Selectionner un numero")
#     if reponse == 1:
#         line = input("Que souhaitez-vous ajouter?")
#         ajouter_recette(fichier_recettes, line)
#     elif reponse == 2:
#         modifier_recette()
#     elif reponse == 3:
#         line = input("Quel texte souhaitez-vous supprimer?")
#         supprimer_recette(fichier_recettes,line)
#     else:
#         return "invalid entry"
# def ajouter_recette(fichier, ligne):
#     with open (fichier, "a") as recettes:
#         recettes.write(ligne)
# def modifier_recette():

# def supprimer_recette(fichier,ligne):
#     with open (fichier, "r+") as recettes:
#         data = recettes.readlines()
#         for i in data:
#             if i == ligne:
#                 del i
# def essai_trier_nombre(txt):
#     num =["0","1","2","3","4","5","6","7","8","9"]
#     num_to_sort =[]
#     str_nums = ""
#     with open(txt, "r") as data:
#         itera = iter(data.read())
#         for i in data.read():
#             for elem in i:
#                 elem_iter = iter(i)
#                 if elem in num:
#                     str_nums = elem
#                     if next(elem_iter) == " ":
#                         num_to_sort.append(elem)
#                     else:
#                         while next(elem_iter) in num:
#                             str_nums = str_nums + next()
#     return sorted(num_to_sort)
def solution_trier_nombres(fichier):
    with open(fichier, "r") as texte:
        return sorted([int(word) for word in texte.read().split() if word.isdigit()])

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(compare_files("text.txt","text1.txt"))
    solution_trier_nombres("exemple.txt")