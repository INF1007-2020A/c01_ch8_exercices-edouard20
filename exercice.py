#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def compare_files(first_file: str,sec_file: str):
    with open(first_file,"r", encoding="utf-8") as f1, open(sec_file,"r",encoding="utf-8") as f2:
        same = True
        while same:
            a = f1.read()
            b = f2.read()
            same = a==b
        print(same)
    return -1 if same else f1.tell()
    #     for _ in first_file:
    #         if f1.read(1) != f2.read(1):
    #             return "false"
    # return "true"
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(compare_files("text.txt","text1.txt"))