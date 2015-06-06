#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    with open("recipe-data.txt", "r") as recipes:
        for recipe in recipes:
            print(recipe)
