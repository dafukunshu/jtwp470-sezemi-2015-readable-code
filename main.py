#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# レシピにIDをふった辞書 ex. id:recipe_name (idはint)
recipe_table = dict()


def dump_table():
    for id, recipe in recipe_table.items():
        print("{id}: {recipe}".format(id=str(id), recipe=recipe), end="")


if __name__ == "__main__":
    with open("recipe-data.txt", "r") as recipes:
        for id, recipe in enumerate(recipes):
            recipe_table[id] = recipe

    dump_table()
