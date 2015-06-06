#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# レシピにIDをふった辞書 ex. id:recipe_name (idはint)
recipe_table = dict()


def dump_table():
    for id, recipe in recipe_table.items():
        print("{id}: {recipe}".format(id=str(id), recipe=recipe), end="")


if __name__ == "__main__":
    with open("recipe-data.txt", "r") as recipes:
        for id, recipe in enumerate(recipes):
            recipe_table[id] = recipe
            print(recipe_table) ##
    if len(sys.argv) <= 1:
        dump_table()
    else:
        argv_len = len(sys.argv)
        print(id)
        if id < 0 or argv_len > id:
            print("error") 
            sys.exit(1)
        
        # TODO: idが範囲外のときにErrorなどを出す refer to memo.md
        # TODO: id が正しくないものを出力してしまうのを直す
        args_id = sys.argv[1]
        print("{id}: {recipe}".format(
            id=str(args_id), recipe=recipe_table.get(int(args_id))))
